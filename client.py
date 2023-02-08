# Start making this project
import socket
# Use AF_INET socket to make it internet socket and SOCK_STREAM to make it TCP internet socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to local host and connect on port 9999
client.connect(("127.0.0.1",9999)) 

# Receive message from the server
print(client.recv(1024).decode())

# We send here whatever user wants to enter in command line then we encode whatever we enter
client.send(input().encode())
print(client.recv(1024).decode()) # So that we can recieve match message