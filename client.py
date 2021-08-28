import requests
import logging
from config import BINANCE_FLEXI_URL


def connect():
    response = requests.get(BINANCE_FLEXI_URL)
    logging.info(response.json())
    return response.json()

