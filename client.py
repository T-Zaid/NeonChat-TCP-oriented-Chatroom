import socket
import threading

#Your Username
username = input("Enter username : ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))    #connect to the server via it's IP address and port

def receive():   #utility function that recieves messages from the server
    
    while True:
        try:
            message = client.recv(1024).decode('ascii')

            if message == "u_name" :    # A silent message from server asking it's username
                client.send(username.encode('ascii'))
            else :
                print(message)
        
        except:     #in case the server closes
            print("Error 69 : Server Time Out")
            client.close()
            break

def write():    #utility function to write a new message
    while True:
        text = input("")
        messageFormat = "{} : {}".format(username, text)
        client.send(messageFormat.encode('ascii'))


receiver = threading.Thread(target=receive)
receiver.start()
writer = threading.Thread(target=write)
writer.start()