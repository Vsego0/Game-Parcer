import requests
from bs4 import BeautifulSoup
from random import choice
import telebot

def rpg():
    response = requests.get('https://stopgame.ru/games/rpg/best')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    games = html.find_all("a", class_ = "_card_67304_1")
    game = choice(games)
    name = game["title"]
    link = "https://stopgame.ru/" + game["href"]
    x = name + "\n" + link
    return x

def action():
    response = requests.get('https://stopgame.ru/games/action/best')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    games = html.find_all("a", class_ = "_card_67304_1")
    game = choice(games)
    name = game["title"]
    link = "https://stopgame.ru/" + game["href"]
    print(name + "\n" + link)
    x = name + "\n" + link
    return x

def adventure():
    response = requests.get('https://stopgame.ru/games/adventure/best')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    games = html.find_all("a", class_ = "_card_67304_1")
    game = choice(games)
    name = game["title"]
    link = "https://stopgame.ru/" + game["href"]
    print(name + "\n" + link)
    x = name + "\n" + link
    return x

def arcade():
    response = requests.get('https://stopgame.ru/games/arcade/best')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    games = html.find_all("a", class_ = "_card_67304_1")
    game = choice(games)
    name = game["title"]
    link = "https://stopgame.ru/" + game["href"]
    print(name + "\n" + link)
    x = name + "\n" + link
    return x

def fighting():
    response = requests.get('https://stopgame.ru/games/fighting/best')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    games = html.find_all("a", class_ = "_card_67304_1")
    game = choice(games)
    name = game["title"]
    link = "https://stopgame.ru/" + game["href"]
    print(name + "\n" + link)
    x = name + "\n" + link
    return x

def mmo():
    response = requests.get('https://stopgame.ru/games/massively_multiplayer/best')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    games = html.find_all("a", class_ = "_card_67304_1")
    game = choice(games)
    name = game["title"]
    link = "https://stopgame.ru/" + game["href"]
    print(name + "\n" + link)
    x = name + "\n" + link
    return x

def online():
    response = requests.get('https://stopgame.ru/games/online/best')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    games = html.find_all("a", class_ = "_card_67304_1")
    game = choice(games)
    name = game["title"]
    link = "https://stopgame.ru/" + game["href"]
    print(name + "\n" + link)
    x = name + "\n" + link
    return x

def racing():
    response = requests.get('https://stopgame.ru/games/racing/best')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    games = html.find_all("a", class_ = "_card_67304_1")
    game = choice(games)
    name = game["title"]
    link = "https://stopgame.ru/" + game["href"]
    print(name + "\n" + link)
    x = name + "\n" + link
    return x

def simulator():
    response = requests.get('https://stopgame.ru/games/simulator/best')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    games = html.find_all("a", class_ = "_card_67304_1")
    game = choice(games)
    name = game["title"]
    link = "https://stopgame.ru/" + game["href"]
    print(name + "\n" + link)
    x = name + "\n" + link
    return x

def sport():
    response = requests.get('https://stopgame.ru/games/sport/best')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    games = html.find_all("a", class_ = "_card_67304_1")
    game = choice(games)
    name = game["title"]
    link = "https://stopgame.ru/" + game["href"]
    print(name + "\n" + link)
    x = name + "\n" + link
    return x

def strategy():
    response = requests.get('https://stopgame.ru/games/strategy/best')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    games = html.find_all("a", class_ = "_card_67304_1")
    game = choice(games)
    name = game["title"]
    link = "https://stopgame.ru/" + game["href"]
    print(name + "\n" + link)
    x = name + "\n" + link
    return x

token = "5921000643:AAF2KGwaKXmGv2kVi3ENxRSvMJ0Z9g5cduM"
bot = telebot.TeleBot(token)

@bot.message_handler(commands = ["start"])
def start(message):
    welcome = "???????????????? ????????, ?? ?????? ???????????????? ?????? ????????"
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
    b1 = telebot.types.KeyboardButton("??????")
    b2 = telebot.types.KeyboardButton("????????")
    b3 = telebot.types.KeyboardButton("??????????????????????")
    b4 = telebot.types.KeyboardButton("????????????")
    b5 = telebot.types.KeyboardButton("??????????????")
    b6 = telebot.types.KeyboardButton("??????")
    b7 = telebot.types.KeyboardButton("????????????")
    b8 = telebot.types.KeyboardButton("??????????")
    b9 = telebot.types.KeyboardButton("??????????????????")
    b10 = telebot.types.KeyboardButton("??????????")
    b11 = telebot.types.KeyboardButton("??????????????????")
    keyboard.add(b5, b2, b3, b4, b10, b6, b7, b8, b9, b1, b11)
    bot.send_message(message.from_user.id, welcome, reply_markup = keyboard)

@bot.message_handler(commands = ["help"])
def help(message):
    info = "???????????? ?????????????? ???????? ???? ???????????????????????? ???????????? ???? ?????????????? ?????? ????????????????????, ?? ?????? ???????????? ?????? ?????????????????? ???????? ?????????? ?????????? ?? ???????????? ???? ????????"
    bot.send_message(message.from_user.id, info)

@bot.message_handler(commands = ["genres"])
def genre(message):
    info = "?????????????????? ??????????: rpg, action, adventure, arcade, fighting, mmo, online, racing, simulator, sport, strategy"
    bot.send_message(message.from_user.id, info)

@bot.message_handler(commands = ["contact"])
def contacts(message):
    contact = "?????????????????? ?? ?????????????????????????? ????????: @Vsego47"
    bot.send_message(message.from_user.id, contact)

@bot.message_handler(content_types = ["text"])
def send_game(message):
    if message.text.lower() == "rpg" or message.text.lower() == "??????":
        bot.send_message(message.from_user.id, rpg())
    elif message.text.lower() == "action" or message.text.lower() == "????????":
        bot.send_message(message.from_user.id, action())
    elif message.text.lower() == "adventure" or message.text.lower() == "??????????????????????":
        bot.send_message(message.from_user.id, adventure())
    elif message.text.lower() == "arcade" or message.text.lower() == "????????????":
        bot.send_message(message.from_user.id, arcade())
    elif message.text.lower() == "fighting" or message.text.lower() == "??????????????":
        bot.send_message(message.from_user.id, fighting())
    elif message.text.lower() == "mmo" or message.text.lower() == "??????":
        bot.send_message(message.from_user.id, mmo())
    elif message.text.lower() == "online" or message.text.lower() == "????????????":
        bot.send_message(message.from_user.id, online())
    elif message.text.lower() == "racing" or message.text.lower() == "??????????":
        bot.send_message(message.from_user.id, racing())
    elif message.text.lower() == "simulator" or message.text.lower() == "??????????????????":
        bot.send_message(message.from_user.id, simulator())
    elif message.text.lower() == "sport" or message.text.lower() == "??????????":
        bot.send_message(message.from_user.id, sport())
    elif message.text.lower() == "strategy" or message.text.lower() == "??????????????????":
        bot.send_message(message.from_user.id, strategy())

bot.polling(none_stop=True, interval=0)