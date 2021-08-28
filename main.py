import client
from flask import Flask, request
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_polling
from config import bot_token
import logging

bot = Bot(bot_token)
dp = Dispatcher(bot)
app = Flask(__name__)


@dp.message_handler(commands=['get'])
async def get(message):
    logging.info('getting')
    msgs = client.connect()
    logging.info(msgs)
    await bot.send_message(message.chat.id, msgs)


if __name__ == "__main__":
    logging.info('Starting Binance Watcher...')
    info = client.connect()
    start_polling(dp, timeout=123)

