import requests 
from bs4 import BeautifulSoup
import time
token = '2099132828:AAFFsSEwxR3EaW0akhXoy-WxQzDjB2fvmyA'
requests.get('https://api.telegram.org/bot'+token+'/sendMessage?chat_id=624064595&text=Софт работает')
i = 1
coin_2 = 1
while True:
	response = requests.get('https://coinmarketcap.com/new/')
	soup = BeautifulSoup(response.content, 'html.parser')
	coin = soup.find('div', {'class': 'sc-1teo54s-2 fZIJcI'}).text
	coin = coin[1:]
	time.sleep(15)
	print('Hi')
	time.sleep(15)
	if coin == coin_2:
		requests.get('https://api.telegram.org/bot'+token+'/sendMessage?chat_id=624064595&text=' +coin)
		time.sleep(15)
		print('Hi')
		time.sleep(15)
		print('Hi')
		time.sleep(15)
		print('Hi')
		time.sleep(15)
		if i == 24:
			requests.get('https://api.telegram.org/bot'+token+'/sendMessage?chat_id=624064595&text=Софт работает')
			i = 0
		i = i + 1
		coin_2 = coin
	else:
		coin_2 = coin
		requests.get('https://api.telegram.org/bot'+token+'/sendMessage?chat_id=624064595&text=Новый токен! ' +coin)
	time.sleep(15)
	print('Hi')	
	time.sleep(15)
	print('Hi')	
	time.sleep(15)
	print('Hi')	
	time.sleep(15)
