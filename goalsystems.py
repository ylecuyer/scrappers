import requests
from bs4 import BeautifulSoup
import re
from pyshorteners.shorteners import Shortener
from pprint import pprint

GOAL_SYSTEMS_URL = "http://www.goalsystems.com/index.php?option=com_content&view=article&id=311&Itemid=198&lang=fr"

shortener = Shortener('TinyurlShortener')

r = requests.get(GOAL_SYSTEMS_URL)
soup = BeautifulSoup(r.text)

results = soup.find(class_='article-rel-wrapper').find_all('li')
results = [result for result in results if re.search(r'Colombie', result.a.text)]

nombre_offre = len(results)
print("Goal Systems ({0}) :".format(nombre_offre))


for result in results:
    publie_le = 'xx/xx/xxxx'
    poste = result.a.text
    url = "http://www.goalsystems.com" + result.a['href']
    print("\t{0} - {1} - {2}".format(publie_le, poste, shortener.short(url)))
