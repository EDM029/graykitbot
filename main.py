
import asyncio
import logging
import random
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# ---- Ложный счётчик ----
fake_buyers = random.randint(173, 286)

# ---- Кнопки ----
menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📖 История", callback_data="history")],
    [InlineKeyboardButton(text="📄 Получить PDF (5 USDT или экв. в TON)", callback_data="get_pdf")],
    [
        InlineKeyboardButton(text="💸 Оплатить TON", url="https://t.me/GrayKitBot?start=ton"),
        InlineKeyboardButton(text="💸 Оплатить USDT", url="https://t.me/GrayKitBot?start=usdt")
    ],
])

# ---- Описание старта ----
welcome_text = f"""
👋 Добро пожаловать в *GrayKitBot* — твой доступ к сливу самых 🔥 рабочих серых схем 2025 года.

🔐 *PDF-документ* содержит серый лендинг, пошаговый запуск, автоворонку и готовые тексты. Всё, чтобы заработать 💸.

💥 *{fake_buyers} копий уже куплено!* Осталось *{random.randint(4, 11)}* штук по 5 USDT.

👇 Нажми, чтобы купить ↓
"""

# ---- Команда /start ----
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(welcome_text, reply_markup=menu, parse_mode="Markdown")

# ---- Обработка кнопок ----
@dp.callback_query(F.data == "history")
async def history(call: CallbackQuery):
    await call.answer()
    await call.message.answer("🧠 *История*: Я всё потерял. Последняя попытка. Если не сработает — удалю телегу и сдам ноутбук в ломбард.\n\nЯ не прошу денег. Я даю схему. Только для тех, кто решит использовать.", parse_mode="Markdown")

@dp.callback_query(F.data == "get_pdf")
async def get_pdf(call: CallbackQuery):
    await call.answer()
    await call.message.answer("🚫 PDF-документ доступен *только после оплаты 5 USDT или TON*. Нажми нужную кнопку для оплаты.", parse_mode="Markdown")

# ---- Команда /share ----
@dp.message(F.text == "/share")
async def share(message: Message):
    await message.answer("💣 Поделись этим ботом с другом, которому тоже нужно выбраться из задницы:\n\nhttps://t.me/GrayKitBot")

# ---- Запуск бота ----
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
