from aiogram.dispatcher.filters.state import State, StatesGroup

class menu_State(StatesGroup):
    id = State()
    qr = State()
