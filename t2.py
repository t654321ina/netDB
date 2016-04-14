
import requests
from bs4 import BeautifulSoup
#response = requests.get("http://www.appledaily.com.tw/realtimenews/section/new/")

response = requests.get("http://tv.atmovies.com.tw/tv/attv.cfm?action=todaytime&tday=2016-03-18&group_id=M")
#response = requests.get("https://www.facebook.com/taiwanstat/?fref=ts")
#<a class=at15b target="_self" href="/tv/attv.cfm?action=channeltime&channel_id=CH57&tday=2016-03-18">東森洋片台</a>


soup = BeautifulSoup(response.text, "lxml")


tables = soup.find_all("table", {"class": "at9"})

print(tables[0].find_all("font", {"class": "at11"}))

