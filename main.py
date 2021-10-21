import requests 
from bs4 import BeautifulSoup
import time
token = '2099132828:AAFFsSEwxR3EaW0akhXoy-WxQzDjB2fvmyA'
requests.get('https://api.telegram.org/bot'+token+'/sendMessage?chat_id=624064595&text=Софт работает')
i = 0
while True:
	response = requests.get('https://coinmarketcap.com/new/')
	soup = BeautifulSoup(response.content, 'html.parser')
	coin = soup.find('div', {'class': 'sc-1teo54s-2 fZIJcI'}).text
	print(coin)
	if coin == coin:
		1time.sleep(300)
		if i == 11:
			requests.get('https://api.telegram.org/bot'+token+'/sendMessage?chat_id=624064595&text=Софт работает')
			print(i)
			i = 0
		i = i + 1
	else:
		coin = coin[1:]
		requests.get('https://api.telegram.org/bot'+token+'/sendMessage?chat_id=624064595&text=Новый токен! ' +coin)