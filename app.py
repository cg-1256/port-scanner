import socket
import sys

host = input("Enter host address: ")
while True:
    try:
        low=int(input("Enter the low bound of ports to scan: "))
        break
    except ValueError:
        print ("Invalid port number")

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