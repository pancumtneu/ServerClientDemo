
import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket Created')
host = '58.154.208.35'
port = 6666
try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()
print('Ip address of ' + host + ' is ' + remote_ip)
s.connect((host, port))
print('Socket Connected to ' + host + ' on ip ' + remote_ip)
message= ("hello server")
try:
    s.send(message.encode())
except socket.error:
    print('Send failed')
    sys.exit()
print('Message send successfully')
reply = s.recv(4096)
print(reply.decode())
