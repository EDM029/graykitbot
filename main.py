import logging
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold
import aiofiles
from datetime import datetime

TOKEN = "7357980179:AAEb62G3UYAkwaxkATGfbqc0R_4hQb_QlGc"

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# Кнопки оплаты
payment_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="💸 Оплатить 2 TON", url="https://tonkeeper.com/transfer/UQCBoBwjzbgw1eptiMrKbdpmX83al1qlaKFnUvI86zQnW4YP?amount=2")],
    [InlineKeyboardButton(text="💸 Оплатить 5 USDT (TRC20)", url="https://tronscan.org/#/address/TUVCh2u3gqwU8kfwzgjmJMUFPXTneFf9Kk")],
])

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "<b>🧠 Это не попрошайничество. Это — продажа серой информации.</b>\n\n"
        "🚫 Больше не будет бесплатных PDF-файлов. Только платный доступ.\n"
        "🔥 Уже более 130+ человек скачали. Осталось всего <b>17 копий</b>.\n\n"
        "💥 Никакой воды. Только серые схемы, которые можно применить сразу.\n"
        "💰 Оплата через TON или USDT. После — отправь хеш (txid), чтобы получить файл вручную.\n\n"
        "👇 Выбери способ оплаты:",
        reply_markup=payment_keyboard
    )

@dp.message()
async def handle_txid(message: types.Message):
    txid = message.text.strip()
    user_id = message.from_user.id
    username = message.from_user.username or "no_username"
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    async with aiofiles.open("payments.txt", mode="a") as f:
        await f.write(f"{now} | ID: {user_id} | @{username} | TXID: {txid}\n")

    await message.reply("✅ Твой хеш сохранён. Мы проверим и отправим PDF вручную в ближайшее время.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    dp.run_polling(bot)
