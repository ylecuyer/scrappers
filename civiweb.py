import requests
from bs4 import BeautifulSoup
import re
import time
from datetime import datetime
from pprint import pprint

CIVIWEB_URL = "https://www.civiweb.com/FR/offre-recherche-avancee/Page/1.aspx?q=s=@c=42,@a=@e=@m=@f=@r=--@v=@t="

r = requests.get(CIVIWEB_URL)
soup = BeautifulSoup(r.text)

top_bleu = soup.find(class_="top bleu").find("h1")

nombre_offre = re.findall(r'\d+', top_bleu.text)[0]
print("Civiweb ({0}) :".format(nombre_offre))

results = soup(class_='result')

for result in results:
    publie_le = result.time.text[-10:]
    compagnie = result.find(class_="location").text[16:]
    poste = result.h1.text[:47]
    url = "https://www.civiweb.com" + result.find(class_='xt_offrelink')['href']
    if len(result.h1.text) > 47:
        poste += "..."
    print("\t{0} - {1} - {2} - {3}".format(publie_le, compagnie, poste, url))
