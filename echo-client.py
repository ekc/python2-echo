# Echo client program
import socket, sys

HOST = sys.argv[1]    # The remote host
PORT = int(sys.argv[2])              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('Hello, world')
data = s.recv(1024)
s.close()
print 'Received', repr(data)
