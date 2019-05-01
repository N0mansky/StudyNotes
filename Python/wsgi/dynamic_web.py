#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server
from cgi import parse_qs,escape

html="""
<html>
    <body>
        <form method="get" action="">
            <p>
            Age: <input type="text" name="age" value="{age}"/>
            </p>
            <p>
            Hobbies: <input name="hobbies" type="checkbox" value="software" {checked_software} /> Software
            <input name="hobbies" type="checkbox" value="tunning" {checked_tunning} /> Auto tunning
            </p>
            <p>
                <input type="submit" value="Submit" />
            </p>
        </form>
        <p>
            Age: {age}<br/>
            Hobbies: {hobbies}
        </p>
    </body>
</html>
"""

def application(environ,start_response):
    # resolve QUERY_STRING
    d = parse_qs(environ['QUERY_STRING'])
    print(d)
    age = d.get('age',[''])[0]
    hobbies = d.get('hobbies',[])

    age = escape(age)
    hobbies = [ escape(hobby) for hobby in hobbies ]
    response_body = html.format(
        checked_software=('','checked')['software' in hobbies],
        checked_tunning=('','checked')['tunning' in hobbies],
        age=age or 'Empty',
        hobbies=','.join(hobbies) or 'No hobbies?'
    )
    send_msg = response_body.encode()
    status = '200 OK'
    content_len=len(response_body)
    response_headers = [('Content-Type','text/html'),
                        ('Content-Length',str(content_len)),
                        ('Server','NOmansky'),
    ]
    start_response(status,response_headers)
    return [send_msg]

httpd = make_server('localhost',8051,application)
httpd.serve_forever()
print('Ended...')
