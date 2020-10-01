import telebot
import pyowm
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language here


bot = telebot.TeleBot('1255681490:AAFaTCHYuZOQA2teXDHiN7JVVNHjtsuxr4g')  # апи телеграмбота
owm = pyowm.OWM('6b89460e9aa402f788f427ec417cb2a8')  # апи с сайта погоды и перевод на русский


@bot.message_handler(content_types=['text'])
def handle_message(message):

	mgr = owm.weather_manager()
	observation = mgr.weather_at_place(message.text)
	w = observation.weather
	temp = w.temperature('celsius')['temp']

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