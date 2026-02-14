import telebot
from telebot import TeleBot
from telebot.types import (
    WebAppInfo,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from bot_logic import gen_pass, game
from config import TOKEN
bot = telebot.TeleBot(TOKEN)
WEB_URL = "https://github.com/eternnoir/pyTelegramBotAPI/blob/master/examples/mini_app.py"

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f"Привет! Я {bot.get_me().first_name}. Напиши что-нибудь!")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['чоч'])
def send_ch(message):
    bot.reply_to(message, "Воу, мемасик!")

@bot.message_handler(commands=['пароль'])
def send_pass(message):
    password = gen_pass(10)
    bot.reply_to(message, f"Твой новый пароль: {password}")

@bot.message_handler(commands=['монета'])
def send_game(message):
    ch = game()
    bot.reply_to(message, f"Монета сказала: {ch}")

@bot.message_handler(commands=['хех'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "хе" * count_heh)

@bot.message_handler(commands=["код"])
def code(message):
    inline_keyboard_markup = InlineKeyboardMarkup()
    inline_keyboard_markup.row(InlineKeyboardButton('Код бота', web_app=WebAppInfo(WEB_URL)))
    bot.reply_to(message, "Нажмите на кнопку ниже, чтобы увидеть код бота", reply_markup=inline_keyboard_markup)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
