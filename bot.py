import telebot
import pyowm


bot = telebot.TeleBot('1255681490:AAFaTCHYuZOQA2teXDHiN7JVVNHjtsuxr4g')  # апи телеграмбота
owm = pyowm.OWM('6b89460e9aa402f788f427ec417cb2a8', language="RU")


@bot.message_handler(content_types=['text'])
def handle_message(message):

	observation = owm.weather_at_place(message.text)
	w = observation.get_weather()

	temp = w.get_temperature('celsius')['temp']

	ans = ('В городе ' + message.text + ' сейчас ' + w.detailed_status) + '\n'

	ans += ('Температура воздуха около: ' + str(temp) + '°') + '\n\n'

	if temp > 20:
		ans = ans + 'Тепло, можно в футболке'
	elif temp < 20:
		ans = ans + 'Достаточно прохладно, оденьтесь потеплее'
	elif temp < 10:
		ans = ans + 'Очень холодно, наденьте куртку'

	bot.send_message(message.chat.id, ans)


if __name__ == '__main__':
	bot.polling(none_stop=True)