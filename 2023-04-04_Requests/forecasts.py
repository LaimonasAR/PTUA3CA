import requests
from bs4 import BeautifulSoup as bs


def get_forecast(site):
    r = requests.get(site, timeout=3)
    soup = bs(r.content, "html.parser")
    res = soup.find(class_="item forecast")
    for i in range(0,9):
        res_cities = res.find(class_="item full clearfix")
        # print(res)
        res_city = res_cities.find(class_="city")
        print(res_city)
        print(type(res_city))


get_forecast("https://orai.15min.lt/prognozes")
