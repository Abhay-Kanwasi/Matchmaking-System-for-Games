import socket

# These things are under configuration which we match with other players
tries = int(input("How many tries you want : "))
max_number = int(input("Enter the maximum number : "))
role = input("Role (Gusser/Decider) : ")

# configuraiton
config_string = f"{tries}-{max_number}-{role}"


# Create the client and connect to local host
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1", 9999))


# When we connected to server firstly we send the configuration
client.send(config_string.encode())
# print whatever we get from the server
print(client.recv(1024).decode())

client.send(input().encode())

while True:
    message = client.recv(1024).decode()
    print(message)
    # Assuming that whenever game come to end these words are in the message
    if "tries" in message or "lost" in message or "Invalid" in message:
        break
    if role == "Guesser":
        client.send(input().encode())
        



