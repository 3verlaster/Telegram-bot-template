###########################################################
#                    TELEGRAM BOT TEMPLATE                #
#           this template using aiogram, not telebot!     #
#              thank you for using this template <3       #
#                 made in Ukraine by 3verlaster           #
#                          god bless                      #
#                                                         #
###########################################################
from aiogram import types, executor, Dispatcher, Bot
from aiogram.types import ReplyKeyboardMarkup
import random

#bot token
TOKEN = '5994631414:AAFDGHOy3UvD6fro7pJOT6Fb9NhbokEJ3tY'
bot = Bot(token=HERE YOUR TOKEN)
dp = Dispatcher(bot)

#register command /start
@dp.message_handler(commands=['start'])
async def begin(message: types.Message):
    await bot.send_message(message.chat.id, 'Привет! Этого бота создал @everlaster_official')
    await bot.send_message(message.chat.id, 'Посмотреть доступные кнопки - /buttons')

#register command /random_num (random number generation)
@dp.message_handler(commands=['random_num'])
async def random_num(message:types.Message):
    num = random.randint(0, 2)
    await bot.send_message(message.chat.id, str(num))

#reply on message 'poka and other'
@dp.message_handler(content_types=['text'])
async def begin(message: types.Message):
    if message.text.lower() == 'poka':
        await bot.send_message(message.chat.id, 'poka gun done')
    elif message.text.lower() == 'привет':
        await bot.send_message(message.chat.id, 'Приффки, зая <3')
    elif message.text.lower() == 'fdsy8953hswa':
        await bot.send_message(message.chat.id, 'Подрочи мне хуйца пж!! <3 @everlaster_official')

executor.start_polling(dp)
