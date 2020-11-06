import telebot
import requests
import json
from telebot import types

bot = telebot.TeleBot('1442405622:AAHtSMV9F4Ddk0w9YGAEJg_sSXswZjH96KY')

i = 0
k = 0
j = 0
g = 0

name = []
vote = []
over = []
reld = []

name2 = []
vote2 = []
over2 = []
reld2 = []

name3 = []
vote3 = []
over3 = []
reld3 = []

name4 = []
vote4 = []
over4 = []
reld4 = []


def ratemoji(rate):
    if rate >= 7.0 and rate <= 10.0:
        return '🔥'
    if rate >= 5.0 and rate < 7.0:
        return '😊'
    if rate < 5.0 and rate >= 3.0:
        return '😒'
    else:
        return '💩'


def globall():
    global name
    global name2
    global vote
    global vote2
    global over
    global over2
    global reld
    global reld2
    global name3
    global vote3
    global over3
    global reld3


def parse():
    globall()

    api_key = {'api_key': 'c714df39f180cce5586ae9609569bb08'}

    ppl = requests.get('https://api.themoviedb.org/3/movie/upcoming',
                       params=api_key)
    response = ppl.text
    dict = json.loads(response)
    res = dict['results']

    for i in range(len(res)):
        raw = res[i]
        nm = raw['original_title']
        name.append(nm)
        vt = raw['vote_average']
        vote.append(vt)
        ov = raw['overview']
        over.append(ov)
        rd = raw['release_date']
        reld.append(rd)

    np = requests.get('https://api.themoviedb.org/3/movie/now_playing', params=api_key)
    response2 = np.text
    dict2 = json.loads(response2)
    res2 = dict2['results']

    for k in range(len(res2)):
        raw = res2[k]
        nm2 = raw['original_title']
        name2.append(nm2)
        vt2 = raw['vote_average']
        vote2.append(vt2)
        ov2 = raw['overview']
        over2.append(ov2)
        rd2 = raw['release_date']
        reld2.append(rd2)

    tr = requests.get('https://api.themoviedb.org/3/movie/top_rated', params=api_key)
    response3 = tr.text
    dict3 = json.loads(response3)
    res3 = dict3['results']

    for j in range(len(res3)):
        raw = res3[j]
        nm3 = raw['original_title']
        name3.append(nm3)
        vt3 = raw['vote_average']
        vote3.append(vt3)
        ov3 = raw['overview']
        over3.append(ov3)
        rd3 = raw['release_date']
        reld3.append(rd3)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(True)
    keyboard.row('Upcoming Movies')
    keyboard.row('Now Playing Movies')
    keyboard.row('Top Rated Movies')
    keyboard.row('About Me')
    bot.send_message(message.chat.id, "Hi! Have nothing to watch?! I will help you! Choose the category you want",
                     reply_markup=keyboard)


@bot.message_handler(commands=['quit'])
def goodbye(message):
    bot.send_message(message.chat.id, 'I hope I could help you) Bye!')


@bot.message_handler(content_types=['text'])
def lists(message):
    global i
    global k
    global j
    parse()
    if message.text.lower() == 'upcoming movies':
        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row('Get UM')
        keyboard.row('Back')
        bot.send_message(message.chat.id, 'You have chosen UPCOMING MOVIES. Click GET UM',
                         reply_markup=keyboard)
    elif message.text.lower() == 'back':
        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row('Upcoming Movies')
        keyboard.row('Now Playing Movies')
        keyboard.row('Top Rated Movies')
        keyboard.row('About Me')
        bot.send_message(message.chat.id, 'Choose the category you want!',
                         reply_markup=keyboard)
    elif message.text.lower() == 'now playing movies':
        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row('Get NPM')
        keyboard.row('Back')
        bot.send_message(message.chat.id, 'You have chosen NOW PLAYING MOVIES. Click GET NPM',
                         reply_markup=keyboard)
    elif message.text.lower() == 'top rated movies':
        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row('Get TRM')
        keyboard.row('Back')
        bot.send_message(message.chat.id, 'You have chosen TOP RATED MOVIES. Click GET NPM',
                         reply_markup=keyboard)
    elif message.text.lower() == 'get um':
        if i <= 19:
            bot.send_message(message.chat.id, (f'Popular Movies: \n'
                                               f'Title: {name[i]}\n'
                                               f'Rate: {vote[i]} {ratemoji(float(vote[i]))}\n'
                                               f'Release date: {reld[i]}\n'
                                               f'Plot twist: {over[i]}'))
            i += 1
        else:
            bot.send_message(message.chat.id, "I have nothing else(")
    elif message.text.lower() == 'get npm':
        if k <= 19:
            bot.send_message(message.chat.id, (f'Now Playing Movies: \n'
                                               f'Title: {name2[k]}\n'
                                               f'Rate: {vote2[k]} {ratemoji(float(vote2[k]))}\n'
                                               f'Release date: {reld2[k]}\n'
                                               f'Plot twist: {over2[k]}'))
            k += 1
    elif message.text.lower() == 'get trm':
        if j <= 19:
            bot.send_message(message.chat.id, (f'Top Rated Movies: \n'
                                               f'Title: {name3[j]}\n'
                                               f'Rate: {vote3[j]} {ratemoji(float(vote3[j]))}\n'
                                               f'Release date: {reld3[j]}\n'
                                               f'Plot twist: {over3[j]}'))
            j += 1
    elif message.text.lower() == 'about me':
        bot.send_message(message.chat.id, f'I am a TelegramBot, created by freshman from AIU COM20-A.\n'
                                          f'I will help you to find a movie for your weekends)\n'
                                          f'All resources been taken from The Movie Database(TMDb)\n'
                                          f'If you want to re-view movie lists - text /start\n'
                                          f'If you want to quit - text /quit')
    else:
        bot.send_message(message.chat.id, "I DO NOT UNDERSTAND YOU! Please click on the button")


bot.polling(none_stop=True, interval=0)
