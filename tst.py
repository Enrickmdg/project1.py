#!/usr/bin/python3

import socket
import re, uuid

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Le nom de la machine est : " + hostname)
print("L'adresse IP de la machine est : " +IPAddr)

print("L'adresse MAC de la machine est : ", end="")
print(':'.join(re.findall('..', '%012x' %uuid.getnode())))
