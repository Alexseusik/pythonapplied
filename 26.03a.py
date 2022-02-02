import requests
from bs4 import BeautifulSoup
import re

DATES = []
TEMP_MAX = []
TEMP_MIN = []


city = input("Введите название города на английском ").capitalize()
temp_url = "https://www.meteoprog.ua/ua/weather/{}".format(city)


page = requests.get(temp_url)
soup = BeautifulSoup(page.text, "html.parser")

section = BeautifulSoup(str(soup.findAll("section", class_="weather-day-by-day-slider")), "html.parser")

allDate = BeautifulSoup(str(section.findAll("div", class_="thumbnail-item__subtitle")), "html.parser").findAll("span")

for date in allDate:
    DATES.append(date.text)


allTemp = BeautifulSoup(str(section.findAll("div", class_="thumbnail-item__temperature")), "html.parser")\
    .findAll(title=re.compile(r"."))

for temp in allTemp:
    tempMax = temp.findNext(class_="temperature-max").findNext("h6").text
    TEMP_MAX.append(tempMax)

for temp in allTemp:
    tempMin = temp.findNext(class_="temperature-min").findNext("h6").text
    TEMP_MIN.append(tempMin)


for i in range(len(DATES)):
    print(f"Weather in {city} for {DATES[i]} is\n"
          f"max = {TEMP_MAX[i]}\n"
          f"min = {TEMP_MIN[i]}\n")


