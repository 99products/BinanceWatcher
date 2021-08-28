import requests
import logging
from config import FLEXIBLE_STAKING_URL, LOCKED_STAKING_URL

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')


def read_locked_staking():
    logging.info('Reading Locked Staking info')
    response = requests.get(LOCKED_STAKING_URL)
    return response.json()


def read_flexible_staking():
    logging.info('Reading Flexible Staking info')
    response = requests.get(FLEXIBLE_STAKING_URL)
    return response.json()

