import socket
import sys

HOST = ''
PORT = 6666
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

try:
    s.bind((HOST, PORT))
except socket.error:
    print('Bind failed.')
    sys.exit()
print('Socket bind complete')
s.listen(10)
print('Socket now listening')
conn, addr = s.accept()
print('Connected with ' + addr[0] + ':' + str(addr[1]))
received_mes = conn.recv(4096)
print(received_mes.decode())
data = 'received successfully'
conn.sendall(data.encode())
