import client
import requests
import schedule
import time
from flask import Flask
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_polling
from config import bot_token, bot_channel_url, interval
import logging

bot = Bot(bot_token)
dp = Dispatcher(bot)
app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')


@dp.message_handler(commands=['get'])
async def get(message):
    data = get_available_assets()
    await bot.send_message('@bwatch_test_channel', data)


def get_available_assets():
    logging.info('Fetching information from Binance')
    locked_skating_json = client.read_locked_staking()
    flexible_skating_json = client.read_flexible_staking()
    logging.info('Completed fetching from Binance')
    is_available = False
    available_asset: str = ''
    available_asset += 'Assets currently availble in Locked Staking\n\n'
    for coin in locked_skating_json['data']:
        for product in coin['products']:
            if product['sellOut']:
                is_available = True
                available_asset += "{:<5}".format(product['asset']) + "\n"
    if not is_available:
        available_asset += "None\n"
    else:
        is_available = False

    available_asset += '\nAssets currently availble in Flexible Staking\n\n'
    for coin in flexible_skating_json['data']:
        for product in coin['projects']:
            if product['sellOut']:
                is_available = True
                available_asset += "{:<5}".format(product['asset']) + "\n"
    if not is_available:
        available_asset += "None\n"
        is_available = False
    return available_asset


@app.route('/', methods=["GET"])
def say_hello():
    return "Welcome to Binance Watcher!"


def poll():
    start_polling(dp, timeout=123)


def send_update_to_channel():
    logging.info('Sending update to telegram channel')
    url = bot_channel_url.format(token=bot_token, channel='@bwatch_test_channel', message=get_available_assets())
    response = requests.get(url)
    logging.info('Response: ' + str(response))


def schedule_checker():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    logging.info('Starting Binance Watcher...')
    schedule.every(interval).minutes.do(send_update_to_channel)
    schedule_checker()
#    send_update_to_channel()
