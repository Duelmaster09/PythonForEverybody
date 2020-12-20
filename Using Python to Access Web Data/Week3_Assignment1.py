'''You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.
http://data.pr4e.org/intro-short.txt
Enter the header values for Last-Modified, ETag, Content-Length, Cache-Control and Content-Type in each of the fields below and press "Submit".'''

import socket

mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))

cmd='GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

resp=""

while True:
    data=mysock.recv(512)
    if len(data)<1:
        break
    resp+=data.decode()

resp_lines=resp.split('\r\n')
headers=resp_lines[:resp_lines.index('')]

for vals in headers:
    if vals.startswith('Last-Modified: ') or vals.startswith('ETag: ') or vals.startswith('Content-Length: ') or vals.startswith('Cache-Control: ') or vals.startswith('Content-Type: '):
        print(vals)