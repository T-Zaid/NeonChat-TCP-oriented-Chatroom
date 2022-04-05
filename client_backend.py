import socket
import threading
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

#Your Username
# username1 = None
# client1 = None
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(('127.0.0.1', 55555))    #connect to the server via it's IP address and port

def receive(client, username, recvbox):   #utility function that recieves messages from the server
    while True:
        try:
            message = client.recv(1024).decode('ascii')

            if message == "u_name" :    # A silent message from server asking it's username
                client.send(username.encode('ascii'))
            else :
                # print(message)
                recvbox.append(message + "\n")
        
        except:     #in case the server closes
            print("Error 69 : Server Time Out")
            client.close()
            break

def write(text, client1, username1):    #utility function to write a new message
    messageFormat = "{} : {}".format(username1, text)
    client1.send(messageFormat.encode('ascii'))


# receiver = threading.Thread(target=receive)
# receiver.start()
# writer = threading.Thread(target=write)
# writer.start()