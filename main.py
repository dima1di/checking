import requests 
from bs4 import BeautifulSoup
import time
token = ''
requests.get('https://api.telegram.org/bot'+token+'/sendMessage?chat_id=&text=Софт работает')
i = 1
coin_2 = 1
while True:
	requests.get('https://api.telegram.org/bot'+token+'/sendMessage?chat_id=&text=Просто')
	response = requests.get('https://coinmarketcap.com/new/')
	soup = BeautifulSoup(response.content, 'html.parser')
	coin = soup.find('div', {'class': 'sc-1teo54s-2 fZIJcI'}).text
	coin = coin[1:]
	if coin == coin_2:
		requests.get('https://api.telegram.org/bot'+token+'/sendMessage?chat_id=&text=' +coin)
		if i == 24:
			requests.get('https://api.telegram.org/bot'+token+'/sendMessage?chat_id=&text=Софт работает')
			i = 0
		i = i + 1
		coin_2 = coin
		time.sleep(15)
	else:
		coin_2 = coin
		requests.get('https://api.telegram.org/bot'+token+'/sendMessage?chat_id=&text=Новый токен! ' +coin)
