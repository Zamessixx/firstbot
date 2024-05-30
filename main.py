from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.keyboards import get_keyboard_1, get_keyboard_2
from keyboard.key_inline import get_keyboard_inline, get_keyboard_inline2
from database.database import initialize_db, add_user, get_user

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

initialize_db()

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description= 'Команда для того, чтобы запустить бота'),
        types.BotCommand(command='/help', description='Команда для того, узнать, с чем может помочь наш бот'),
        types.BotCommand(command='/comand3', description='Для того чтобы узнать как работает третья команда'),
        types.BotCommand(command='/comand4', description='Для того чтобы узнать как работает четвёртая команда'),
        types.BotCommand(command='/comand5', description='Для того чтобы узнать как работает пятая команда')
        ]
    await bot.set_my_commands(commands)



@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    user = get_user(message.from_user.id)
    if user is None:
        add_user(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
        await message.answer('Привет, я твой первый Эхо бот', reply_markup=get_keyboard_1())
    else:
        await message.answer('Привет, я твой первый Эхо бот', reply_markup=get_keyboard_1())



@dp.message_handler(lambda message: message.text == 'Отправь фото отеля')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://avatars.dzeninfra.ru/get-zen_doc/2404797/pub_5ec05dabc419064bb24dcdcb_5ec07408d54088764522e780/scale_1200', caption= 'Вот ваше фото и ссылки на аренду номера отелей ', reply_markup= get_keyboard_inline())

@dp.message_handler(lambda message: message.text == 'Перейти на 2 клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут вы можете попросить ссылки на покупку билетов на самолёт и поезд', reply_markup= get_keyboard_2())


@dp.message_handler(lambda message: message.text == 'Отправь картинку самолёта и поезда')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://avatars.dzeninfra.ru/get-zen_doc/5231677/pub_63df6d803fede37a27a6d867_63df728bc190412358747cd3/scale_1200', caption= 'Вот вам ссылки на покупку билетов', reply_markup= get_keyboard_inline2())


@dp.message_handler(lambda message: message.text == 'Перейти на 1 клавиатуру')
async def button_4_click(message: types.Message):
    await message.answer('Тут ты можешь попросить увидеть ссылки ня снятие номера в отеле', reply_markup= get_keyboard_1())




@dp.message_handler(commands= 'help')
async def help(message: types.Message):
    await message.reply('Я помогу тебе')

@dp.message_handler(commands= 'comand3')
async def comand3(message: types.Message):
    await message.reply('команда 3')

@dp.message_handler(commands= 'comand4')
async def comand4(message: types.Message):
    await message.reply('команда 4')

@dp.message_handler(commands= 'comand5')
async def comand5(message: types.Message):
    await message.reply('команда 5')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)



async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)
