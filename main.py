from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.keyboards import get_keyboard_1, get_keyboard_2
from keyboard.key_inline import get_keyboard_inline, get_keyboard_inline2, get_keyboard_inline3, get_keyboard_inline4, get_keyboard_inline5

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description= 'Команда для того, чтобы запустить бота'),
        types.BotCommand(command='/low_ranks', description='Для того чтобы узнать какие есть низшие звания'),
        types.BotCommand(command='/middle_ranks', description='Для того чтобы узнать какие есть средние звания'),
        types.BotCommand(command='/highest_ranks', description='Для того чтобы узнать какие есть высшие звания')
        ]
    await bot.set_my_commands(commands)



@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply( 'Привет, я бот ,который поможет узнать какие есть звания в армии и военных боевых техник.')





@dp.message_handler(lambda message: message.text == 'Отправь фото всех званий')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://i.5pages.net/files/21b/21bb5f13c32a87ddc36027fe5ebd473f.jpg', caption= 'Вот ваши звания ', reply_markup= get_keyboard_inline())

@dp.message_handler(lambda message: message.text == 'Перейти на 2 клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут вы можете попросить ссылки на описание военных техник', reply_markup= get_keyboard_2())


@dp.message_handler(lambda message: message.text == 'Отправь военную технику')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://flomaster.top/uploads/posts/2022-12/1672504933_flomaster-club-p-oboronnaya-illyustratsiya-vkontakte-23.jpg', caption= 'Вот вам ссылки на описание военной техники', reply_markup= get_keyboard_inline2())


@dp.message_handler(lambda message: message.text == 'Перейти на 1 клавиатуру')
async def button_4_click(message: types.Message):
    await message.answer('Тут ты можете попросить узнать описание, какие есть звания в армии', reply_markup= get_keyboard_1())




@dp.message_handler(commands= 'low_ranks')
async def low_ranks(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://museum-kam.ru/800/600/https/pp.userapi.com/c845017/v845017679/7f50/zLeFspDZyi8.jpg', caption='Низшые звания', reply_markup=get_keyboard_inline3())

@dp.message_handler(commands= 'middle_ranks')
async def middle_ranks(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://museum-kam.ru/800/600/https/pp.userapi.com/c845017/v845017679/7f50/zLeFspDZyi8.jpg', caption='Средние звания', reply_markup=get_keyboard_inline4())

@dp.message_handler(commands= 'highest_ranks')
async def highest_ranks(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://museum-kam.ru/800/600/https/pp.userapi.com/c845017/v845017679/7f50/zLeFspDZyi8.jpg', caption='Высшие звания', reply_markup=get_keyboard_inline5())






async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)
