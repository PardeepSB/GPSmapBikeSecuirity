import socket
import sys

import pandas as pd
 
host = 'IPv4 from ipconfig'
port = PortNumber
address = (host, port)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(address)
server_socket.listen(5)

print ("Listening for client . . .")
conn, address = server_socket.accept()
print ("Connected to client at ", address)
#pick a large output buffer size because i dont necessarily know how big the incoming packet is                                                    
while True:
    output = conn.recv(2048);
    if output.strip() == "disconnect":
        conn.close()
        sys.exit("Received disconnect message.  Shutting down.")
        
    elif output:
        print ("Message received from client:")
        print (output.decode())
        f = open("Coordinates.csv", "w")
        saving = str(output).strip('b').strip("'").replace(" ", "")
        f.write(saving)
        f.close


        # conn.send("dack".encode())
        # conn.send("ack".encode())
        