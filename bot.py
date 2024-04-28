import logging
from aiogram import Bot, Dispatcher, types, executor
from btn import *

API_TOKEN = '6542830780:AAGncQd5uUjqoswU5hVvWP1rcMEe_SbA0mQ'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    await message.answer("salom", reply_markup=kb)
    


@dp.message_handler(text="men zor")
async def text_message(message:types.Message):
    await message.answer("san zorsan🫡")



@dp.message_handler(text="men chiroyli❤️")
async def text_message(message:types.Message):
    await message.answer("kim chiroytli")




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)