from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def categories_keyboard(categories: list[str]) -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(inline_keyboard=[])
    for category in categories:
        kb.inline_keyboard.append(
            [InlineKeyboardButton(text=category, callback_data=f"cat:{category}")]
        )
    return kb

def products_keyboard(products: list[dict]) -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(inline_keyboard=[])
    for product in products:
        kb.inline_keyboard.append(
            [InlineKeyboardButton(
                text=f"{product['name']} – {product['price']} грн",
                callback_data=f"product:{product['id']}"
            )]
        )
    return kb