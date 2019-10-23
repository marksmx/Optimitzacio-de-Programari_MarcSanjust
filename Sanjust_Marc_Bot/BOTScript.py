import telebot
import random
from telebot import types

bot = telebot.TeleBot("934530540:AAF-NYqSFHAtt8CgDZ5NQNwWQW8Vs1XkXAw")

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
	lista=(random.randint(1,5))
	switcher = {
		1: "Me acaba de picar una serpiente!",
		2: "Buenos dias. Busco trabajo.",
		3: "Hola, soy paraguayo y quiero pedirle la mano de su hija para casarme con ella.",
		4: "Buenos dias, queria una camiseta de un personaje inspirador.",
		5: "Sabes? Hoy me he comprado una paloma que cuesta diez mil euros."
	}
	bot.reply_to(message, switcher.get(lista,"Error"))

	preg = False

	if preg == False:
		if lista == 1:
			@bot.message_handler(commands=['Cobra'])
			def test(message):
				bot.reply_to(message, "No, idiota, lo ha hecho gratis!")
			preg = True

		if lista == 2:
		   @bot.message_handler(commands=['Jardinero'])
		   def test(message):
			   bot.reply_to(message, "Dejar dinero? Si lo que busco es trabajo!")
		   preg = True

		   if lista == 3:
			@bot.message_handler(commands=['Para'])
			def test(message):
			  bot.reply_to(message, "Paraguayo")
  	  	  	preg = True

		if lista == 4:
			@bot.message_handler(commands=['Ghandi'])
			def test(message):
				bot.reply_to(message, "No, mediani.")
			preg = True

			if lista == 5:
		 		@bot.message_handler(commands=['Mensajera'])
		 		def test(message):
			 		bot.reply_to(message, "No no, no te exagero")
	     		preg = True

bot.polling()

