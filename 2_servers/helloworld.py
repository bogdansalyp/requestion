#!/usr/bin/env python3

from wsgiref.simple_server import make_server
from cgi import parse_qs

html = """
<html>
<head></head>
<body>
    <h1>{}</h1>
    <h2>Parameters:</h2>
    <p>{}</p>
</body>
</html
"""

def application(env, start_response):
    try:
        request_body_size = int(env.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0

    request_body = env['wsgi.input'].read(request_body_size)

    d = {}
    d.update(parse_qs(env['QUERY_STRING']))
    d.update(parse_qs(request_body))
    result = ''.join(['{}: {}, '.format(k, v) for (k, v) in d.items()])

    response_body = html.format("Hello World!", result or "no parameters").encode()

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return[response_body]

httpd = make_server('localhost', 8081, application)
httpd.serve_forever()