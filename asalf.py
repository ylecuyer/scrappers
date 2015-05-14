import requests
from bs4 import BeautifulSoup
from pprint import pprint

ASALF_URL="http://www.asalf.com/index.php?option=com_content&view=article&id=54&Itemid=119"

r = requests.get(ASALF_URL)
soup = BeautifulSoup(r.text)

results = soup.find(class_='item-page').find_all('strong')

results.pop(0)

nombre_offre = len(results)
print("ASALF ({0}) :".format(nombre_offre))


for result in results:
    publie_le = 'xx/xx/xxxx'
    poste = result.text.strip()
    print("\t{0} - {1}".format(publie_le, poste))
