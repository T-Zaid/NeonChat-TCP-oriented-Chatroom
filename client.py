from email import message
from pydoc import cli
import socket
import threading

username = input("Enter username : ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')

            if message == "u_name" :
                client.send(username.encode('ascii'))
            else :
                print(message)
        
        except:
            print("Error 69")
            client.close()
            break

def write():
    while True:
        text = input("")
        messageFormat = "{} : {}".format(username, text)
        client.send(messageFormat.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()