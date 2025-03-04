import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message # type: ignore
from aiogram.filters import Command # type: ignore
import logging

# Указываем токен бота (замени на свой!)
TOKEN = "7972940989:AAEXLLhcedRhzDDQr8eIKriINkblHgG9zLo"

# Создаём бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Команда /start
@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Привет! Я бот 'Монетка'. Напиши /flip, и я подброшу монету!")

# Команда /flip (бросок монеты)
@dp.message(Command("flip"))
async def flip_coin(message: Message):
    result = random.choice(["Орел 🦅", "Решка 🏵"])
    await message.answer(f"Монетка подброшена: {result}")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
