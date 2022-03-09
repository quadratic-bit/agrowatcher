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


def get_image(bounding_box: list[float], days=15, save_image=False, delay=0):
    now = datetime.now().date() - timedelta(days=delay)
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


def colour_ndvi(input_=None, output_="out.jpg", bbox=None, days=15, save_image=False,
                delay=0) -> None:
    if input_ is None and bbox is None:
        raise ValueError("Either input_ or bbox must be specified")
    elif input_ is None:
        image_arr = get_image(bbox, days=days, save_image=save_image, delay=delay)
    else:
        image_arr = asarray(Image.open(input_))  # noqa
    for y, row in enumerate(image_arr):
        for x, pixel in enumerate(row):
            NIR, RED = float(pixel[1]), float(pixel[0])
            denominator = NIR + RED
            ndvi = (NIR - RED) / denominator if denominator != 0 else 0.0
            image_arr[y, x][0], image_arr[y, x][1], image_arr[y, x][2] = switch_ndvi[ndvi]
    Image.fromarray(image_arr).save(output_)
