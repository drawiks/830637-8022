
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject

import asyncio

from .api import client

from .utils import logger

from .config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}! Я твой первый бот на aiogram 3.")

@dp.message(Command("encode"))
async def cmd_encode(message: types.Message, command: CommandObject):
    if command.args is None:
        await message.answer("oшиbка: введи текст! nример: /encode привет")
        return
    
    result = await client.request("encode", command.args)
    
    await message.answer(f": {result}")

# Хэндлер на любые текстовые сообщения (Эхо)
@dp.message()
async def echo_handler(message: types.Message):
    # message.answer просто отправляет текст, message.reply — отвечает на сообщение
    await message.reply(f"Ты написал: {message.text}")

# Запуск процесса поллинга (опроса серверов Telegram)
async def main():
    await dp.start_polling(bot)
