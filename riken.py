#!/usr/bin/python3

import nmap
import os

sc = nmap.PortScanner()

print("\n****************************************************************************************")
print("\n****************************************************************************************")

print("""__________          ___________            .__        __    \n
\______   \___.__.  \_   _____/ ___________|__| ____ |  | __ \n
 |    |  _<   |  |   |    __)_ /    \_  __ \  |/ ___\|  |/ / \n
 |    |   \\___  |   |        \   |  \  | \/  \  \___|    <  \n
 |______  // ____|  /_______  /___|  /__|  |__|\___  >__|_ \ \n
        \/ \/               \/     \/              \/     \/ \n""")


print("\nBienvenue sur mon scirpt de reconnaissance reseau.")

print("\n****************************************************************************************")
print("\n****************************************************************************************")

def main():
    n = input("1 - Network scanner\n2 - Vulnerabilities Detection\n3 - Exploit \n\nSvp choisissez une option : ")
    if n == '1':
        nmap()

    if n == '2':
        vuln()

    if n == '3':
        os.system('msfconsole')

    else :
        print("Option selectionnee invalide. Svp choisissez une option entre 1 et 3.")

def nmap():
    print("*****************************************************************************")
    print("********************Vous Avez Selectionner Le Scan Reseau********************")
    print("*****************************************************************************")
    ip = input("\nSvp entrez une adresse IP:")
    sc.scan(ip , '1-1024')
    print(sc.scaninfo())
    print(sc[ip]['tcp'].keys())

def vuln():
    print("*********************************************************************************************")
    print("********************Vous Avez Selectionner La Detection De Vulnerabilites********************")
    print("*********************************************************************************************")
    ip = input("\nSvp entrez une adresse IP: ")
    print(os.system('nmap -sV --script=vulscan.nse' +ip))

if __name__ == '__main__':
    main()
