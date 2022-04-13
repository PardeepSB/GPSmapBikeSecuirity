import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("207.23.214.101", 8220))

while(True):
    data = input('send to server: ')
    client_socket.send(data.encode())
