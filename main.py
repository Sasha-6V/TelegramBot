import telebot
from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from telebot import types
from bot_logic import gen_pass, game, dice
from config import TOKEN, URL
from ai_handler import ask_ai, log_to_json
bot = telebot.TeleBot(TOKEN)
help_text = """
/start и /hello - приветствие
/bye - прощание
/пароль - генерирует новый пароль
/чоч - ???
/монета - орел или решка
/хех - хе * число после команды
/код - код бота
/ai - спросить нейросеть
"""
reply = None
# URL = "https://github.com/Sasha-6V/TelegramBot"
BOT_NAME = bot.get_me().first_name

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f"Привет! Я {BOT_NAME}. Напиши что-нибудь!")

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
    bot.reply_to(message, f"На монете выпало: {ch}")

@bot.message_handler(commands=['кубик'])
def send_dice(message):
    dices = dice()
    bot.reply_to(message, f"🎲 На кубике выпало: {dices}")

@bot.message_handler(commands=['хех'])
def send_heh(message):
    try:
        count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
        count_heh = min(count_heh, 100)
    except ValueError:
        count_heh = 5
    bot.reply_to(message, "хе" * count_heh)

@bot.message_handler(commands=['код'])
def send_code_button(message):
    keyboard = InlineKeyboardMarkup()
    keyboard.row(InlineKeyboardButton('📂 Код бота', url=URL))
    bot.reply_to(message, "Нажмите на кнопку ниже, чтобы увидеть код бота", reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['ai'])
def ai_command(message):
    user_text = message.text.replace('/ai', '', 1).strip()
    if not user_text:
        bot.reply_to(message, "Напиши текст после команды.\n\nПример:\n/ai Привет, как дела?")
        return
    user_text = user_text[:1000]
    try:
        bot.send_chat_action(message.chat.id, "typing")
        reply = ask_ai(user_text)
        # print("AI:", reply)
        bot.reply_to(message, reply)
    except Exception as e:
        bot.reply_to(message, "⚠ Ошибка при обращении к ИИ.")
        print(e)
    if reply:
        log_to_json(
            message.from_user.id,
            user_text,
            reply
        )


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
