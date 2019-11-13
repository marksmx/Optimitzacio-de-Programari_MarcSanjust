import telebot
import random
from telebot import types
from multiprocessing import Value

bot = telebot.TeleBot("934530540:AAF-NYqSFHAtt8CgDZ5NQNwWQW8Vs1XkXAw")

f = [line.rstrip('\n') for line in open("/home/msanjust/Escriptori/test/Practica1_MarcSanjust/Python/ch.txt")]

fet_cobra = Value('i', 0)

@bot.message_handler(commands=['add'])
def test(message):
	if " " in message.text:
		cl_j=open("/home/msanjust/Escriptori/test/Practica1_MarcSanjust/Python/ch_l.txt",'a')
		jk=message.text
		jkf=jk.replace("/add ","")
		cl_j.write(jkf+"\n")
		cl_j.close
	else:
		print 0
@bot.message_handler(commands=['joke'])
def test(message):
	lista=(random.randint(1,5))
	switcher = {
		1: cl_j[0],
		2: cl_j[1],
		3: cl_j[2],
		4: cl_j[3],
		5: cl_j[4]
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
