import os
import subprocess
from ponto1 import *

resolv_dns_file = "search trabalho.pt\nnameserver 127.0.0.1"
zone_forward = '\nzone '+dominio_input+' IN { \n	type master;\n	file "/var/named/'+dominio_input+'.hosts";\n};'

def input_register():
	
	register_input = raw_input("Tipo de registo (A ou MX): ").upper()
	
	if register_input not in ('A', 'MX'):
		print('Input Invalido')
		input_register()

def register_type(register):
	if register == 'MX':
   		host = '\n        IN      MX      10      smtp.'+dominio_input
	elif register == 'A':
		prefixo = raw_input("Insira o prefixo: ")
		ip = raw_input("Insira o IP: ")
		host = '\n'+prefixo+'	IN      A       '+ip
	with open("/var/named/"+dominio_input+".hosts", "a") as myfile:
		myfile.write(host)

def check_zone_create_register(zone):
	file = open("/etc/named.conf").read()
	if dominio_input in file:
		register_type(register_input)
	else:
		create_zone(zone_forward, dominio_input)
		create_hosts_file(dominio_input, hosts_file)
		register_type(register_input)
	restart_named()
	
if __name__=='__main__':
	os.system("rpm -qa > installedPackages.txt")
	packageList = open("installedPackages.txt").read()
	if "bind" not in packageList:
		os.system("yum install bind * -y")

	domain_input_zone_forward()
	input_register()
	replace_lines()
	write_resolv_file(resolv_dns_file)
	check_zone_create_register(zone_forward)