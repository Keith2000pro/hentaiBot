import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import os
from img import token
logging.basicConfig(level=logging.INFO)
bot = Bot(token=token[0], parse_mode=types.ParseMode.HTML)
dp= Dispatcher(bot)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["спасибо, хорошо", "new menu"]
    keyboard.add(*buttons)
    await message.answer("привет дорогой хозяин, как провел день❤️😘🤗?", reply_markup=keyboard)
#ответы

@dp.message_handler(Text(equals="спасибо, хорошо"))
async def thanks(message: types.Message):
	await message.reply('😘')

    
@dp.message_handler(lambda message: message.text == "new menu")
async def without_puree(message: types.Message):
     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
     buttons = ["поцеловать", "выебать"]
     keyboard.add(*buttons)
     await message.answer("что выберете хозяин?", reply_markup=keyboard)

@dp.message_handler(Text(equals="выебать"))
async def fuck(message: types.Message):
		await message.reply('только пожалуйста, не сильно 🥺')		
@dp.message_handler(Text(equals="поцеловать"))
async def kiss(message: types.Message):
		await message.reply('kiss')
		if message.from_user.id ==5085467188:
						await message.reply('нахуй иди предатель')
								
												
if __name__=="__main__":
	executor.start_polling(dp, skip_updates=True)
