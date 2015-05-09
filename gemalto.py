import requests
from bs4 import BeautifulSoup
import re
import time
from pyshorteners.shorteners import Shortener
from pprint import pprint

GEMALTO_URL = "https://gemalto-recrute.talent-soft.com/offre-de-emploi/liste-offres.aspx?changefacet=1&facet_JobCountry=41&LCID=1033"

shortener = Shortener('TinyurlShortener')

r = requests.get(GEMALTO_URL)
soup = BeautifulSoup(r.text)

nombre_offre = re.findall(r'\d+', soup.find(class_="resultat").text)[0]

print("Gemalto ({0}) :".format(nombre_offre))

results = soup.find(id="listing-resultat").find('ul').find_all('li', recursive=False)

for result in results:
    publie_le = time.strftime('%d/%m/%Y', time.strptime(result.ul('li')[1].text, '%m/%d/%Y'))
    poste = result.h2.text.strip()
    url = result.h2.a['href']
    print("\t{0} - {1} - {2}".format(publie_le, poste, shortener.short(url)))
