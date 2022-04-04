# from http import server
import threading
import socket

hostIP = '127.0.0.1'
port = 55555
clients = []    #client IP address
usernames = []  #client username

def broadcast(message):
    for client in clients:
        client.send(message)

def send(client):

    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            client_num = clients.index(client)
            u_name = usernames[client_num]
            clients.remove(client)
            usernames.remove(u_name)

            broadcast("{} has left the chat".format(u_name).encode('ascii'))
            client.close()
            break

def recieve():

    while True:
        client, address = server.accept()
        #asks for the client username
        client.send('u_name'.encode('ascii'))
        u_name = client.recv(1024).decode('ascii')
        usernames.append(u_name)
        clients.append(client)

        broadcast("{} has joined the chat".format(u_name).encode('ascii'))
        client.send("You have successfully joined the chat group".encode('ascii'))

        thread = threading.Thread(target=send, args=(client,))
        thread.start()


#AF_INET : using an internet socket
#SOCK_STREAM : using TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((hostIP, port))
server.listen()

recieve()
