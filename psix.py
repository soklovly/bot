import os
import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message

API_TOKEN = 'токен'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("привет, я тебя промотивирую")

@dp.message_handler(commands=['мотивация'])
async def send_motivation(message: types.Message):
    images_folder = 'motivation'
    images = [f for f in os.listdir(images_folder) if os.path.isfile(os.path.join(images_folder, f))]
    if images:
        image_path = os.path.join(images_folder, random.choice(images))
        with open(image_path, 'rb') as photo:
            await message.answer_photo(photo)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(dp.start_polling())
    loop.run_forever()
