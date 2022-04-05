import threading
import socket
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

hostIP = '127.0.0.1'
port = 55555
clients = []    #client IP address
usernames = []  #client username

def broadcast(message):     #Utility to broadcast message to all clients
    # print(message.decode('ascii'))
    for client in clients:
        client.send(message)

def manage(client, recvbox):     #recieving every messages and broadcasting, incase user leaves, so broadcast
                        #and close that client connection.
    while True:
        try:
            message = client.recv(50)   #only 50 peoples are allowed in chatroom. Tentative!
            recvbox.append(message.decode('ascii') + "\n")
            broadcast(message)
        except:
            client_num = clients.index(client)
            u_name = usernames[client_num]
            clients.remove(client)
            usernames.remove(u_name)

            broadcast("{} has left the chat".format(u_name).encode('ascii'))
            client.close()
            break

def write(text, recvbox):       #Utility function to write any message from Server
    
    messageFormat = "Server : {}".format(text)
    recvbox.append(messageFormat + "\n")
    broadcast(messageFormat.encode("ascii"))

def recieve(server, recvbox):  #Kinda main func that will accept the client to chatroom

    while True:
        client, address = server.accept()
        
        #asks for the client username
        client.send('u_name'.encode('ascii'))   #'u_name' is a secret message to client asking its username
        u_name = client.recv(50).decode('ascii')
        usernames.append(u_name)
        clients.append(client)

        print("{} : {} has joined the server".format(address, u_name))
        broadcast("{} has joined the chat".format(u_name).encode('ascii'))
        client.send("You have successfully joined the chat group".encode('ascii'))

        #Two thread running simulataneously for manage and write functions
        manager = threading.Thread(target=manage, args=(client, recvbox))
        manager.start()
        # writer = threading.Thread(target=write)
        # writer.start()



#AF_INET : using an internet socket
#SOCK_STREAM : using TCP
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind((hostIP, port))
# server.listen()
# server = None
# recieve()