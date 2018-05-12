import os
import subprocess
import string 
from ponto1 import *

def user_input():
	global gama_ip, fqdn, ip, zone, reverse, resolv_dns
	gama_ip = input("Insira o IP para a zona reverse: ")
	fqdn = input("Insira o FQDN: ")
	ip = input("Insira o IP para o FQDN: ")

	zone = 'zone "'+gama_ip+'.in-addr.arpa" IN { \n	type master;\n	file "/var/named/reverse.'+fqdn+'";\n};'

	reverse = '$TTL 38400\n@	IN	SOA	@ root(\n			100;\n			10800;\n			3600;\n			684000;\n			38400;\n			)\n	IN	NS	trabalho.pt.\n'+ip+'	IN	PTR	'+fqdn+'.\n'

	resolv_dns = "search projecto.pt\nnameserver 127.0.0.1"

def write_reverse():
	file = open("/etc/named.conf").read()
	if gama_ip not in file:
		create_zone(zone, gama_ip)

subprocess.check_call("service named restart".split())

if __name__ == '__main__':
	os.system("rpm -qa > installedPackages.txt")
	packageList = open("installedPackages.txt").read()
	if "bind" not in packageList:
		os.system("yum install bind* -y")
	user_input()
	write_reverse()
	change_resolv_file(resolv_dns)
	replace_lines()
	restart_named()