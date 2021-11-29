# Echo server program
import socket, sys, thread, time
HOST = ''                 # Symbolic name meaning all available interfaces

def on_new_thread(s):
    while True:
        conn, addr = s.accept()
        data = conn.recv(1024)
        print conn.getsockname(), addr, ":", data
        conn.sendall(data)
        conn.close()

try:
    ports = [int(port) for port in sys.argv[1:] if (int(port) > 0 and int(port) < 65536)]
except ValueError as e:
    print e
    sys.exit(1)
ss = []
for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Listening on ", port
    s.bind((HOST, port))
    s.listen(5)
    ss.append(s)

for s in ss:
    thread.start_new_thread(on_new_thread,(s,))

while True:
    try:
        time.sleep(5)
    except KeyboardInterrupt as e:
        print "Receive Keyboard Interrupt: exiting ..."
        sys.exit(0)
