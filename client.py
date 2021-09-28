"""
Programmer : Francis Watson
Program Description: This program create a server and client using Transmission Control Protocol and IPv4.
Date : 09/23/2021
Last Changed:09/27/2021
"""
import socket

# create client socket using default par (ipv4, tcp)
client = socket.socket()
# connecting to the server with given ip and port number
client.connect(('localhost', 9999))
# asking for host name
name = input("Enter your host name")
# sending the data to server
client.send(bytes(name, 'utf-8'))
# receiving the data from server
print(client.recv(1024).decode())
