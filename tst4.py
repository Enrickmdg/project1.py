#!/usr/bin/python3

# Pour flex
import pyfiglet

# Pour connaître les interfaces réseaux présentes sur la machine
import netifaces

# Pour importer le module nmap
import nmap

# Pour importer les différents sockets
import socket

# Pour l'@ MAC
import re, uuid

# Pour le temps de scan
import time

print("\n########################################################################################")
print("\n########################################################################################")

ascii_banner = pyfiglet.figlet_format("CREER PAR ENRICK MDG.")
print(ascii_banner)

print("\nBienvenue sur mon scirpt de reconnaissance reseau.")

print("\n########################################################################################")
print("\n########################################################################################")

###################################################################################################
# Les variables :                                                                                 #
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sc = nmap.PortScanner()
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
#                                                                                                 #
###################################################################################################

###################################################################################################
# Tout d'abord on commence par présenter la machine et ses interfaces réseau.

print("Le nom de la machine est : " + hostname)
print("L'adresse IP de la machine est : " + IPAddr)

print("L'adresse MAC de la machine est : ", end="")
print(':'.join(re.findall('..', '%012x' % uuid.getnode())))

netifaces.gateways()

interfaces = netifaces.interfaces()
for interface in interfaces:
    print("Les interfaces réseaux de la machine sont : ", interface)

###################################################################################################
# La prochaine étape est de demander à l'utilisateur l'IP, la plage ou le réseau entier à scanner.

ipaddr = input("Svp veuillez entrer une IP, une plage ou un réseau à scanner : ")
print("L'IP, la plage ou le réseau que vous avez entrer est : ")
type(ipaddr)

###################################################################################################
# Ensuite on demande à l'utilisateur le type de scan qu'il veut effectuer

resp = input("""\nSvp entrez le type de scan à effectuer
                1) Scan SYN ACK
                2) Scan UDP
                3) Scan Comprehensive \n""")
print("Vous avez sélectionner l'option : ", resp)

tps = time.time()

if resp == '1':
    print("Nmap Version : ", sc.nmap_version())
    sc.scan(ipaddr, '1-1024', '-v -sS')
    print(sc.scaninfo())
    print("Ip Status : ", sc[ipaddr].state())
    print(sc[ipaddr].all_protocols())
    print("Open Ports : ", sc[ipaddr]['tcp'].keys())
    print("Le Scan s'est déroulé en : ", time.time() - tps)

elif resp == '2':
    print("Nmap Version : ", sc.nmap_version())
    sc.scan(ipaddr, '1-1024', '-v -sU')
    print(sc.scaninfo())
    print("Ip Status : ", sc[ipaddr].state())
    print(sc[ipaddr].all_protocols())
    print("Open Ports : ", sc[ipaddr]['udp'].keys())
    print("Le Scan s'est déroulé en : ", time.time() - tps)

elif resp == '3':
    print("Nmap Version : ", sc.nmap_version())
    sc.scan(ipaddr, '1-1024', '-v -sS -sV -sC -A -O')
    print(sc.scaninfo())
    print("Ip Status : ", sc[ipaddr].state())
    print(sc[ipaddr].all_protocols())
    print("Open Ports : ", sc[ipaddr]['tcp'].keys())
    print("Le Scan s'est déroulé en : ", time.time() - tps)

elif resp >= '4':
    print("L'option sélectionée est invalide. Svp, choisissez parmis les 3 options disponibles")