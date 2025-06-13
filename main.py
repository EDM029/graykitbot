import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.enums import ParseMode
import logging
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
PDF_FILE_PATH = "schemes.pdf"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

# --- Основной текст и кнопки ---
WELCOME_TEXT = (
    "<b>💼 Gray Kit: Cерые схемы 2025</b>\n\n"
    "Топ-методы заработка, которые работают прямо сейчас.\n"
    "Без попрошайничества. Только готовые решения.\n\n"
    "⚠️ Осталось всего <b>17 копий</b>. Потом доступ будет закрыт.\n"
    "Цена: <b>5 USDT</b> или эквивалент в TON."
)

history_text = (
    "📊 <b>Легенда:</b> Этот набор схем собран вручную, отработан на практике, упакован в PDF.\n\n"
    "Если ты хочешь <b>заработать нестандартно</b> — это твой шанс.\n"
    "Работает только для тех, кто применяет. Не для нытиков."
)

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="💸 Оплатить 5 USDT (TRC-20)", url="https://tronscan.org/#/address/TUVCh2u3gqwU8kfwzgjmJMUFPXTneFf9Kk")],
    [InlineKeyboardButton(text="💎 Оплатить в TON", url="https://tonviewer.com/UQCBoBwjzbgw1eptiMrKbdpmX83al1qlaKFnUvI86zQnW4YP")],
    [InlineKeyboardButton(text="📥 Получить PDF", callback_data="get_pdf")],
    [InlineKeyboardButton(text="📖 История", callback_data="history")],
])

# --- Команды ---
@dp.message(commands=["start"])
async def start_cmd(message: types.Message):
    await message.answer(WELCOME_TEXT, reply_markup=keyboard, parse_mode=ParseMode.HTML)

@dp.callback_query(lambda c: c.data == "get_pdf")
async def send_pdf(callback_query: types.CallbackQuery):
    await callback_query.message.answer_document(
        types.FSInputFile(PDF_FILE_PATH),
        caption="📦 Вот твой файл. Не передавай другим.",
    )
    await callback_query.answer()

@dp.callback_query(lambda c: c.data == "history")
async def show_history(callback_query: types.CallbackQuery):
    await callback_query.message.answer(history_text, parse_mode=ParseMode.HTML)
    await callback_query.answer()

# --- Запуск ---
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
