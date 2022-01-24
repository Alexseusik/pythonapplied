from urllib.request import urlopen


url = "http://www.matfiz.univ.kiev.ua/pages/13"

response = urlopen(url)
info = response.info()
enc = info.get_content_charset()


html = str(response.read(), encoding=enc)
print(html)
