import telebot
import random

from telebot import types

bot = telebot.TeleBot('1122101091:AAFmyzjDxCdcL02oVcm6mPIOnbV62m_1gCA')

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open ('C:/Users/Daniil/Desktop/Учёба/телеграм бот/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    #keyboard
    item1 = types.KeyboardButton("🍺Пиво")
    item2 = types.KeyboardButton("🍷Вино")
    item3 = types.KeyboardButton("Ром")
    item4 = types.KeyboardButton("Коньяк")
    item5 = types.KeyboardButton("Виски")
    markup = types.ReplyKeyboardMarkup().row(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный, чтобы облегчить твой выбор бухлишка на тусу.".format(message.from_user, bot.get_me()),
    parse_mode ='html', reply_markup=markup)
vine = ['Может стоит попробовать красное сухое вино из ЮАР - "BARISTA PINOTAGE"?',
        'Я думаю стоит попробовать белое сухое итальянское вино - "PRESTIGE CaMaiol"',
        'Отлично подойдёт вино красивого рубинового цвета, созданное в Италии - "EPICURO Primitivo di Manduria"',
        'Хорошим выбором будет вино с насыщенным вкусом винограда - "Живописная Гудаута"']

pivo = ['"Essa Lime & Mint"?',
        '"Essa Pineapple & Grapefruit"',
        '"Essa Orange & Cherry"',
        '"Garage Hard Lemon"',
        '"Garage Hard Lemon Tea"',
        '"Garage Hard Ginger"',
        '"Garage Hard Lingonberry drink"',
        '"Garage Hard Black Cherry Drink"',
        '"Dr.Diesel Wild Mix"',
        '"Dr.Diesel Hot Mix"',
        '"Dr.Diesel Cool Mix"',
        '"Bud"',
        '"Bud Light"',
        '"Amstel"',
        '"Heineken"',
        '"Три медведя"',
        '"Krušovice"',
        '"Carlsberg"']

cognaс = ['"Коньяк армянский Старый КС Шалахо 10 лет"',
          '"Коньяк Кизляр 3 года"',
          '"Российский коньяк Шустов не менее 5 лет"',
          '"Коньяк Квинт выдержанный 14 лет"',
          '"Коньяк А.де Фуссиньи ХО п/к"',
          '"Коньяк Квинт выдержанный 14 лет"',
          '"Арарат Отборный 7 лет"',
          '"Лезгинка"']

rum = ['"Captain Morgan"',
        '"Capitan Silver"',
        '"Steel Drum"',
        '"Matusalem Anejo"',
        '"Matusalem Salera"',
        '"Brugal Añejo"',]

whiskey = ['"Grant’s tripple wood"',
           '"Bell’s"',
           '"Tullamore Dew"',
           '"White Horse"',
           '"Clan MacGregor"',
           '"Jack Daniel’s"',
           '"Jim Beam Apple"',
           '"Jim Beam Honey"',
           '"Jim Beam Bourbon"',
           '"William Lawson’s"']

choiser = ['Может стоит попробовать - ',
           'Я думаю стоит попробовать - ',
           'Отлично подойдёт - ',
           'Хорошим выбором будет - ',
           'Как насчёт - ']

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.chat.type == 'private':
        if message.text == '🍺Пиво':
            bot.send_message(message.chat.id, str(random.choice(choiser)+random.choice(pivo)))
        elif message.text == '🍷Вино':
            bot.send_message(message.chat.id, str(random.choice(vine)))
        elif message.text == 'Коньяк':
            bot.send_message(message.chat.id, str(random.choice(choiser) + random.choice(cognaс)))
        elif message.text == 'Ром':
            bot.send_message(message.chat.id, str(random.choice(choiser) + random.choice(rum)))
        elif message.text == 'Виски':
            bot.send_message(message.chat.id, str(random.choice(choiser) + random.choice(whiskey)))
        else:
            bot.send_message(message.chat.id, 'Я не знаю что на это ответить 😥')


bot.polling(none_stop=True)

bot.run("1122101091:AAFmyzjDxCdcL02oVcm6mPIOnbV62m_1gCA")
