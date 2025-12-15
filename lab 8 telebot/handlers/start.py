from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from keyboards.reply import start_menu, main_menu

router = Router()

@router.message(Command(commands=["start", "help"]))
async def start_cmd(message: Message):
    await message.answer(
        "👋 Вітаємо у магазині меблів! Натисніть 'Старт', щоб продовжити.",
        reply_markup=start_menu
    )

@router.message(lambda message: message.text == "🚀 Старт")
async def start_pressed(message: Message):
    await message.answer(
        "Оберіть дію:",
        reply_markup=main_menu
    )