import telebot
import random
from telebot import types
from multiprocessing import Value

f = [line.rstrip('\n') for line in open("/home/msanjust/Escriptori/test/Practica1_MarcSanjust/Python/ch.txt")]

bot = telebot.TeleBot("934530540:AAF-NYqSFHAtt8CgDZ5NQNwWQW8Vs1XkXAw")


fet_cobra = Value('i', 0)

@bot.message_handler(commands=['joke'])
def test(message):
	lista=(random.randint(1,5))
	switcher = {
		1: "Cual es la fruta mas divertida? La naranja ja ja ja ja",
		2: "Donde cuelga Superman su supercapa? En superchero",
		3: "Que le dice una iguana a su hermana gemela? Somos iguanitas",
		4: "Si los zombies se deshacen con el paso del tiempo, zombiodegradables?",
		5: "Para que van una caja al gimnasio? Para hacerse caja fuerte."
	}
	bot.reply_to(message, switcher.get(lista,"Error"))

@bot.message_handler(commands=['question'])
def test(message):
	lista=(random.randint(1,2))
	switcher = {
		1: "Me acaba de picar una serpiente!",
		2: "Buenos dias. Busco trabajo.",
		3: "Hola, soy paraguayo y quiero pedirle la mano de su hija para casarme con ella.",
		4: "Buenos dias, queria una camiseta de un personaje inspirador.",
		5: "Sabes? Hoy me he comprado una paloma que cuesta diez mil euros."
	}
	bot.reply_to(message, switcher.get(lista,"Error"))
	fet_cobra.value = 0


	@bot.message_handler(content_types=['text'])
	def test(message):
		if lista == 1:
			if message.text == "Cobra?" and fet_cobra.value == 0:
				bot.reply_to(message, f[0])
				fet_cobra.value = 1
			elif fet_cobra.value == 0:
				bot.reply_to(message, "Como que "+message.text+"?")

		if lista == 2:
			if message.text == "Que le parece de jardinero?" and fet_cobra.value == 0:
				bot.reply_to(message, f[1])
				fet_cobra.value = 1
			elif fet_cobra.value == 0:
				bot.reply_to(message, "Que trabajo es "+message.text+"?")

		if lista == 3:
			if message.text == "Para que?" and fet_cobra.value == 0:
				bot.reply_to(message, f[2])
				fet_cobra.value = 1
			elif fet_cobra.value == 0:
				bot.reply_to(message, "Como que para "+message.text+"?")

		if lista == 4:
			if message.text == "Ghandi?" and fet_cobra.value == 0:
				bot.reply_to(message, f[3])
				fet_cobra.value = 1
			elif fet_cobra.value == 0:
				bot.reply_to(message, "Quien es "+message.text+"? Es fascista?")

		if lista == 5:
			if message.text == "Mensajera?" and fet_cobra.value == 0:
				bot.reply_to(message, f[4])
				fet_cobra.value = 1
			elif fet_cobra.value == 0:
				bot.reply_to(message, message.text+"? Que?")

		else:
			print '0'
print bot

bot.polling()
