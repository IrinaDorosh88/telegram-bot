import telebot
import requests
import json

bot=telebot.TeleBot('6082877163:AAFFPhb8if8HESXSUNESA4k8sLYEzLhiWx8')
API = "7addbd0bb61dcb9dbeeda40a2b4caf87"
#вивід тексту у чаті

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привіт, напиши назву міста')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        bot.reply_to(message, f'У цьому місті температура повітря {data["main"]["temp"]} С')
    else:
        bot.reply_to(message, f'Назва міста указана неправильно')
    

bot.polling(none_stop=True)
