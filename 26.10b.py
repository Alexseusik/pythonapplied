import requests
from html.parser import HTMLParser
from time import localtime


class myHtmlParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.enteredtag = False

    def handle_starttag(self, tag, attrs):
        if tag == 'script':
            self.enteredtag = True

    def handle_data(self, data):
        if self.enteredtag and "draw_clock" in data:
            array = data.split()
            sitetime = [int(el) for el in array[0][-10:-2].split(',')]
            ltime = loctime()
            for element in zip(sitetime, ltime):
                if element[0] == element[1]:
                    continue
                else:
                    print("!!Час не співпадає!!")
            print("!!Локальний час і час з сайту співпадає!!")
                
    def handle_endtag(self, tag):
        if tag == "script":
            self.enteredtag = False


def loctime():
    return [localtime().tm_hour, localtime().tm_min, localtime().tm_sec]


city = 'kyiv'
URL = f"https://time.online.ua/in/{city}/"
url = requests.get(URL).text
parser = myHtmlParser()
parser.feed(url)







