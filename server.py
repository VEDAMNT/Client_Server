import socket
import threading

def handle_client(client_socket, username):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                print(f"{username} has left the chat.")
                break
            print(f"{username}: {message}")
            broadcast(f"{username}: {message}", client_socket)
        except Exception as e:
            print(f"Error: {e}")
            break

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode("utf-8"))
            except Exception as e:
                print(f"Error: {e}")
                clients.remove(client)

# Server setup
host = "127.0.0.1"
port = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

print(f"Server listening on {host}:{port}")

clients = []

while True:
    client_socket, client_address = server.accept()
    username = client_socket.recv(1024).decode("utf-8")
    clients.append(client_socket)
    print(f"{username} has joined the chat.")

    # Start a thread to handle the new client
    client_handler = threading.Thread(target=handle_client, args=(client_socket, username))
    client_handler.start()
