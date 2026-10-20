import socket

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind(("10.9.0.6", 9090))

while True:
    data, (ip, port) = udp.recvfrom(1024)
    print('From {}:{}: {}'.format(ip, port, str(data, 'utf-8')))
    udp.sendto(b'hello back \n', (ip, port))
