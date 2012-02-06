<<<<<<< HEAD

"""
echo client, usage:

 python echo_client.py <host> <port>

Both host and port are optional, defaults: localhost 50003
host must be present if you want to provide port
"""

import select
import socket 
import sys

host = 'localhost' 
port = 50003
size = 1024 

nargs = len(sys.argv)
if nargs > 1:
    host = sys.argv[1]
if nargs > 2:
    port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, 
                  socket.SOCK_STREAM) 
s.connect((host,port))
input = [s, sys.stdin]
running = 1

while running:
    inputready,outputready,exceptready = select.select(input,[],[])

    for i in inputready:
        if i == sys.stdin:
            thedata = sys.stdin.readline()
            if len(thedata) > 1:
                s.send(thedata)
            else:
                running = 0
        else:
            data = s.recv(size)  
            print '%s\n' % (data)
s.close()    

=======

"""
echo client, usage:

 python echo_client.py <host> <port>

Both host and port are optional, defaults: localhost 50003
host must be present if you want to provide port
"""

import select
import socket 
import sys

host = 'localhost' 
port = 50003
size = 1024 

nargs = len(sys.argv)
if nargs > 1:
    host = sys.argv[1]
if nargs > 2:
    port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, 
                  socket.SOCK_STREAM) 
s.connect((host,port))
input = [s, sys.stdin]
running = True

while running:
    inputready,outputready,exceptready = select.select(input,[],[])

    for i in inputready:
        if i == sys.stdin:
            readline = sys.stdin.readline()
            if len(readline) > 1:
                s.send(readline)
            else:
                running = False
        else:
            data = s.recv(size)  
            print '%s\n' % (data)
s.close()    

>>>>>>> 0e5ac8e4f046441b94bf248e1e53e8da3cbde7df
