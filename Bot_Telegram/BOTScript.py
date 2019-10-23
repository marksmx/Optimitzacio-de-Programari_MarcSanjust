import telebot
import random
from telebot import types

bot = telebot.TeleBot("934530540:AAF-NYqSFHAtt8CgDZ5NQNwWQW8Vs1XkXAw")

@bot.message_handler(commands=['joke'])
def test(message):
	lista=(random.randint(1,5))
	switcher = {
		1: "Acudit1",
		2: "Acudit2",
		3: "Acudit3",
		4: "Acudit4",
		5: "Acudit5"
	}
	bot.reply_to(message, switcher.get(lista,"Error"))

@bot.message_handler(commands=['question'])
def test(message):
	lista=(random.randint(1,5))
	switcher = {
		1: "Quan son 2 + 2?",
		2: "Preg?",
		3: "Otra?",
		4: "Saps?",
		5: "No Saps?"
	}
	bot.reply_to(message, switcher.get(lista,"Error"))

	@bot.message_handler(commands=['hola'])
	def test(message):
			print("yee")
			bot.reply_to(message, "Blyat")

bot.polling()
