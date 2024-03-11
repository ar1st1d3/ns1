import socket

receveur = socket.socket(type=socket.SOCK_DGRAM)
receveur.bind(('localhost', 56789))
donnee, adress = receveur.recvfrom(1500)


print(f'{donnee = }')
print(f'{adress = }')
