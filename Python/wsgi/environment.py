#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server

def application(environ,start_response):
    response_body = [
    '{}:{}'.format(key,value) for key,value in sorted(environ.items())
    ]
    response_body = 'The Beggining\n'+'\n'.join(response_body)+'The Ending\n'
    response_body=response_body.encode()
    status = '200 OK'
    response_headers = [('Content-Type','text/plain'),('Content-Length',str(len(response_body)))]
    start_response(status,response_headers)
    return [response_body]

httpd = make_server('127.0.0.1',8051,application)
httpd.handle_request()
print('Ended.........')
