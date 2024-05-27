from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_keyboard_inline():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline = InlineKeyboardButton('Посмотреть', url='https://youtu.be/oOS43qK7qYE?si=wF6xyOZAIIKvet3o')
    but_inline2 = InlineKeyboardButton('Посмотреть', url='https://youtu.be/6SF05US2hKY?si=VHZS6dUxRwyvvOYm')
    keyboard_inline.add(but_inline, but_inline2)
    return keyboard_inline

def get_keyboard_inline2():
    keyboard_inline2 = InlineKeyboardMarkup(row_width=2)
    but_inline3 = InlineKeyboardButton('Посмотреть', url='https://youtu.be/cDTPgh4GzRw?si=qhQfzux3Y4R8YQxM')
    but_inline4 = InlineKeyboardButton('Посмотреть', url='https://youtu.be/Pe8_A9coILs?si=eLAEBGPyg8rB521T')
    keyboard_inline2.add(but_inline3, but_inline4)
    return keyboard_inline2

