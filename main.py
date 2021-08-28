import client
from flask import Flask, request
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_polling
from config import bot_token
import logging

bot = Bot(bot_token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')


@dp.message_handler(commands=['get'])
async def get(message):
    data = get_available_assets()
    await bot.send_message(message.chat.id, data)


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


if __name__ == "__main__":
    logging.info('Starting Binance Watcher...')
    print(get_available_assets())
    start_polling(dp, timeout=123)

