from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext
from data.furniture import furniture
from keyboards.inline import categories_keyboard
from keyboards.reply import main_menu
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from states.order_states import OrderFSM

router = Router()

main_menu_with_catalog = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📦 Оформити замовлення")],
        [KeyboardButton(text="🔙 Повернутися до каталогу")]
    ],
    resize_keyboard=True
)

@router.message(F.text == "🛒 Каталог")
async def show_catalog(message: Message):
    await message.answer(
        "📂 Оберіть категорію меблів:",
        reply_markup=categories_keyboard(furniture.keys())
    )

@router.callback_query(F.data.startswith("cat:"))
async def show_products(call: CallbackQuery):
    category = call.data.split("cat:")[1]
    products = furniture.get(category, [])
    kb = InlineKeyboardMarkup(inline_keyboard=[])
    for product in products:
        kb.inline_keyboard.append(
            [InlineKeyboardButton(
                text=f"{product['name']} – {product['price']} грн",
                callback_data=f"select:{product['id']}"
            )]
        )
    await call.message.answer(f"{category}:", reply_markup=kb)
    await call.answer()

@router.callback_query(F.data.startswith("select:"))
async def select_quantity(call: CallbackQuery, state: FSMContext):
    product_id = int(call.data.split(":")[1])
    for items in furniture.values():
        for product in items:
            if product["id"] == product_id:
                await state.update_data(selected_product=product)
                await call.message.answer("Введіть кількість товару, яку бажаєте замовити:")
                await state.set_state(OrderFSM.quantity)
                break
    await call.answer()

@router.message(OrderFSM.quantity)
async def add_to_cart(message: Message, state: FSMContext):
    if not message.text.isdigit() or int(message.text) <= 0:
        await message.answer("Введіть будь ласка правильну кількість (ціле число більше 0):")
        return
    quantity = int(message.text)
    data = await state.get_data()
    product = data.get("selected_product")
    cart = data.get("cart", [])
    cart.append({**product, "quantity": quantity})
    await state.update_data(cart=cart)
    await message.answer(
        f"✅ Додано {quantity} × {product['name']} у кошик.\n\nОберіть наступну дію:",
        reply_markup=main_menu_with_catalog
    )
    await state.set_state(None)  # ← скидаємо стан, щоб кнопки працювали

@router.message(F.text == "🔙 Повернутися до каталогу")
async def back_to_catalog(message: Message):
    await message.answer(
        "📂 Оберіть категорію меблів:",
        reply_markup=categories_keyboard(furniture.keys())
    )