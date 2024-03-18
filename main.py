import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher, F
from aiogram.client import bot
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, BotCommand, CallbackQuery
from root import TOKEN
from aiogram import types
from botton import button1, button2

logging.basicConfig(level=logging.INFO)

dp = Dispatcher()


########################################################

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("""Assalomu alaykum! Botdan foydalanish uchun avval ro'yxatdan o'tishingizni iltimos qilamiz.

Keling, avval xizmat ko‘rsatish 🇺🇿 tilini tanlab olaylik.

________________________________

Здравствуйте! Для продолжения просим вас пройти регистрацию.

Выберите 🇷🇺 язык обслуживания.""", reply_markup=button1)


@dp.message(F.text == "Categories")
async def command_help_handler(message: Message) -> None:
    await message.answer("Categories bro!", reply_markup=button2)


@dp.message(F.text == "⬅️ Back")
async def command_back_handler(message: Message) -> None:
    await message.answer("⬅️ Back bro!", reply_markup=button1)


@dp.message(F.text == "VPS 1")
async def command_back_handler(message: Message) -> None:
    await message.answer("VPS 1"
                         "\n\nMemory: 1032 RAM"
                         "\nCORE: 2"
                         "\nStorage: 20 GB"
                         "\nOS: WINDOW 2012"
                         "\n\nPRICE: 50$", reply_markup=button2)

async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)
    await bot.set_my_commands([
        BotCommand(command="botni ishga tushirish!", description="start"),  # noqa
        BotCommand(command="foydalanuvchiga yordam berish!", description="help"),  # noqa
        BotCommand(command="foydalanuvchini kanalga olib kiradi!", description="silka")])  # noqa


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())