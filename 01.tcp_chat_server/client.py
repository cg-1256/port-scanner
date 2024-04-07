import socket
import threading

username = input("Please enter your username: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1',1031))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message=="NICK":
                client.send(username.encode('ascii'))
            else:
                print(message)
        except:
            print("There has been an error")
            client.close()
            break

def write():
    while True:
        message = f'{username}: {input("")}'
        client.send(message.encode('ascii'))
        
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()