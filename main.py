import asyncio
import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor

API_TOKEN = "YOUR_BOT_TOKEN_HERE"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

pdf_file_path = "gray_schemes_guide.pdf"
usdt_wallet = "TXkJ6dEkz5EmU7KoVRJMeFnBbc5kctiZAA"
ton_wallet = "EQDvKf-6l17S09Y0Eklufy8qL83DKxhJz7g1fIPhuykC5-bF"

fake_sales = 124
fake_remaining = 7

async def periodic_fake_updates():
    global fake_sales, fake_remaining
    while True:
        await asyncio.sleep(random.randint(180, 300))  # 3–5 минут
        if fake_remaining > 1:
            fake_sales += 1
            fake_remaining -= 1

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("💸 Купить за 5 USDT", callback_data="buy_usdt"),
        InlineKeyboardButton("💰 Купить за TON", callback_data="buy_ton"),
        InlineKeyboardButton("📄 Описание PDF", callback_data="description")
    )

    await message.answer(
        f"🕵️ Ты получил доступ к закрытой базе серых схем.\n"
        f"⚠️ Осталось: {fake_remaining} копий\n"
        f"💬 {fake_sales} человек уже купили PDF за последние 48 часов.",
        reply_markup=keyboard
    )

    await asyncio.sleep(30)
    await message.answer("🕔 Время идёт. Осталось 6 копий. Получи PDF сейчас — или упустишь.")

@dp.callback_query_handler(lambda c: c.data == 'buy_usdt')
async def process_buy_usdt(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await bot.send_message(
        callback_query.from_user.id,
        f"💸 Переведи 5 USDT (TRC20) на адрес:\n`{usdt_wallet}`\n"
        f"После оплаты PDF будет выслан в течение 1–3 минут."
    )

@dp.callback_query_handler(lambda c: c.data == 'buy_ton')
async def process_buy_ton(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await bot.send_message(
        callback_query.from_user.id,
        f"💰 Переведи эквивалент 5 USDT в TON на адрес:\n`{ton_wallet}`\n"
        f"После оплаты PDF будет выслан в течение 1–3 минут."
    )

@dp.callback_query_handler(lambda c: c.data == 'description')
async def process_description(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await bot.send_message(
        callback_query.from_user.id,
        "📄 Внутри PDF ты найдёшь:\n"
        "1. Серые схемы Telegram и Instagram\n"
        "2. Алгоритмы прогрева\n"
        "3. Подпольные лендинги и вирусные автоворонки\n"
        "4. Примеры текстов, офферов, доминов\n"
        "5. Гайды по трафику и перепродаже\n\n"
        "Цена — 5 USDT или TON."
    )

async def main():
    asyncio.create_task(periodic_fake_updates())
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
