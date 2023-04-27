import csv

from bs4 import BeautifulSoup
import requests

mainurl = "https://www.telia.lt/prekes/mobilieji-telefonai"
mainurl_phone = "https://www.telia.lt/prekes/mobilieji-telefonai?q=%3Arelevance&page="

source = requests.get(mainurl).text
soup = BeautifulSoup(source, "html.parser")

blokai = soup.find_all(
    "div",
    class_="mobiles-product-card card card__product card--anim js-product-compare-product",
)


def find_and_save_first(blokai):
    with open(
        "Telia Samsung telefonai.csv", "w", encoding="UTF-8", newline=""
    ) as failas:
        csv_writer = csv.writer(failas)
        csv_writer.writerow(["Modelis", "Mėnesio kaina", "Kaina"])

        for blokas in blokai:
            try:
                pavadinimas = blokas.find(
                    "a", class_="mobiles-product-card__title js-open-product"
                ).text.strip()
                men_kaina = blokas.find(
                    "div", class_="mobiles-product-card__price-marker"
                ).text.strip()
                kaina = blokas.find_all(
                    "div", class_="mobiles-product-card__price-marker"
                )[1].text.strip()
                print(pavadinimas, men_kaina, kaina)
                csv_writer.writerow([pavadinimas, men_kaina, kaina])
            except:
                pass


find_and_save_first(blokai)

links = soup.find(class_="pagination")
last_page_link = links.find_all("a")
for link in last_page_link:
    last_a = last_page_link[6]
print(type(last_a))

last_link = last_a["href"]
last_link_number = last_link[-1]
# print(last_link_number)
# print(last_page_link)


def find_and_save(blokai):
    with open(
        "Telia Samsung telefonai.csv", "a", encoding="UTF-8", newline=""
    ) as failas:
        csv_writer = csv.writer(failas)
        # csv_writer.writerow(["Modelis", "Mėnesio kaina", "Kaina"])

        for blokas in blokai:
            try:
                pavadinimas = blokas.find(
                    "a", class_="mobiles-product-card__title js-open-product"
                ).text.strip()
                men_kaina = blokas.find(
                    "div", class_="mobiles-product-card__price-marker"
                ).text.strip()
                kaina = blokas.find_all(
                    "div", class_="mobiles-product-card__price-marker"
                )[1].text.strip()
                print(pavadinimas, men_kaina, kaina)
                csv_writer.writerow([pavadinimas, men_kaina, kaina])
            except:
                pass


# for i in range(0, int(last_link_number) - 1):
for i in range(1, int(last_link_number)):
    page_link = mainurl_phone + str(i)
    source_two = requests.get(page_link).text
    soup = BeautifulSoup(source_two, "html.parser")

    blokai = soup.find_all(
        "div",
        class_="mobiles-product-card card card__product card--anim js-product-compare-product",
    )
    find_and_save(blokai)
# print(blokai)


# https://www.telia.lt/prekes/mobilieji-telefonai/samsung?q=%3Arelevance&page=0
