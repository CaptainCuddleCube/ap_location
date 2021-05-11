import logging
import sys
from os import environ

logger = logging.getLogger("ap_location")

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(
    logging.Formatter(
        "%(levelname)s: %(asctime)27s [%(filename)s:%(lineno)s] " "%(message)s"
    )
)

logger.addHandler(console_handler)
logger.setLevel(logging.INFO)


API_TOKEN = environ.get("API_TOKEN")
API_URL = "https://www.googleapis.com/geolocation/v1/geolocate"
INDEX_THRESHOLD = environ.get("INDEX_THRESHOLD", -82)
