#!/usr/local/bin/python3
import cgi


def check_strings(fstr, sstr):
    first_string = fstr.split()
    second_string = sstr.split()
    resultstring = []
    for element in first_string:
        if element in second_string:
            continue
        else:
            resultstring.append(element)
    return resultstring


if __name__ == '__main__':
    form = cgi.FieldStorage()
    first, second = str(form.getfirst('first', '')), str(form.getfirst('second', ''))
    result = check_strings(first, second)

    with open("result.html", encoding="utf-8") as f:
        html = f.read()

    print("Content-Type: text/html; charset=utf-8\n")
    html = html.replace('result', str(result))
    print(html)
