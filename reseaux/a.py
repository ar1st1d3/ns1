import socket

donnee = b'OBEY THE PUG'

emmeteur = socket.socket(type=socket.SOCK_DGRAM)
emmeteur.sendto(donnee,('localhost', 56789))
