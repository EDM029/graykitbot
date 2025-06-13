from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import Message, FSInputFile
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import F
import asyncio
import logging
import os

# Установим логгирование
logging.basicConfig(level=logging.INFO)

# Токен бота
TOKEN = "7357980179:AAEb62G3UYAkwaxkATGfbqc0R_4hQb_QlGc"

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

# PDF файл со схемами
PDF_PATH = "Ultimate_Gray_Schemes.pdf"

# Кнопки оплаты и шейринга
def create_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="💸 Оплатить в USDT (TRC20)", url="https://tronscan.org/#/address/TUVCh2u3gqwU8kfwzgjmJMUFPXTneFf9Kk")
    builder.button(text="💸 Оплатить в TON", url="https://tonviewer.com/UQCBoBwjzbgw1eptiMrKbdpmX83al1qlaKFnUvI86zQnW4YP")
    builder.button(text="📄 Скачать PDF", callback_data="get_pdf")
    builder.button(text="🚀 Расшарить", switch_inline_query="")
    return builder.as_markup()

# Обработка /start
@dp.message(F.text == "/start")
async def cmd_start(message: Message):
    text = (
        "<b>🧠 Это не попрошайничество.</b>\n"
        "<i>Это — продажа серой информации. Ты либо пользуешься ей, либо проходишь мимо.</i>\n\n"
        "Внутри PDF — самые жёсткие схемы и фишки.\n"
        "Никаких оправданий. Только действие."
    )
    await message.answer(text, reply_markup=create_keyboard())

# Обработка запроса PDF
@dp.callback_query(F.data == "get_pdf")
async def send_pdf(callback_query: types.CallbackQuery):
    pdf_file = FSInputFile(PDF_PATH)
    await callback_query.message.answer_document(pdf_file)
    await callback_query.answer()

# Основной запуск
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
