import requests
from flask import Flask
import telebot
from config import bot_token, bot_channel_url
from db import check_staking_data, beautify
import logging

bot = telebot.TeleBot(bot_token)
app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')


@bot.message_handler(commands=['get'])
def get(message):
    locked_staking_info = check_staking_data('Locked')
    flexible_staking_info = check_staking_data('Flexible')
    msg = beautify(asset_set=locked_staking_info, staking_type='Locked')
    msg += beautify(asset_set=flexible_staking_info, staking_type='Flexible')
    bot.reply_to(message, msg)


def send_update_to_channel(msg):
    logging.info('Sending update to telegram channel')
    url = bot_channel_url.format(token=bot_token, channel='@bwatch_test_channel', message=msg)
    response = requests.get(url)
    logging.info('Response: ' + str(response))


@app.route('/', methods=["GET"])
def say_hello():
    return "Welcome to Binance Watcher!"
