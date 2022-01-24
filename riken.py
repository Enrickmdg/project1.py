#!/usr/bin/python3
#pip3 install python-nmap

import nmap
import os
sc = nmap.PortScanner()

print("\n****************************************************************************************")

print("""__________         ___________            .__        __    \n    
\______   \___.__. \_   _____/ ___________|__| ____ |  | __
 |    |  _<   |  |  |    __)_ /    \_  __ \  |/ ___\|  |/ /         \n
 |    |   \\___  |  |        \   |  \  | \/  \  \___|    <          \n
 |______  // ____| /_______  /___|  /__|  |__|\___  >__|_ \         \n
        \/ \/              \/     \/              \/     \/         \n""")

print("\n****************************************************************************************")
print("\n* By Enrick Mondongue, 2022\n* https://github.com/Enrickmdg")
print("\n****************************************************************************************")

def main():
    n = input("1 - Network scanner\n2 - Vulnerabilities Detection\n3 - Exploit \n\nPlease choose the option you want : ")
    if n == '1':
        nmap()

    if n == '2':
        vuln()

    if n == '3':
        os.system('msfconsole')

    else :
        print("There is no valid option with the command you entered. Please choose a number between 1 and 3.")

def nmap():
    print("********************Welcome to the Network Scanner********************")
    print("**********************************************************************")
    ip = input("\nPlease enter one IP address:")

def vuln():
    print("********************Welcome to the Vulnerabilites Detection********************")
    print("*******************************************************************************")
    ip = input("\nPlease enter the IP address: ")
    print(os.system('nmap -sV --script=vulscan.nse' +ip))

if __name__ == '__main__':
    main()