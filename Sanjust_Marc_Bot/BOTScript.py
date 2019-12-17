import telebot
import random
from telebot import types
from multiprocessing import Value

bot = telebot.TeleBot("934530540:AAF-NYqSFHAtt8CgDZ5NQNwWQW8Vs1XkXAw")

f = [line.rstrip('\n') for line in open("/home/msanjust/Escriptori/test/Practica1_MarcSanjust/Python/ch.txt")]
f1 = [line.rstrip('\n') for line in open("/home/msanjust/Escriptori/test/Practica1_MarcSanjust/Python/ch_l.txt")]
size = len(f1)
lista = Value('i', 0)

@bot.message_handler(commands=['start'])
def test(message):
	bot.reply_to(message, "Abrir menu: /menu"+"\n"+"Chiste Normal: /joke"+"\n"+"Chiste de tipo Pregunta: /question"+"\n"+"Crear Chiste Normal: /add *chiste*"+"\n")

@bot.message_handler(commands=['menu'])
def test(message):
	bot.reply_to(message, "Abrir menu: /menu"+"\n"+"Chiste Normal: /joke"+"\n"+"Chiste de tipo Pregunta: /question"+"\n"+"Crear Chiste Normal: /add *chiste*"+"\n")

@bot.message_handler(commands=['add'])
def test(message):
	if " " in message.text:
		cl_j=open("/home/msanjust/Escriptori/test/Practica1_MarcSanjust/Python/ch_l.txt",'a')
		jk=message.text
		jkf=jk.replace("/add ","")
		cl_j.write(jkf+"\n")
		cl_j.close
	else:
		print ''

@bot.message_handler(commands=['joke'])
def test(message):
	max = 5
	lista.value=(random.randint(0,size-1))
	thislist=[f1[0],f1[1],f1[2],f1[3],f1[4]]

	if size > max:
		max += 1
		thislist.insert(size,f1[size-1])

	print size
	bot.reply_to(message, f1[lista.value])

@bot.message_handler(commands=['question'])
def test(message):
    lista.value=0
    if lista.value>0:
	    switcher = {
		    1: "Me acaba de picar una serpiente!",
		    2: "Buenos dias. Busco trabajo.",
		    3: "Hola, soy paraguayo y quiero pedirle la mano de su hija para casarme con ella.",
		    4: "Buenos dias, queria una camiseta de un personaje inspirador.",
		    5: "Sabes? Hoy me he comprado una paloma que cuesta diez mil euros."
	    }
	    bot.reply_to(message, switcher.get(lista.value,"Error"))
    else:
		lista.value=(random.randint(1,5))
		switcher = {
		    1: "Me acaba de picar una serpiente!",
		    2: "Buenos dias. Busco trabajo.",
		    3: "Hola, soy paraguayo y quiero pedirle la mano de su hija para casarme con ella.",
		    4: "Buenos dias, queria una camiseta de un personaje inspirador.",
		    5: "Sabes? Hoy me he comprado una paloma que cuesta diez mil euros."
	    }
		bot.reply_to(message, switcher.get(lista.value,"Error"))

		@bot.message_handler(content_types=['text'])
		def test(message):
			#print fet_cobra.value, lista
			if lista.value == 0:
				lista.value=(random.randint(1,5))
				if lista.value == 1:
					if message.text == "Cobra?" and lista.value == 1:
						bot.reply_to(message, f[0])
						lista.value = 0
					else:
						bot.reply_to(message, "Como que "+message.text+"?")

				if lista.value == 2:
					if message.text == "Que le parece de jardinero?" and lista.value == 2:
						bot.reply_to(message, f[1])
						lista.value = 0
					else:
						bot.reply_to(message, "Que trabajo es "+message.text+"?")

				if lista.value == 3:
					if message.text == "Para que?" and lista.value == 3:
						bot.reply_to(message, f[2])
						lista.value = 0
					else:
						bot.reply_to(message, "Como que "+message.text+"?")

				if lista.value == 4:
					if message.text == "Ghandi?" and lista.value == 4:
						bot.reply_to(message, f[3])
						lista.value = 0
					else:
						bot.reply_to(message, "Quien es "+message.text+"? Es fascista?")

				if lista.value == 5:
					if message.text == "Mensajera?" and lista.value == 5:
						bot.reply_to(message, f[4])
						lista.value = 0
					else:
						bot.reply_to(message, message.text+"? Que?")

				else:
					print ''
			else:

				if lista.value == 1:
					if message.text == "Cobra?" and lista.value == 1:
						bot.reply_to(message, f[0])
						lista.value = 0
					else:
						bot.reply_to(message, "Como que "+message.text+"?")

				if lista.value == 2:
					if message.text == "Que le parece de jardinero?" and lista.value == 2:
						bot.reply_to(message, f[1])
						lista.value = 0
					else:
						bot.reply_to(message, "Que trabajo es "+message.text+"?")

				if lista.value == 3:
					if message.text == "Para que?" and lista.value == 3:
						bot.reply_to(message, f[2])
						lista.value = 0
					else:
						bot.reply_to(message, "Como que "+message.text+"?")

				if lista.value == 4:
					if message.text == "Ghandi?" and lista.value == 4:
						bot.reply_to(message, f[3])
						lista.value = 0
					else:
						bot.reply_to(message, "Quien es "+message.text+"? Es fascista?")

				if lista.value == 5:
					if message.text == "Mensajera?" and lista.value == 5:
						bot.reply_to(message, f[4])
						lista.value = 0
					else:
						bot.reply_to(message, message.text+"? Que?")

				else:
					print ''

print bot

bot.polling()
