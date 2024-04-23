import socket, sys, os
from datetime import datetime
 
current_dir = os.getcwd()
date = datetime.now()
dir_addition = "port_scan_"+str(date)
new_dir = os.path.join(current_dir, dir_addition)
os.mkdir(new_dir)

open_file = new_dir+"/open_ports.txt"
closed_file = new_dir+"/closed_ports.txt"

host = input("Enter host address: ")
low = -1
high = -1

while low==-1 or low>65534:
	while True:
		try:
			low=int(input("Enter the low bound of ports to scan: "))
			break
		except ValueError:
			print ("Invalid port number")

while high==-1 or high>65536 or high<=low:
	while True:
		try:
			high=int(input("Enter the high bound of ports to scan: "))+1
			break
		except ValueError:
			print ("Invalid port number")

try:
    
	for port in range(low, high):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)

		result = sock.connect_ex((host,port))
		if result == 0:
			print("[+] Port {} is open".format(port))
			with open(open_file, 'a') as file:
				file.write("[+] Port {} is open\n".format(port))
		else:
			with open(closed_file, 'a') as file:
				file.write("[-] Port {} is closed\n".format(port))
		sock.close()
except KeyboardInterrupt:
	print("\nExiting program...")
	sys.exit()
except socket.gaierror:
	print("\nHostname Could Not Be Resolved")
	sys.exit()
except socket.error:
	print("\nServer Not Responding")
	sys.exit()