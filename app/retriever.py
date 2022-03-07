import sentinelhub
from sentinelhub import SentinelHubRequest, DataCollection, MimeType, CRS, BBox, SHConfig
import json
from datetime import datetime, timedelta
from PIL import Image
from numpy import asarray
import math


class Switch(dict):
    def __getitem__(self, item):
        for key in self.keys():
            if key[0] <= item < key[1]:
                return super().__getitem__(key)
        raise KeyError(item)


# Prepare NDVI switch
switch_ndvi = Switch({
    (-math.inf, -1.1): [0, 0, 0],
    (-1.1, -0.2): [191, 191, 191],
    (-0.2, -0.1): [219, 219, 219],
    (-0.1, 0): [255, 255, 224],
    (0, 0.025): [255, 250, 204],
    (0.025, 0.05): [237, 232, 181],
    (0.05, 0.075): [222, 217, 156],
    (0.075, 0.1): [204, 199, 130],
    (0.1, 0.125): [189, 184, 107],
    (0.125, 0.15): [176, 194, 97],
    (0.15, 0.175): [163, 204, 89],
    (0.175, 0.2): [145, 191, 82],
    (0.2, 0.25): [128, 179, 71],
    (0.25, 0.3): [112.2, 163, 64],
    (0.3, 0.35): [97, 150, 54],
    (0.35, 0.4): [79, 138, 46],
    (0.4, 0.45): [64, 125, 36],
    (0.45, 0.5): [48, 110, 28],
    (0.5, 0.55): [33, 97, 18],
    (0.55, 0.6): [15, 84, 10],
    (0.6, math.inf): [0, 69, 0]
})

# Load client data from configs
with open("data/secrets.json", "r", encoding="utf-8") as secrets_file:
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
                bands: ["B04", "B08"]
            }],
            output: {
                bands: 3
            }
        };
    }

    function evaluatePixel(sample) {
        return [sample.B04, sample.B08, 0];
    }
"""


def get_image(bounding_box: list[float], days=15, save_image=False):
    now = datetime.now().date()
    then = now - timedelta(days=days)
    bbox = BBox(bbox=bounding_box, crs=CRS.WGS84)
    request = SentinelHubRequest(
        evalscript=eval_script,
        input_data=[SentinelHubRequest.input_data(data_collection=DataCollection.SENTINEL2_L2A,
                                                  time_interval=(then.strftime("%Y-%m-%d"),
                                                                 now.strftime("%Y-%m-%d")),
                                                  mosaicking_order='leastCC')],
        responses=[SentinelHubRequest.output_response("default", MimeType.JPG)],
        bbox=bbox,
        size=[*sentinelhub.bbox_to_dimensions(bbox, 10)],
        config=config,
        data_folder="images")
    return request.get_data(save_data=save_image)[0]


def colour_ndvi(input_=None, output_="out.jpg", bbox=None, days=15, save_image=False) -> None:
    if input_ is None and bbox is None:
        raise ValueError("Either input_ or bbox must be specified")
    elif input_ is None:
        image_arr = get_image(bbox, days=days, save_image=save_image)
    else:
        image_arr = asarray(Image.open(input_))  # noqa
    for y, row in enumerate(image_arr):
        for x, pixel in enumerate(row):
            NIR, RED = pixel[1], pixel[0]
            denominator: float = float(NIR) + float(RED)
            ndvi: float = (NIR - RED) / denominator if denominator != 0 else 0.0
            image_arr[y, x][0], image_arr[y, x][1], image_arr[y, x][2] = switch_ndvi[ndvi]
    Image.fromarray(image_arr).save(output_)
