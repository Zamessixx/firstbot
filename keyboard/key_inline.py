from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_keyboard_inline():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline = InlineKeyboardButton('Посмотреть', url='https://translated.turbopages.org/proxy_u/en-ru.ru.a4849af1-665d91ad-436d7dab-74722d776562/https/en.wikipedia.org/wiki/Army_ranks_and_insignia_of_the_Russian_Federation')
    keyboard_inline.add(but_inline)
    return keyboard_inline

def get_keyboard_inline2():
    keyboard_inline2 = InlineKeyboardMarkup(row_width=2)
    but_inline3 = InlineKeyboardButton('Истребитель', url='https://ru.wikipedia.org/wiki/%D0%98%D1%81%D1%82%D1%80%D0%B5%D0%B1%D0%B8%D1%82%D0%B5%D0%BB%D1%8C')
    but_inline4 = InlineKeyboardButton('Танк', url='https://ru.wikipedia.org/wiki/%D0%A2%D0%B0%D0%BD%D0%BA')
    but_inline5 = InlineKeyboardButton('Боевой вертолет', url='https://ru.wikipedia.org/wiki/%D0%91%D0%BE%D0%B5%D0%B2%D0%BE%D0%B9_%D0%B2%D0%B5%D1%80%D1%82%D0%BE%D0%BB%D1%91%D1%82')
    but_inline6 = InlineKeyboardButton('Авианосец', url='https://ru.wikipedia.org/wiki/%D0%90%D0%B2%D0%B8%D0%B0%D0%BD%D0%BE%D1%81%D0%B5%D1%86')
    but_inline7 = InlineKeyboardButton('Ракетная установка', url='https://ru.wikipedia.org/wiki/%D0%A0%D0%B0%D0%BA%D0%B5%D1%82%D0%BD%D0%B0%D1%8F_%D0%BF%D1%83%D1%81%D0%BA%D0%BE%D0%B2%D0%B0%D1%8F_%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0')
    but_inline8 = InlineKeyboardButton('Крылатая ракета', url='https://ru.wikipedia.org/wiki/%D0%9A%D1%80%D1%8B%D0%BB%D0%B0%D1%82%D0%B0%D1%8F_%D1%80%D0%B0%D0%BA%D0%B5%D1%82%D0%B0')
    keyboard_inline2.add(but_inline3, but_inline4, but_inline5, but_inline6, but_inline7, but_inline8)
    return keyboard_inline2


def get_keyboard_inline3():
    keyboard_inline3 = InlineKeyboardMarkup(row_width=2)
    but1 = InlineKeyboardButton('Рядовой', url='https://ru.wikipedia.org/wiki/%D0%A0%D1%8F%D0%B4%D0%BE%D0%B2%D0%BE%D0%B9')
    but2 = InlineKeyboardButton('Ефрейтор', url='https://ru.wikipedia.org/wiki/%D0%95%D1%84%D1%80%D0%B5%D0%B9%D1%82%D0%BE%D1%80')
    but3 = InlineKeyboardButton('Младший сержант', url='https://ru.wikipedia.org/wiki/%D0%9C%D0%BB%D0%B0%D0%B4%D1%88%D0%B8%D0%B9_%D1%81%D0%B5%D1%80%D0%B6%D0%B0%D0%BD%D1%82')
    but4 = InlineKeyboardButton('Сержант', url='https://ru.wikipedia.org/wiki/%D0%A1%D0%B5%D1%80%D0%B6%D0%B0%D0%BD%D1%82')
    but5 = InlineKeyboardButton('Старший сержант', url='https://ru.wikipedia.org/wiki/%D0%A1%D1%82%D0%B0%D1%80%D1%88%D0%B8%D0%B9_%D1%81%D0%B5%D1%80%D0%B6%D0%B0%D0%BD%D1%82')
    but6 = InlineKeyboardButton('Старшина', url='https://ru.wikipedia.org/wiki/%D0%A1%D1%82%D0%B0%D1%80%D1%88%D0%B8%D0%BD%D0%B0')
    but7 = InlineKeyboardButton('Прапорщик', url='https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%B0%D0%BF%D0%BE%D1%80%D1%89%D0%B8%D0%BA')
    but8 = InlineKeyboardButton('Старший прапорщик', url='https://translated.turbopages.org/proxy_u/en-ru.ru.e801b8eb-665da14c-91890a74-74722d776562/https/en.wikipedia.org/wiki/Starshy_praporshchik')
    keyboard_inline3.add(but1, but2, but3, but4, but5, but6, but7, but8)
    return keyboard_inline3



def get_keyboard_inline4():
    keyboard_inline4 = InlineKeyboardMarkup(row_width=2)
    but_1 = InlineKeyboardButton('Младший лейтенант', url='https://ru.wikipedia.org/wiki/%D0%9C%D0%BB%D0%B0%D0%B4%D1%88%D0%B8%D0%B9_%D0%BB%D0%B5%D0%B9%D1%82%D0%B5%D0%BD%D0%B0%D0%BD%D1%82')
    but_2 = InlineKeyboardButton('Лейтинант', url='https://ru.wikipedia.org/wiki/%D0%9B%D0%B5%D0%B9%D1%82%D0%B5%D0%BD%D0%B0%D0%BD%D1%82')
    but_3 = InlineKeyboardButton('Старший лейтенант', url='https://ru.wikipedia.org/wiki/%D0%A1%D1%82%D0%B0%D1%80%D1%88%D0%B8%D0%B9_%D0%BB%D0%B5%D0%B9%D1%82%D0%B5%D0%BD%D0%B0%D0%BD%D1%82')
    but_4 = InlineKeyboardButton('Капитан', url='https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D0%BF%D0%B8%D1%82%D0%B0%D0%BD_(%D0%B2%D0%BE%D0%B8%D0%BD%D1%81%D0%BA%D0%BE%D0%B5_%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5)')
    but_5 = InlineKeyboardButton('Майор', url='https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D0%B9%D0%BE%D1%80')
    but_6 = InlineKeyboardButton('Подполковник', url='https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%B4%D0%BF%D0%BE%D0%BB%D0%BA%D0%BE%D0%B2%D0%BD%D0%B8%D0%BA')
    but_7 = InlineKeyboardButton('Полковник', url='https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%BB%D0%BA%D0%BE%D0%B2%D0%BD%D0%B8%D0%BA')
    keyboard_inline4.add(but_1, but_2, but_3, but_4, but_5, but_6, but_7)
    return keyboard_inline4


def get_keyboard_inline5():
    keyboard_inline5 = InlineKeyboardMarkup(row_width=2)
    button_1 = InlineKeyboardButton('Генерал-майор', url='https://ru.wikipedia.org/wiki/%D0%93%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D0%BB-%D0%BC%D0%B0%D0%B9%D0%BE%D1%80')
    button_2 = InlineKeyboardButton('Генерал-лейтенант', url='https://ru.wikipedia.org/wiki/%D0%93%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D0%BB-%D0%BB%D0%B5%D0%B9%D1%82%D0%B5%D0%BD%D0%B0%D0%BD%D1%82')
    button_3 = InlineKeyboardButton('Генерал-полколвник', url='https://ru.wikipedia.org/wiki/%D0%93%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D0%BB-%D0%BF%D0%BE%D0%BB%D0%BA%D0%BE%D0%B2%D0%BD%D0%B8%D0%BA')
    button_4 = InlineKeyboardButton('Генерал-армии', url='https://ru.wikipedia.org/wiki/%D0%93%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D0%BB_%D0%B0%D1%80%D0%BC%D0%B8%D0%B8_(%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F)')
    button_5 = InlineKeyboardButton('Маршал', url='https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D1%80%D1%88%D0%B0%D0%BB')
    keyboard_inline5.add(button_1, button_2, button_3, button_4, button_5)
    return keyboard_inline5




