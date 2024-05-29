from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_keyboard_inline():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline = InlineKeyboardButton('Посмотреть', url='https://travel.mts.ru/hotels/rossiya/moskva/etalon?utm_source=cvm_context_stream_tr&utm_medium=yandex_cpc&utm_campaign=stream_mtstravel_rus_hotel_dsa-feed_msk_search%7C99942866&utm_content=adset_id%3D5324905181%7Cnid%3Dnone%7Cdevice_type%3Ddesktop%7Crid%3D4912272&yclid=12748377160180826111&utm_referrer=https%3A%2F%2Fyandex.ru%2F&checkin=2024-05-30&checkout=2024-05-31&adults=2&children=0&location=cce1a1e0-9acc-4d1d-b778-1c2970845d63')
    but_inline2 = InlineKeyboardButton('Посмотреть', url='https://www.pentamoscow.ru/')
    keyboard_inline.add(but_inline, but_inline2)
    return keyboard_inline

def get_keyboard_inline2():
    keyboard_inline2 = InlineKeyboardMarkup(row_width=2)
    but_inline3 = InlineKeyboardButton('Посмотреть', url='https://www.kupibilet.ru/')
    but_inline4 = InlineKeyboardButton('Посмотреть', url='https://fstravel.com/avia/?utm_source=yandex&utm_medium=cpc&utm_campaign=Moskva_%7C_Poisk_%7C_Aviabileti_%7C_Obshie_%7C_FS&utm_content=16120523295&utm_term=ST%3Asearch%7CS%3Anone%7CAP%3Ano%7CPT%3Apremium%7CP%3A4%7CDT%3Adesktop%7CRI%3A98591%7CRN%3A%D0%9B%D0%B5%D0%BD%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B9%20%D1%80%D0%B0%D0%B9%D0%BE%D0%BD%7CCI%3A110371913%7CGI%3A5443823162%7CPI%3A51470773623%7CAI%3A16120523295%7CKW%3A%D1%86%D0%B5%D0%BD%D0%B0%20%D0%B1%D0%B8%D0%BB%D0%B5%D1%82%20%D0%BD%D0%B0%20%D1%81%D0%B0%D0%BC%D0%BE%D0%BB%D0%B5%D1%82&calltouch_tm=yd_c%3A110371913_gb%3A5443823162_ad%3A16120523295_ph%3A51470773623_st%3Asearch_pt%3Apremium_p%3A4_s%3Anone_dt%3Adesktop_reg%3A98591_ret%3A51470773623_apt%3Anone&yclid=2779019152038035455')
    keyboard_inline2.add(but_inline3, but_inline4)
    return keyboard_inline2

