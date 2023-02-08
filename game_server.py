import socket
import threading

# Server is an TCP Socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",9999)) # bind the sever to local host

server.listen() # Listen for incoming connections

connected_clients = []

def handle_match(client1,client2):
    tries, max_num = client1[1].split("-")
    tries, max_num = int(tries), int(max_num)
    if client1[2] != "Decider":
        #[2] means role
        client1,client2 = client2, client1

    client1[0].send("Enter the nubmer to be guessed: ".encode())
    number = int(client1[0].recv(1024).decode())

    if number > max_num:
        client1[0].send("Invalid Request!".encode())
        client2[0].send("Your partner messed up things! Invalid range ! ".endcode())
        client1[0].close()
        client2[0].close()
    else:
        guessed = False
        try_counter = 0
        client2[0].send("Enter the guess: ".encode())
        while not guessed:
            try_counter+=1
            guess = int(client2[0].recv(1024).decode())
            if guess == number:
                client2[0].send(f"Correct! It took you {try_counter} tries.".encode())
                client1[0].send(f"Your partner guessed correctly after {try_counter} tries.".encode())
                client1[0].close()
                client2[0].close()
                guessed = True
            else:
                if try_counter >= tries:
                    client2[0].send(f"You lost mann! The number was {number}".encode())
                    client1[0].send(f"You partner lost mann! The number was {number}".encode())
                    client1[0].close()
                    client2[0].close()
                    break
                else:
                    if guess < number:
                        client2[0].send("Your guess is too low. Try again : ".encode())
                        client1[0].send(f"Your partner guessed {guess}".encode())
                    elif guess > number:
                        client2[0].send("Your guess is too high. Try again : ".encode())
                        client1[0].send(f"Your partner guessed {guess}".encode())


def handle_client(client):
    config_string = client.recv(1024).decode()
    config = config_string[:config_string.rfind("-")]
    role = config_string[config_string.rfind("-")+ 1:]
    found_match = False
    for i in range(len(connected_clients)):
        if connected_clients[i][1] == config:
            if connected_clients[i][2] == role: # We can't match in the same role
                print("MATCH")
                threading.Thread(target=handle_match, args = ((client,config,role),connected_clients[i])).start()
                del connected_clients[i]
                found_match = True # So if we once found match it will stored in already matched string.
                break

    if not found_match:
        connected_clients.append((client,config,role))



while True:
    client, addr = server.accept()
    threading.Thread(target=handle_client, args=(client,)).start()