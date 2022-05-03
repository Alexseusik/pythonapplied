from wsgiref.simple_server import make_server
import cgi
from string import Template

HOST = ''
PORT = 9000


def check_strings(fstr, sstr):
    fstring = fstr.split()
    sstring = sstr.split()
    resultstring = []
    for felement in fstring:
        if felement in sstring:
            continue
        else:
            resultstring.append(felement)
    return resultstring


def app(environ, start_response):

    path = environ['PATH_INFO'].lstrip('/')
    if path == '':
        form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        first, second = str(form.getfirst('first', '')), str(form.getfirst('second', ''))
        if first and second:
            result = check_strings(first, second)
        else:
            result = None
        with open('check_string.html', encoding='utf-8') as f:
            page = Template(f.read()).substitute(result=result)

        start_response('200 OK', [('Content-type', 'text/html; charset = utf-8')])
        return [bytes(page, encoding='utf-8')]
    else:
        with open('error_404.html', encoding='utf-8') as f:
            page = f.read()

        start_response('404 PAGE NOT FOUND', [('Content-type', 'text/html; charset = utf-8')])
        return [bytes(page, encoding='utf-8')]


if __name__ == '__main__':
    print(f'Server on http://localhost:{PORT} started')
    httpd = make_server(HOST, PORT, app)
    httpd.serve_forever()
