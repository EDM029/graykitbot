import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
import asyncio
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📥 Получить PDF", callback_data="get_pdf")],
    [InlineKeyboardButton(text="💸 Поддержать", url="https://t.me/ltchallengebot")],
    [InlineKeyboardButton(text="📊 История", callback_data="history")],
    [InlineKeyboardButton(text="📤 Расшарить", switch_inline_query="🔥 Челлендж от Грея")],
    [InlineKeyboardButton(text="🚀 Другие схемы", url="https://t.me/GrayKitBot")]
])

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Привет! Это бот GrayKit. Выбери действие ниже:", reply_markup=kb)

@dp.callback_query(lambda c: c.data == "get_pdf")
async def send_pdf(callback_query: types.CallbackQuery):
    await callback_query.message.answer_document(types.FSInputFile("graykit.pdf"))

@dp.callback_query(lambda c: c.data == "history")
async def show_history(callback_query: types.CallbackQuery):
    await callback_query.message.answer("История скоро появится.")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
