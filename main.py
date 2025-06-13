import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.enums import ParseMode
import random
import logging
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

PDF_FILE_PATH = "Ultimate_Gray_Schemes.pdf"
TON_WALLET = "UQCBoBwjzbgw1eptiMrKbdpmX83al1qlaKFnUvI86zQnW4YP"
USDT_WALLET = "TUVCh2u3gqwU8kfwzgjmJMUFPXTneFf9Kk"

FAKE_PURCHASES = random.randint(317, 563)

start_text = f"""
<b>💼 ULTIMATE GRAY SCHEMES — РАСКРЫТО</b>

⚠️ <b>Пока не поздно!</b>
Схемы массово сливают. Осталось всего <b>{FAKE_PURCHASES}</b> копий.

<b>Цена доступа: 5 USDT или эквивалент в TON</b>
Ты получаешь PDF-файл со всеми актуальными серыми связками, без лишнего буллшита.

👇 Выбери способ оплаты ниже:
"""

@dp.message(F.text == "/start")
async def start_handler(message: Message):
    kb = InlineKeyboardBuilder()
    kb.button(text="💸 Оплатить 5 USDT (TRC20)", url=f"https://tronscan.org/#/address/{USDT_WALLET}")
    kb.button(text="🌀 Оплатить TON", url=f"https://tonviewer.com/{TON_WALLET}")
    kb.button(text="✅ Получить PDF", callback_data="get_pdf")
    await message.answer(start_text, reply_markup=kb.as_markup())

@dp.callback_query(F.data == "get_pdf")
async def send_pdf(call: CallbackQuery):
    await call.answer()
    doc = FSInputFile(PDF_FILE_PATH)
    await call.message.answer_document(document=doc, caption="<b>📂 Твой файл: Ultimate Gray Schemes</b>")

@dp.message(F.text.lower().in_(["история", "history"]))
async def send_story(message: Message):
    await message.answer("<i>🧠 Это не попрошайничество. Это — продажа серой информации.
Вы или используете её и зарабатываете, или просто проходите мимо.</i>")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
