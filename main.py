from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command= '/start', description= 'Команда для того, чтобы запустить бота'),
        types.BotCommand(command='/help', description='Команда для того, узнать, с чем может помочь наш бот'),
        types.BotCommand(command='/comand3', description='Для того чтобы узнать как работает третья команда'),
        types.BotCommand(command='/comand4', description='Для того чтобы узнать как работает четвёртая команда'),
        types.BotCommand(command='/comand5', description='Для того чтобы узнать как работает пятая команда')
        ]
    await bot.set_my_commands(commands)



@dp.message_handler(commands= 'start')
async  def start(message: types.Message):
    await message.answer('Привет, я твой первый Эхо бот')



@dp.message_handler(commands= 'help')
async  def help(message: types.Message):
    await message.reply('Я помогу тебе')

@dp.message_handler(commands= 'comand3')
async  def comand3(message: types.Message):
    await message.reply('команда 3')

@dp.message_handler(commands= 'comand4')
async  def comand4(message: types.Message):
    await message.reply('команда 4')

@dp.message_handler(commands= 'comand5')
async  def comand5(message: types.Message):
    await message.reply('команда 5')


@dp.message_handler()
async  def echo(message: types.Message):
    await  message.answer(message.text)



async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)
