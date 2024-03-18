from aiogram import types

kirish1 = [
    [types.KeyboardButton(text="Categories")],
    [types.KeyboardButton(text="Profile"), types.KeyboardButton(text="Deposit")],
    [types.KeyboardButton(text="Support")]
]

button1 = types.ReplyKeyboardMarkup(keyboard=kirish1, resize_keyboard=True)

########################################################################################################################

kirish2 = [
    [types.KeyboardButton(text="VPS 1"), types.KeyboardButton(text="VPS 2")],
    [types.KeyboardButton(text="VPS 3"), types.KeyboardButton(text="VPS 4")],
    [types.KeyboardButton(text="⬅️ Back")]
]

button2 = types.ReplyKeyboardMarkup(keyboard=kirish2, resize_keyboard=True)
