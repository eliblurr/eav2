from config import settings
import os

static_DIR = settings.STATIC_DIR or os.path.dirname(os.path.relpath(__file__))
image_DIR = f"{static_DIR}/images"
# items_DIR = "{image_DIR}/items".format(image_DIR=image_DIR)