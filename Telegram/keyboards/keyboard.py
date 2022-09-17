from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup

main_menu = InlineKeyboardMarkup(row_width=1)
btn1 = InlineKeyboardButton(text='Первый пункт меню', callback_data='1')
btn2 = InlineKeyboardButton(text='Второй пункт меню', callback_data='2')
main_menu.add(btn1, btn2)
