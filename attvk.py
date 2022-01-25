#!/usr/bin/python3

# Pour la machine
import ipaddress
import os
import re
# Pour importer les différents sockets
import socket
import sys
# Pour le temps de scan
import time
import uuid
# Pour importer Exploit-db
from optparse import OptionParser
from urllib.request import urlopen

# Pour connaître les interfaces réseaux présentes sur la machine
import netifaces
# Pour importer le module nmap
import nmap
# Pour flex
import pyfiglet

# Enregistrement csv

print("\n########################################################################################")
print("\n########################################################################################")

ascii_banner = pyfiglet.figlet_format("CREER PAR ENRICK MDG.")
print(ascii_banner)

print("\nBienvenue sur mon scirpt de reconnaissance reseau.")

print("\n########################################################################################")
print("\n########################################################################################")

###################################################################################################
# On commence par présenter la machine  et ses interfaces réseau.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Le nom de la machine est : " + hostname)
print("L'adresse IP de la machine est : " + IPAddr)

print("L'adresse MAC de la machine est : ", end="")
print(':'.join(re.findall('..', '%012x' % uuid.getnode())))

netifaces.gateways()

interfaces = netifaces.interfaces()
for interface in interfaces:
    print("Les interfaces réseaux de la machine sont : ", interface)

###################################################################################################
# Le script nous donne directement toutes les IP disponibles sur le réseau.

net4 = ipaddress.ip_network('192.168.100.0/24')
for x in net4.hosts():
    print(x)

###################################################################################################
# On choisit ensuite une IP parmis celle disponible sur le réseau.

ipaddr = input("Svp veuillez entrer une IP du réseau à scanner : ")
print("L'IP que vous avez entrer est : " + ipaddr)
type(ipaddr)

###################################################################################################
# Ensuite on demande à l'utilisateur le type de scan qu'il veut effectuer

sc = nmap.PortScanner()

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
    print("Open Ports : ", sc[ipaddr].keys())
    print("Le Scan s'est déroulé en : ", time.time() - tps)

elif resp == '2':
    print("Nmap Version : ", sc.nmap_version())
    sc.scan(ipaddr, '1-1024', '-v -sU')
    print(sc.scaninfo())
    print("Ip Status : ", sc[ipaddr].state())
    print(sc[ipaddr].all_protocols())
    print("Open Ports : ", sc[ipaddr].keys())
    print("Le Scan s'est déroulé en : ", time.time() - tps)

elif resp == '3':
    print("Nmap Version : ", sc.nmap_version())
    sc.scan(ipaddr, '1-1024', '-sC -A -O -v -sS -sV')
    print(sc.scaninfo())
    print("Ip Status : ", sc[ipaddr].state())
    print(sc[ipaddr].all_protocols())
    print("Open Ports : ", sc[ipaddr].keys())
    print("Le Scan s'est déroulé en : ", time.time() - tps)

elif resp >= '4':
    print("L'option sélectionée est invalide. Svp, choisissez parmis les 3 options disponibles")

###################################################################################################
# On importe Exploit-db

options = OptionParser(usage='%prog number_of_dorks [options]', description='Exploit-db.Com GHDB Database Replicator')
options.add_option('-s', '--start_number', type='int', default=51, help='Dork number to start with (default: 5)')
options.add_option('-o', '--output_file', type='string', default="output.txt",
                   help='Name of the output file.  Paths accepted. User must have access to output path. (default: '
                        'output.txt)')

opts, args = options.parse_args()
if len(args) < 1:
    options.print_help()
    exit()

dorkData = []
output = ""
log_file = open(opts.output_file, "a")

if os.name == 'nt':
    os.system('color a')
    os.system('cls')
else:
    os.system('clear')

max_range = int(args[0]) - opts.start_number
failed_atempts = 0
for page in range(int(opts.start_number), int(max_range)):  # 3943 Max Results

    print('Grabbing ' + 'http://www.exploit-db.com/ghdb/' + str(page) + '/')
    print('========================================================================')
    search_url = urlopen('http://www.exploit-db.com/ghdb/' + str(page) + '/')
    search_url.add_header('User-agent',
                          'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5')

    try:
        search_response = urlopen(search_url, timeout=6)
        search_content = search_response.read()
        dork = re.findall('<h1>(.*?)</h1>', search_content)
        date_added = re.findall('<p>Submited: (.*?)</p>', search_content)
        dork_desc = re.findall('<p class="text">(.*?)</p>', search_content)

        print('Checking response')
        try:
            var = dork[0]

            try:
                date_added[0]
            except:
                date_added.append("0000-00-00")

            try:
                dork_desc[0]
            except:
                dork_desc.append("na")

            log_file.write(dork[0] + "," + date_added[0] + "," + dork_desc[0] + "\n")
            failed_attempts = 0

        except:
            print('Communication error.  Waiting 3 seconds.')
            time.sleep(3)
            pass

        search_response.close()
    except:
        print('Connection interrupted.  Waiting 5 Seconds.')
        failed_attempts = failed_attempts + 1
        time.sleep(5)
        if failed_attempts == 3:
            print('Connection lost.  Exiting.')
            log_file.close()
            exit()

log_file.close()





