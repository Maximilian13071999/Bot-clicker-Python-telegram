from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_kb = ReplyKeyboardMarkup()
start_kb.row(KeyboardButton('Баланс'), KeyboardButton('Фарм'), KeyboardButton('Нефть'))
start_kb.row(KeyboardButton('Магазин'), KeyboardButton('Топ'), KeyboardButton('Казино'))

casino_kb = ReplyKeyboardMarkup()
casino_button1 = KeyboardButton("Hard game")
casino_button2 = KeyboardButton("Light game")
casino_button2_1 = KeyboardButton("Basketball")
casino_button3 = KeyboardButton("Не назад, а куда?")
casino_kb.row(casino_button1, casino_button2 , casino_button2_1).row(casino_button3)

basket_g = ReplyKeyboardMarkup()
backet_button1 = KeyboardButton("Попадёт")
backet_button2 = KeyboardButton("Не попадёт")
backet_button3 = KeyboardButton("Назад")
basket_g.row(backet_button1 , backet_button2).row(backet_button3)

casino_l = ReplyKeyboardMarkup()
casino_buttonl1 = KeyboardButton("1 - 3")
casino_buttonl2 = KeyboardButton("4 - 6")
casino_buttonl3 = KeyboardButton("Назад")
casino_l.row(casino_buttonl1, casino_buttonl2).row(casino_buttonl3)

casino_h = ReplyKeyboardMarkup()
casino_buttonh1 = KeyboardButton("1")
casino_buttonh2 = KeyboardButton("2")
casino_buttonh3 = KeyboardButton("3")
casino_buttonh4 = KeyboardButton("4")
casino_buttonh5 = KeyboardButton("5")
casino_buttonh6 = KeyboardButton("6")
casino_buttonh7 = KeyboardButton("Назад")
casino_h.row(casino_buttonh1, casino_buttonh2 , casino_buttonh3 , casino_buttonh4 , casino_buttonh5 , casino_buttonh6).row(casino_buttonh7)

earn_kb = InlineKeyboardMarkup()
earn_kb.add(InlineKeyboardButton("Тык", callback_data="get"))

earn2_kb = InlineKeyboardMarkup()
earn2_kb.add(InlineKeyboardButton("Тык", callback_data="get2"))

shop_kb = ReplyKeyboardMarkup()
shop_button1 = KeyboardButton("Up level")
shop_button2 = KeyboardButton("Back")
shop_button3 = KeyboardButton("Buy Cristalls money")
shop_button4 = KeyboardButton("Buy Cristalls oil")
shop_kb.row(shop_button1 , shop_button2 , shop_button3 , shop_button4)
