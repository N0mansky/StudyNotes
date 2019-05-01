#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server
from cgi import parse_qs,escape


html="""
<html>
<body>
   <form method="post" action="">
        <p>
           Age: <input type="text" name="age" value="{age}">
        </p>
        <p>
            Hobbies:
            <input
                name="hobbies" type="checkbox" value="software"
                {checked_software}
            > Software
            <input
                name="hobbies" type="checkbox" value="tunning"
                {checked_tunning}
            > Auto Tunning
        </p>
        <p>
            <input type="submit" value="Submit">
        </p>
    </form>
    <p>
        Age: {age}<br>
        Hobbies: {hobbies}
    </p>
</body>
</html>
"""

def application(environ,start_response):
    try:
        request_body_size = environ['CONTENT_LENGTH'] or '0'
        request_body_size = int(request_body_size)
    except Exception :
        request_body_size
        raise 
    request_body = environ['wsgi.input'].read(request_body_size)
    request_body = request_body.decode()
    d = parse_qs(request_body)
    age = escape(d.get('age',[''])[0]) or 'Empty'
    hobbies = [ escape(hobby) for hobby in d.get('hobbies',[])]
    response_body = html.format(
            checked_software=('','checked')['software' in hobbies],
            checked_tunning=('','checked')['tunning' in hobbies],
            age=age,
            hobbies=','.join(hobbies) or 'No hobbies?'
            )
    status = '200 OK'
    response_headers =[
        ('Content-Length',str(len(response_body))),
        ('Content-Type','text/html'),
        ('Server','Nomansky')
    ]
    start_response(status,response_headers)
    return [response_body.encode()]

httpd = make_server('localhost',8051,application)
httpd.serve_forever()
print('Ended...')


















