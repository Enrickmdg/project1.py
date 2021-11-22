*By Enrick MDG.*

## Disclaimer

This project is initiated in an educational framework for my M2 Networks & Cybersecurity Manager year.
Being public, I have to put a disclaimer for this project.
Therefore, I'm not responsible for the use of this script by a third party.

## Project

This repository contains the necessary files to launch an active recognition script written in python. 
The goal is to perform an active reconnaissance on a remote device (server, virtual machine...) in order to find a security hole and to exploit it. 
The script will also write in a text file the collected information.

Steps  :

 - NMAP scan
	 - Search for open ports
 - Scan for vulnerabilities
	 - Recovery of information in a txt file
 - Exploit scan
	 - Recovery of information from a txt file

## Requirements

Debian est recommandée, mais ce projet devrait fonctionner sur toute distribution basée sur Linux. Vous pouvez rencontrer quelques erreurs avec certaines distributions comme Ubuntu ou Kali, alors n'hésitez pas à me demander si vous avez des problèmes.

Vous aurez besoin d'installer ces outils :

L'AP est configuré avec le deamon Hostapd. Vous aurez également besoin de Dhcpd pour le DHCP et de Dnsmasq pour la résolution DNS. Enfin, le portail captif est hébergé sur Apache2 avec une base de données MySQL.

Assurez-vous d'avoir installé tous ces éléments avant de lancer le script.

## Configuration

See the "**config.conf**" in the "**conf**" folder.

## Ameliorations

Better script with more attack features.
