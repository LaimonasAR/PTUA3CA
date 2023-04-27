from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.delfi.lt").text

soup = BeautifulSoup(source, "html.parser")
blokas = soup.find("div", class_="headline")
blokelis = blokas.find(class_="headline-category")
blokelis = blokelis.find("a")
print(blokelis.text)
# print(blokas.prettify())


kategorija = blokas.find('div', class_ = 'headline-category').text.strip()
tekstas = blokas.find('a', class_ = 'CBarticleTitle').text.strip()
linkas = blokas.find('a', class_="CBarticleTitle")['href']

print(kategorija)
print(tekstas)
print(linkas)