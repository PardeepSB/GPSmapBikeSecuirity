import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("IPv4 from ipconfig", PortNumber))

while(True):
    data = input('send to server: ')
    client_socket.send(data.encode())
