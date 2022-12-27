import requests
from bs4 import BeautifulSoup
from random import choice
import telebot

refers = {'rpg' : 'https://stopgame.ru/games/rpg/best', 'рпг' : 'https://stopgame.ru/games/rpg/best', 'action' : 'https://stopgame.ru/games/action/best', 'экшн' : 'https://stopgame.ru/games/action/best', 'adventure' : 'https://stopgame.ru/games/adventure/best', 'приключение' : 'https://stopgame.ru/games/adventure/best', 'arcade' : 'https://stopgame.ru/games/arcade/best', 'аркада' : 'https://stopgame.ru/games/arcade/best', 'fighting' : 'https://stopgame.ru/games/fighting/best', 'файтинг' : 'https://stopgame.ru/games/fighting/best', 'mmo' : 'https://stopgame.ru/games/massively_multiplayer/best', 'ммо' : 'https://stopgame.ru/games/massively_multiplayer/best', 'online' : 'https://stopgame.ru/games/online/best', 'онлайн' : 'https://stopgame.ru/games/online/best', 'racing' : 'https://stopgame.ru/games/racing/best', 'гонки' : 'https://stopgame.ru/games/racing/best', 'simulator' : 'https://stopgame.ru/games/simulator/best', 'симулятор' : 'https://stopgame.ru/games/simulator/best', 'sport' : 'https://stopgame.ru/games/sport/best', 'спорт' : 'https://stopgame.ru/games/sport/best', 'strategy' : 'https://stopgame.ru/games/strategy/best', 'стратегия' : 'https://stopgame.ru/games/strategy/best'}

token = "5921000643:AAF2KGwaKXmGv2kVi3ENxRSvMJ0Z9g5cduM"
bot = telebot.TeleBot(token)

@bot.message_handler(commands = ["start"])
def start(message):
    welcome = "Выберите жанр, и бот подберёт вам игру"
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
    b1 = telebot.types.KeyboardButton("рпг")
    b2 = telebot.types.KeyboardButton("экшн")
    b3 = telebot.types.KeyboardButton("приключение")
    b4 = telebot.types.KeyboardButton("аркада")
    b5 = telebot.types.KeyboardButton("файтинг")
    b6 = telebot.types.KeyboardButton("ммо")
    b7 = telebot.types.KeyboardButton("онлайн")
    b8 = telebot.types.KeyboardButton("гонки")
    b9 = telebot.types.KeyboardButton("симулятор")
    b10 = telebot.types.KeyboardButton("спорт")
    b11 = telebot.types.KeyboardButton("стратегия")
    keyboard.add(b5, b2, b3, b4, b10, b6, b7, b8, b9, b1, b11)
    bot.send_message(message.from_user.id, welcome, reply_markup = keyboard)

@bot.message_handler(commands = ["help"])
def help(message):
    info = "Просто введите один из предложенных жанров на русском или английском, а бот выдаст вам случайную игру этого жанра и ссылку на игру"
    bot.send_message(message.from_user.id, info)

@bot.message_handler(commands = ["genres"])
def genre(message):
    info = "Доступные жанры: rpg, action, adventure, arcade, fighting, mmo, online, racing, simulator, sport, strategy"
    bot.send_message(message.from_user.id, info)

@bot.message_handler(commands = ["contact"])
def contacts(message):
    contact = "Связаться с разработчиком бота: @Vsego47"
    bot.send_message(message.from_user.id, contact)

@bot.message_handler(content_types = ["text"])
def game(message):
    response = requests.get(refers[message.text.lower()])
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    games = html.find_all("a", class_ = "_card_67304_1")
    game = choice(games)
    name = game["title"]
    link = "https://stopgame.ru/" + game["href"]
    print(name + "\n" + link)
    x = name + "\n" + link
    bot.send_message(message.from_user.id, x)

bot.polling(none_stop=True, interval=0)