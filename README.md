# NeonChat-TCP-oriented-Chatroom
A TCP oriented chatroom that utilizes the libraries of socket and threading.

A user-friendly GUI has been implemented for smoother and seamless experience of users.

## Required Libraries
1) Socket -> for connection between server and client.
2) Threading -> for managing multiple process simulataneously.
3) PySide2 -> for GUI purpose.

NOTE : The first and second library are mostly installed by default.
TIP : To install PySide : Run this in terminal -> `py -m pip install PySide2`

## How to Run:
1) Run serverUI by typing "py serverUI.py" in cmd.
2) Enter IP and port and click on start listening
3) Run clientUI by typing "py clientUI.py" in cmd.
4) Enter just the IP address and a nickname/username to be used during the chat.
5) Click on connect.
6) Start Chatting.

## Demo Picture:
![Server Chatting wih two Clients](https://user-images.githubusercontent.com/75293628/161961300-d064e987-ba48-4f05-8085-2df9b859f233.png)

This picture contains the working example of a Server that initiated a chatroom by entering the IP and port. A new client (by name of "Tiger") has joined the chat. Server and client can with other. Upto 50 clients can connect to this server's chatroom. Make sure to give yourself a username!
