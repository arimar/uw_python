"""
echo server, usage:

 python echo_server.py <port>

Port is optional, default: 50000
"""

import socket 
import sys

host = '' 
port = 50002 

if len(sys.argv) > 1:
    port = int(sys.argv[1])

backlog = 5 
size = 1024 

# server's listener socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Release listener socket immediately when program exits, 
# avoid socket.error: [Errno 48] Address already in use
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((host,port)) 

print 'echo_server listening on port', port
s.listen(backlog) 

while True: 
    client, address = s.accept()
    print 'accepted connection from ',address
    while True:
    	data = client.recv(size) 
    	if data: 
        	client.send('arimar: %s' % data) 
	else:
    		client.close()
		print 'closed connection'
		break
