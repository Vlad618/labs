from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.order_states import OrderFSM
from keyboards.reply import main_menu

router = Router()

@router.message(F.text == "📦 Оформити замовлення")
async def start_order(message: Message, state: FSMContext):
    data = await state.get_data()
    cart = data.get("cart", [])
    if not cart:
        await message.answer("🛒 Ваш кошик порожній! Додайте товари з каталогу.")
        return
    await message.answer("✍️ Введіть ваше ім'я:")
    await state.set_state(OrderFSM.name)

@router.message(OrderFSM.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("📞 Введіть номер телефону:")
    await state.set_state(OrderFSM.phone)

@router.message(OrderFSM.phone)
async def get_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("🏠 Введіть адресу доставки:")
    await state.set_state(OrderFSM.address)

@router.message(OrderFSM.address)
async def finish_order(message: Message, state: FSMContext):
    data = await state.get_data()
    cart = data.get("cart", [])
    total = sum(item['price'] * item.get('quantity', 1) for item in cart)
    cart_text = "\n".join([
        f"{item['name']} × {item.get('quantity',1)} – {item['price'] * item.get('quantity',1)} грн"
        for item in cart
    ])
    await message.answer(
        f"✅ Замовлення оформлено!\n\n🛒 Кошик:\n{cart_text}\n💰 Сума: {total} грн\n\n"
        f"👤 Ім'я: {data['name']}\n📞 Телефон: {data['phone']}\n🏠 Адреса: {message.text}",
        reply_markup=main_menu
    )
    await state.clear()