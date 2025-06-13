import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.enums import ParseMode
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "вставь_сюда_токен_бота"

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# Клавиатура оплаты
def get_payment_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💰 Оплатить 5 USDT (TRC20)", url="https://tronscan.org/#/address/TUVCh2u3gqwU8kfwzgjmJMUFPXTneFf9Kk")],
        [InlineKeyboardButton(text="💰 Оплатить в TON", url="https://tonviewer.com/UQCBoBwjzbgw1eptiMrKbdpmX83al1qlaKFnUvI86zQnW4YP")],
        [InlineKeyboardButton(text="✅ Я оплатил(а)", callback_data="paid")]
    ])

@dp.message(F.text == "/start")
async def start_handler(message: Message):
    await message.answer(
        """<i>🧠 Это не попрошайничество. Это — продажа серой информации.

Ты получаешь PDF с рабочими серыми схемами.

📉 Цена: всего 5 USDT или эквивалент в TON.
📈 Счётчик: уже <b>134</b> человек приобрели сегодня.

👇 Жми кнопку ниже, чтобы оплатить и получить PDF.</i>""",
        reply_markup=get_payment_keyboard()
    )

@dp.callback_query(F.data == "paid")
async def paid_callback(callback: CallbackQuery):
    pdf_path = "Ultimate_Gray_Schemes.pdf"
    if os.path.exists(pdf_path):
        await callback.message.answer_document(FSInputFile(pdf_path))
        await callback.answer("✅ Файл отправлен", show_alert=True)
    else:
        await callback.answer("❌ PDF не найден. Свяжитесь с поддержкой.", show_alert=True)

@dp.message(F.text.lower().startswith("история"))
async def history_handler(message: Message):
    await message.answer(
        "<b>История</b>\n\nЭтот проект — ультимативная попытка монетизировать серый опыт. Ты не просто получаешь PDF — ты входишь в игру, где всё зависит от твоей решимости. Действуй — или останешься ни с чем.",
        parse_mode="HTML"
    )

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(dp.start_polling(bot))
