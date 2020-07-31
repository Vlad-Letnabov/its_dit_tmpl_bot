# -*- coding: utf-8 -*-
import socket
import json

IFACES = ''                                    # чтобы привязать сразу ко всем, можно использовать ''
PORT = 53210
serv_sock = socket.socket(socket.AF_INET,      # задамем семейство протоколов 'Интернет' (INET)
                          socket.SOCK_STREAM,  # задаем тип передачи данных 'потоковый' (TCP)
                          proto=0)             # выбираем протокол 'по умолчанию' для TCP, т.е. IP
#print(type(s))
serv_sock.bind((IFACES, PORT))
serv_sock.listen(5)
while True:
    # Бесконечно обрабатываем входящие подключения
    client_sock, client_addr = serv_sock.accept()
    print('Connected by', client_addr)

    while True:
        # Пока клиент не отключился, читаем передаваемые
        # им данные и отправляем их обратно
        data = client_sock.recv(1024)
        print('CLEAR DATA: ', data, type(data))
        #print('CLEAR DATA2: ', data[0].decode(), type(data))
        #print('data', data.encode().decode('utf-8'))

        if not data:
            # Клиент отключился
            break
        try:
            result = dict(data=json.loads(data.decode('utf-8')), state=200) #.rstrip()
        except BaseException as exp:
            print('Error:', exp)
        client_sock.sendall(json.dumps(result).encode())

    client_sock.close()
