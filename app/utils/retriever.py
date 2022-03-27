import json
import math
from datetime import datetime, timedelta

from pathlib import Path

import sentinelhub
from PIL import Image
from sentinelhub import SentinelHubRequest, DataCollection, MimeType, CRS, BBox, SHConfig, Geometry
from shapely import geometry


class Switch(dict):
    def __getitem__(self, item):
        for key in self.keys():
            if key[0] < item <= key[1]:
                return super().__getitem__(key)
        raise KeyError(item)


# Prepare NDVI switch
switch_ndvi = Switch({
    (-math.inf, -0.2): [0, 0, 0],
    (-0.2, 0): [165, 0, 38],
    (0, 0.1): [215, 48, 39],
    (0.1, 0.2): [244, 109, 67],
    (0.2, 0.3): [253, 174, 97],
    (0.3, 0.4): [254, 224, 139],
    (0.4, 0.5): [255, 255, 191],
    (0.5, 0.6): [217, 239, 139],
    (0.6, 0.7): [166, 217, 106],
    (0.7, 0.8): [102, 189, 99],
    (0.8, 0.9): [26, 152, 80],
    (0.9, math.inf): [0, 104, 55]
})

APP_FOLDER = Path(__file__).parent.parent

# Load client data from configs
with open(APP_FOLDER.joinpath("data/secrets.json"), "r",
          encoding="utf-8") as secrets_file:
    secrets: dict = json.load(secrets_file)

# Credentials
config = SHConfig()
config.sh_client_id = secrets["client_id"]
config.sh_client_secret = secrets["client_secret"]
eval_script = """
    //VERSION=3

    function setup() {
        return {
            input: [{
                bands: ["B02", "B03", "B04", "B08"]
            }],
            output: [{
                id: "rgb",
                bands: 3
            }, {
                id: "ndvi",
                bands: 3
            }]
        };
    }

    function evaluatePixel(sample) {
        return {
            rgb: [2.5 * sample.B04, 2.5 * sample.B03, 2.5 * sample.B02],
            ndvi: [sample.B04, sample.B08, 0]
        };
    }
"""


def get_image(bounding_box: list[float] | BBox, days=15, save_image=False, delay=0):
    now = datetime.now().date() - timedelta(days=delay)
    then = now - timedelta(days=days)
    if not isinstance(bounding_box, BBox):
        bbox = BBox(bbox=bounding_box, crs=CRS.WGS84)
    else:
        bbox = bounding_box
    request = SentinelHubRequest(
        evalscript=eval_script,
        input_data=[SentinelHubRequest.input_data(data_collection=DataCollection.SENTINEL2_L2A,
                                                  time_interval=(then.strftime("%Y-%m-%d"),
                                                                 now.strftime("%Y-%m-%d")),
                                                  mosaicking_order='leastCC')],
        responses=[SentinelHubRequest.output_response("rgb", MimeType.JPG),
                   SentinelHubRequest.output_response("ndvi", MimeType.JPG)],
        bbox=bbox,
        size=[*sentinelhub.bbox_to_dimensions(bbox, 10)],
        config=config,
        data_folder="images")
    return request.get_data(save_data=save_image)[0]


def colour_ndvi(output_="out.jpg", polygon=None, days=15, save_image=False,
                delay=0) -> None:
    pure_polygon = geometry.Polygon(polygon)
    bbox = Geometry(pure_polygon, CRS.WGS84).bbox
    images = get_image(bbox, days=days, save_image=save_image, delay=delay)
    image_arr_rgb = images["rgb.jpg"]
    image_arr_ndvi = images["ndvi.jpg"]
    height, width, _ = image_arr_rgb.shape
    t_w, t_h = bbox.upper_right[0] - bbox.lower_left[0], bbox.upper_right[1] - bbox.lower_left[1]
    edge_x, edge_y = bbox.lower_left[0], bbox.upper_right[1]
    for y, row in enumerate(image_arr_rgb):
        for x, pixel in enumerate(row):
            x_perc, y_perc = x / width, y / height
            point = geometry.Point(
                edge_x + x_perc * t_w,
                edge_y - y_perc * t_h)
            if pure_polygon.contains(point):
                NIR, RED = float(image_arr_ndvi[y][x][1]), float(image_arr_ndvi[y][x][0])
                denominator = NIR + RED
                ndvi = (NIR - RED) / denominator if denominator != 0 else 0.0
                image_arr_rgb[y, x][0], image_arr_rgb[y, x][1], image_arr_rgb[y, x][2] = \
                    switch_ndvi[ndvi]
    Image.fromarray(image_arr_rgb).save(APP_FOLDER.joinpath(output_))
