import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)

def server(conn):
    while True:
        data = conn.recv(1024)
        if (data == b'close') or (not data):
            break
        conn.send(data)
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connection", addr)
    t = threading.Thread(target=server, args=(conn, addr))
    t.start()