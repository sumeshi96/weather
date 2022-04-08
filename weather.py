from bs4 import BeautifulSoup
import requests

url = requests.get("https://tenki.jp/forecast/1/4/2300/1202/")

soup = BeautifulSoup(url.text, "lxml")
