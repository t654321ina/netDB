
#F74022086 資訊106 黃筱婷
import requests
from bs4 import BeautifulSoup
#response = requests.get("http://www.appledaily.com.tw/realtimenews/section/new/")

response = requests.get("http://tv.atmovies.com.tw/tv/attv.cfm?action=todaytime&tday=2016-03-18&group_id=M")
#response = requests.get("https://www.facebook.com/taiwanstat/?fref=ts")
#<a class=at15b target="_self" href="/tv/attv.cfm?action=channeltime&channel_id=CH57&tday=2016-03-18">東森洋片台</a>


soup = BeautifulSoup(response.text, "lxml")
channels = soup.find_all("a", {"class": "at15b"})

tables = soup.find_all("table", {"class": "at9"})

'''終端機版本'''
i = 0
while i <len(channels):
	print('* 頻道: 	'+channels[i].text) #印出電影台
	print('時間	片名')

	times = tables[i].find_all("td", {"align": "center", "class":"at9"})
	movies = tables[i].find_all("font", {"class": "at11"})
	j = 2 #前兩個不是
	while j < len(times):
		print(times[j].text+'	'+movies[j-2].text)
		j +=1
	
	i += 1

'''POST 版本 
	
#api: http://52.192.20.250/chat/create/robot/
#robot_id: 108143422899450

i = 0
while i <len(channels):
	payload = {'robot_id': '108143422899450', 'content': '* 頻道: 	'+channels[i].text,'lng':'120','lat':'22.4'}
	req = requests.post("http://52.192.20.250/chat/create/robot/", data=payload)
	payload = {'robot_id': '108143422899450', 'content': '時間	片名','lng':'120','lat':'22.4'}
	req = requests.post("http://52.192.20.250/chat/create/robot/", data=payload)

	times = tables[i].find_all("td", {"align": "center", "class":"at9"})
	movies = tables[i].find_all("font", {"class": "at11"})
	j = 2 #前兩個不是
	while j < len(times):
		payload = {'robot_id': '108143422899450', 'content': times[j].text+'	'+movies[j-2].text,'lng':'120','lat':'22.4'}
		req = requests.post("http://52.192.20.250/chat/create/robot/", data=payload)
		j +=1
	
	i += 1


print(req.status_code)
'''