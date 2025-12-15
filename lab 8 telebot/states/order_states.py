from aiogram.fsm.state import StatesGroup, State

class OrderFSM(StatesGroup):
    name = State()
    phone = State()
    address = State()
    quantity = State()