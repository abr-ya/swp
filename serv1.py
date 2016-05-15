import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222)) #связь сокета с адресом
s.listen(10) #слушать адрес, длина очереди
while True:
    conn, addr = s.accept() #установка соединения
    while True:
        data = conn.recv(1024)
        if data == 'close': break
        conn.send(data) #отправка данных назад
    conn.close()