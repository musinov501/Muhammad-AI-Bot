import asyncio
import logging
from aiogram import Bot , Dispatcher , types
from aiogram.filters import Command
from aiogram.methods import DeleteWebhook
from aiogram.types import Message
from openai import OpenAI


TOKEN = '7826322147:AAGA4oeSTNGmOhputuADfIpp0iEQ96WKLq0'

logging.basicConfig(level = logging.INFO)
bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(Command("Start"))
async def cmd_start(message: types.Message):
    await message.answer('Hello, I am a bot generated to serve like Chat GPT, so you may ask your questions!!!😊', parse_mode = 'HTML')
 
 
@dp.message(lambda message: message.text)
async def filter_messages(message: Message):
  client = OpenAI(
  base_url="https://api.langdock.com/openai/eu/v1",
  api_key="sk-vbuwofP9s-7mwmzXRiGtr9AeTqDwDnas4uKaZfhpJTMw1IiNikDx_uATeqrSmqyfDZT5zrO042r-AUbstGPA2A"
)

  completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "user", "content": message.text}
  ]
)
  
  text = completion.choices[0].message.content
  
  await message.answer(text , parse_mode = 'Markdown')
  
  
async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    asyncio.run(main())