import os
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    FSInputFile,
)

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# 📌 Главное меню с 4 кнопками
main_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📜 История", callback_data="history")],
    [InlineKeyboardButton(text="💸 Поддержать", url="https://t.me/GrayKitBot")],
    [InlineKeyboardButton(text="📄 PDF", callback_data="pdf")],
    [InlineKeyboardButton(text="📥 Как получить?", callback_data="how_to_get")],
])

# 🟢 /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Добро пожаловать в проект GrayKitBot!\n\nВыберите действие 👇",
        reply_markup=main_keyboard
    )

# 📜 История
@dp.callback_query(F.data == "history")
async def show_history(callback: types.CallbackQuery):
    await callback.message.answer(
        "<b>📜 История челленджа:</b>\n\n"
        "Ты смотришь на историю создания проекта. Это начало."
    )
    await callback.answer()

# 📄 PDF
@dp.callback_query(F.data == "pdf")
async def send_pdf(callback: types.CallbackQuery):
    try:
        pdf_path = "challenge.pdf"
        pdf_file = FSInputFile(pdf_path)
        await callback.message.answer_document(pdf_file, caption="📄 Вот файл челленджа")
    except FileNotFoundError:
        await callback.message.answer("Файл PDF не найден.")
    await callback.answer()

# 📥 Как получить?
@dp.callback_query(F.data == "how_to_get")
async def how_to_get(callback: types.CallbackQuery):
    await callback.message.answer(
        "<b>📥 Как получить файл?</b>\n\n"
        "Просто нажми на кнопку 📄 PDF выше — и бот отправит тебе файл.\n\n"
        "Если кнопка не работает — файл еще не загружен в систему."
    )
    await callback.answer()

# /share
@dp.message(Command("share"))
async def share_cmd(message: types.Message):
    share_text = (
        "🚨 Новый челлендж!\n\n"
        "Поддержи проект GrayKit — анонимно, быстро и с пользой.\n"
        "👉 https://t.me/GrayKitBot\n\n"
        "#донат #челлендж #анонимно"
    )
    await message.answer(share_text)

# 🔁 Старт бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
