from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from Telegram.keyboards.keyboard import main_menu

TOKEN = '5794163854:AAGoAe_aFL_-jQAelOH9rceL_5EmVh0NQj0'
bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def send_menu(message: types.Message):
    await bot.send_message(message.from_user.id, text='Выберите интересующий пункт меню:', reply_markup=main_menu)


executor.start_polling(dp)
