"""
echo client, usage:

 python echo_client.py <host> <port>

Both host and port are optional, defaults: localhost 50000
host must be present if you want to provide port
"""

import socket 
import sys

host = 'localhost' 
port = 50000 
size = 1024 
string_to_send = ''

nargs = len(sys.argv)
if nargs > 1:
    host = sys.argv[1]
if nargs > 2:
    port = int(sys.argv[2])

while True:
	string_to_send = raw_input('-> ')
	if (string_to_send == ''):
		s.close()
		break;
	else:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		s.connect((host,port)) 
		s.send(string_to_send) 
		data = s.recv(size) 
		s.close() 

