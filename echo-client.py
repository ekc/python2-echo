# Echo client program
import socket, sys

if (len(sys.argv) < 3):
    print "Usage: ", sys.argv[0], "target_host target_port [message]"
    sys.exit(1)
host = sys.argv[1]    # The remote host
port = int(sys.argv[2])

# if only hostname and port
if (len(sys.argv) == 3):
    msg = 'Hello, world'
else:
    msg = ' '.join(sys.argv[3:])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print s.getsockname(), " <= ", msg
s.sendall(msg)
data = s.recv(1024)
s.close()
print '=> ', repr(data)
