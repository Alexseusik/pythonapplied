from urllib.request import urlopen, urlretrieve
import re
import os


TOPIC = r'<a href=\"(?P<URL>.*?)\" >Тема {}\..*?</a>'
PYFILE = r'"(.+?\.pyw*)"'
NAME = r'.*/(?P<NAME>.+)'


theme = int(input("Enter number"))
url = "http://www.matfiz.univ.kiev.ua"
topics = "/pages/13"

response = urlopen(url + topics)
info = response.info()
enc = info.get_content_charset()
html = str(response.read(), encoding=enc)

match = re.search(TOPIC.format(theme), html)
print(match)

if match:
    topic = match.group("URL")
    response = urlopen(url + topic)
    html_topic = str(response.read(), encoding=enc)
    print(topic)
    if not os.path.exists("pyfiles"):
        os.mkdir("pyfiles")
    for pyfile in re.findall(PYFILE, html_topic):
        m = re.search(NAME, pyfile)
        name = m.group("NAME")
        urlretrieve(url + pyfile,
                    os.path.join('pyfiles', name))
        print(name)
