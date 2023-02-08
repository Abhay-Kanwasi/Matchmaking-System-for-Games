import socket
import threading

# Server is an TCP Socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",9999)) # bind the sever to local host

server.listen() # Listen for incoming connections

connected_clients = []
def handle_match(client1,client2):
    client1.send("MATCH".encode())
    client2.send("MATCH".encode())
    
def handle_client(client):
    client.send("Enter matching string : ".encode())
    matching_string = client.recv(1024).decode()
    found_match = False
    for i in range(len(connected_clients)):
        if connected_clients[i][1] == matching_string:
            threading.Thread(target=handle_match, args = (client,connected_clients[i][0])).start()
            del connected_clients[i]
            found_match = True # So if we once found match it will stored in already matched string.

    if not found_match:
        connected_clients.append((client,matching_string))



while True:
    client, addr = server.accept()
    threading.Thread(target=handle_client, args=(client,)).start()
