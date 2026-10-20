
import socket

data = b'hello, Server\n'
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Starting...')
udp.sendto(data, ("10.9.0.6", 9090))

data, (ip, port) = udp.recvfrom(1024)
print('From {}:{}: {}'.format(ip, port, str(data, 'utf-8')))
