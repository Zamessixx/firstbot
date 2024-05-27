from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from  keyboard.keyboards import get_keyboard_1, get_keyboard_2
from  keyboard.key_inline import  get_keyboard_inline, get_keyboard_inline2


bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)



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
    await message.answer('Привет, я твой первый Эхо бот', reply_markup= get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Отправь фото игры')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://shared.cloudflare.steamstatic.com/store_item_assets/steam/apps/238320/capsule_616x353.jpg?t=1666817106', caption= 'Вот тебе игра', reply_markup= get_keyboard_inline())

@dp.message_handler(lambda message: message.text == 'Перейти на 2 клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить отправить мем', reply_markup= get_keyboard_2())


@dp.message_handler(lambda message: message.text == 'Отправь мем')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://thumb.tildacdn.com/tild6465-6132-4937-b964-336163313261/-/resize/824x/-/format/webp/mem-2-1024x683.jpg', caption= 'Вот тебе мем', reply_markup= get_keyboard_inline2())


@dp.message_handler(lambda message: message.text == 'Перейти на 1 клавиатуру')
async def button_4_click(message: types.Message):
    await message.answer('Тут ты можешь попросить увидеть игру', reply_markup= get_keyboard_2())




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
