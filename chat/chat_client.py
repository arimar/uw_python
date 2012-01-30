"""
echo client, usage:

 python echo_client.py <host> <port>

Both host and port are optional, defaults: localhost 50000
host must be present if you want to provide port
"""

import socket 
import sys
import select

host = 'localhost' 
port = 50003 
size = 1024 
timeout = 10

nargs = len(sys.argv)
if nargs > 1:
    host = sys.argv[1]
if nargs > 2:
    port = int(sys.argv[2])

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

print 'Connection accepted by (%s,%s)' % (host,port)

while True:
    try:
	inputready, outputready,exceptready = select.select([0,s],[],[])

	for i in inputready:
		if i == 0:
			data = sys.stdin.readline().strip()
                        print "Data is %s" % data
	        	if data: 
                                s.send(data)
                        elif i == s:
	        	        data = s.recv(s)
	        	        if not data:
	        			print 'Shutting down.'
		        		break
                		else:
                        		sys.stdout.write(data + '\n')
                        		sys.stdout.flush()

    except KeyboardInterrupt:
        print 'Interrupted.'
	s.close()
	break
