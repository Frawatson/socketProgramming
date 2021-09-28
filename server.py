"""
Programmer : Francis Watson
Program Description: This program create a server and client using Transmission Control Protocol and IPv4.
Date : 09/23/2021
Last Changed:09/27/2021
"""
import socket

# using default par (ipv4, tcp)
server = socket.socket()
print("Server socket created")

# binding ipaddress and port
server.bind(('localhost', 9999))

# server connected to 3 clients at a given time
server.listen(3)
print("server waiting for connection")

while True:
    # retrieving client and it's ip
    client, ipaddress = server.accept()
    # receiving data from clients
    name = client.recv(1024).decode()
    print("Server is now connected with ", ipaddress, name)
    # sending data to client
    client.send(bytes("you're now connected with the server", "utf-8"))
    # close connection
    client.close()
