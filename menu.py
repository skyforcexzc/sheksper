import settings
import telebot
import random
#import functions as func
from telebot import types


# Main menu
main_menu = types.InlineKeyboardMarkup(row_width=3)
main_menu.add(
    types.InlineKeyboardButton(text='🚬 Каталог', callback_data='catalog'),
    types.InlineKeyboardButton(text='👤 Профиль', callback_data='profile'),
    types.InlineKeyboardButton(text='ℹ️ Информация', callback_data='info'),
    types.InlineKeyboardButton(text='🛒 Мои покупки', callback_data='purchases'),
    types.InlineKeyboardButton(text='💲Пополнить баланс ', callback_data='popolnenie'),
)
main_menu.add(
    types.InlineKeyboardButton(text='🙋🏻‍♂️ Реферальная система', callback_data='referral_web'),
    types.InlineKeyboardButton(text='💸 Работа', callback_data='rabota')
)       

# Admin menu
admin_menu = types.InlineKeyboardMarkup(row_width=2)
admin_menu.add(types.InlineKeyboardButton(text='Управление городами', callback_data='catalog_control'))
admin_menu.add(types.InlineKeyboardButton(text='Управление товаром', callback_data='section_control'))
admin_menu.add(types.InlineKeyboardButton(text='Изменить баланс', callback_data='give_balance'))
admin_menu.add(types.InlineKeyboardButton(text='Рассылка', callback_data='admin_sending_messages'))
admin_menu.add(types.InlineKeyboardButton(text='Топ рефералов ', callback_data='admin_top_ref'))
admin_menu.add(types.InlineKeyboardButton(text='Найти пользователя', callback_data='find_user'))
admin_menu.add(
    types.InlineKeyboardButton(text='Информация', callback_data='admin_info'),
    types.InlineKeyboardButton(text='Выйти', callback_data='exit_admin_menu')
)

# Admin control
nazad = types.InlineKeyboardMarkup(row_width=1)
nazad.add(
    types.InlineKeyboardButton(text='Назад', callback_data='exit_to_menu')
)

# Admin control
admin_menu_control_catalog = types.InlineKeyboardMarkup(row_width=1)
admin_menu_control_catalog.add(
    types.InlineKeyboardButton(text='Добавить город', callback_data='add_section_to_catalog'),
    types.InlineKeyboardButton(text='Удалить город', callback_data='del_section_to_catalog'),
    types.InlineKeyboardButton(text='Назад', callback_data='back_to_admin_menu')
)

# Изменено: оставлена только банковская карта
popolnenie = types.InlineKeyboardMarkup(row_width=1)
popolnenie.add(
    types.InlineKeyboardButton(text='Банковская карта', callback_data='bank_card'),
    types.InlineKeyboardButton(text='Назад', callback_data='exit_to_menu')
)

# Admin control section
admin_menu_control_section = types.InlineKeyboardMarkup(row_width=1)
admin_menu_control_section.add(
    types.InlineKeyboardButton(text='Добавить товар в город', callback_data='add_product_to_section'),
    types.InlineKeyboardButton(text='Удалить товар из города', callback_data='del_product_to_section'),
    types.InlineKeyboardButton(text='Загрузить товар', callback_data='download_product'),
    types.InlineKeyboardButton(text='Назад', callback_data='back_to_admin_menu')
)

# Back to admin menu
back_to_admin_menu = types.InlineKeyboardMarkup(row_width=1)
back_to_admin_menu.add(
    types.InlineKeyboardButton(text='Вернуться в админ меню', callback_data='back_to_admin_menu')
)

btn_purchase = types.InlineKeyboardMarkup(row_width=2)
btn_purchase.add(
    types.InlineKeyboardButton(text='Купить', callback_data='buy'),
    types.InlineKeyboardButton(text='Выйти', callback_data='exit_to_menu')
)

btn_ok = types.InlineKeyboardMarkup(row_width=3)
btn_ok.add(
    types.InlineKeyboardButton(text='Понял', callback_data='btn_ok')
)

to_close = types.InlineKeyboardMarkup(row_width=3)
to_close.add(
    types.InlineKeyboardButton(text='Назад', callback_data='exit_to_menu')
)
goroda = telebot.types.ReplyKeyboardMarkup(True, True)
goroda.row('💠 Абакан')
goroda.row('💠 Арзамас')
goroda.row('💠 Артем')
goroda.row('💠 Астрахань')
goroda.row('💠 Балашиха')
goroda.row('💠 Батайск')
goroda.row('💠 Белгород')
goroda.row('💠 Брянск')
goroda.row('💠 Владивосток')
goroda.row('💠 Владимир')
goroda.row('💠 Волгоград')
goroda.row('💠 Домодедово')
goroda.row('💠 Евпатория')
goroda.row('💠 Екатеренбург')
goroda.row('💠 Ессентуки')
goroda.row('💠 Иваново')
goroda.row('💠 Ижевск')
goroda.row('💠 Иркутск')
goroda.row('💠 Казань')
goroda.row('💠 Калининград')
goroda.row('💠 Кемерово')
goroda.row('💠 Керчь')
goroda.row('💠 Киров')
goroda.row('💠 Краснодар')
goroda.row('💠 Красноярск')
goroda.row('💠 Курган')
goroda.row('💠 Курск')
goroda.row('💠 Липецк')
goroda.row('💠 Магадан')
goroda.row('💠 Магнитогорск')
goroda.row('💠 Москва')
goroda.row('💠 Муром')
goroda.row('💠 Мытищи')
goroda.row('💠 Нефтекамск')
goroda.row('💠 Нижний Новгород')
goroda.row('💠 Нижний Тагил')
goroda.row('💠 Новокузнецк')
goroda.row('💠 Новосибирск')
goroda.row('💠 Омск')
goroda.row('💠 Оренбург')
goroda.row('💠 Орёл')
goroda.row('💠 Пенза')
goroda.row('💠 Пермь')
goroda.row('💠 Пятигорск')
goroda.row('💠 Ростов-на-Дону')
goroda.row('💠 Рязань')
goroda.row('💠 Самара')
goroda.row('💠 Санкт-Петербург')
goroda.row('💠 Саратов')
goroda.row('💠 Сиферополь')
goroda.row('💠 Сочи')
goroda.row('💠 Ставрополь')
goroda.row('💠 Сургут')
goroda.row('💠 Таганрон')
goroda.row('💠 Тверь')
goroda.row('💠 Тольятти')
goroda.row('💠 Томск')
goroda.row('💠 Тула')
goroda.row('💠 Тюмень')
goroda.row('💠 Ульяновск')
goroda.row('💠 Уфа')
goroda.row('💠 Хабаровск')
goroda.row('💠 Химки')
goroda.row('💠 Чебоксары')
goroda.row('💠 Челябинск')
goroda.row('💠 Ялта')
goroda.row('💠 Ярославль')

interesno = telebot.types.ReplyKeyboardMarkup(True, True)
interesno.row('Заинтересовало!')
interesno.row('Вернуться в главное меню')

# Удалена функция replenish_balance