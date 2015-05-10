import requests
from bs4 import BeautifulSoup
import re
from pyshorteners.shorteners import Shortener
from pprint import pprint

COORDINATION_SUD_URL="http://www.coordinationsud.org/espace-emploi/?pays%5B%5D=colombie&age=&mots="

shortener = Shortener('TinyurlShortener')

r = requests.get(COORDINATION_SUD_URL)
soup = BeautifulSoup(r.text)

results = soup.find(class_='elements').find_all('article')

nombre_offre = len(results)
print("Coordination Sud ({0}) :".format(nombre_offre))


for result in results:
    publie_le = result.find(class_="date").text
    entreprise = result.find(class_="author").text
    poste = result.find(class_="entry-title").text.strip()
    url = result.find(class_="entry-title").find('a')['href']
    print("\t{0} - {1} - {2} - {3}".format(publie_le, entreprise, poste, shortener.short(url)))
