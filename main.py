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

# 📌 Кнопочная клавиатура
main_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📜 История", callback_data="history")],
    [InlineKeyboardButton(text="💸 Поддержать", url="https://t.me/GrayKitBot")],  # можно заменить ссылку
    [InlineKeyboardButton(text="📄 PDF", callback_data="pdf")],
])

# 🟢 /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Добро пожаловать в проект GrayKitBot!\n\nВыберите действие 👇",
        reply_markup=main_keyboard
    )

# 🔁 Обработка callback-кнопок
@dp.callback_query(F.data == "history")
async def show_history(callback: types.CallbackQuery):
    text = (
        "<b>📜 История челленджа:</b>\n\n"
        "Я запустил анонимный челлендж по сбору средств. "
        "Каждый донат — шаг ближе к цели. "
        "История будет обновляться здесь."
    )
    await callback.message.answer(text)
    await callback.answer()

@dp.callback_query(F.data == "pdf")
async def send_pdf(callback: types.CallbackQuery):
    try:
        pdf_path = "challenge.pdf"  # название файла должно совпадать
        pdf_file = FSInputFile(pdf_path)
        await callback.message.answer_document(pdf_file, caption="📄 Вот файл челленджа")
    except FileNotFoundError:
        await callback.message.answer("Файл PDF не найден. Пожалуйста, загрузите файл 'challenge.pdf' в папку проекта.")
    await callback.answer()

# 📤 /share
@dp.message(Command("share"))
async def share_cmd(message: types.Message):
    share_text = (
        "🚨 Новый челлендж! 🚨\n\n"
        "Поддержи проект GrayKit — анонимно, без лишних слов.\n"
        "👉 https://t.me/GrayKitBot\n\n"
        "#донат #челлендж #анонимно"
    )
    await message.answer(share_text)

# 🔁 Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
