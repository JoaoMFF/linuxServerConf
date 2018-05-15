import os
import subprocess
import string 

def delete_zone_forward():
    dominio_to_delete = raw_input("Insira  o dominio a eliminar: ")

    zone_forward = '\nzone '+dominio_to_delete+' IN { \n	type master;\n	file "/var/named/'+dominio_input+'.hosts";\n};'

    file = open("/etc/named.conf").read()
    with open("/etc/named.conf", "a") as myfile:
        for line in file:
            myfile.write(line.replace(zone_forward, ''))
        else:
            print("Dominio nao encontrado")
            delete_zone_forward()

    os.system("rm -f /var/named/"+dominio_to_delete+".hosts")

def input_switch():

    selection = input("Insert an option: \n1 - Delete Zone Forward\n2 - Delete Zone Reverse\n3 - Delete VirtualHosts\n")
    
    if selection == '1':
        delete_zone_forward()
    elif selection == '2':
        print("Opção a")
    elif selection == '3':
        print("Opção b")
    else:
        print("Input inválido")
        input_switch()

if __name__ == '__main__':

	input_switch()