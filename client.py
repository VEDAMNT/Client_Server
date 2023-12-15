import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            print(message)
        except Exception as e:
            print(f"Error: {e}")
            break

# Client setup
host = "127.0.0.1"
port = 5555

username = input("Enter your username: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# Send username to the server
client.send(username.encode("utf-8"))

# Start a thread to receive messages
receive_thread = threading.Thread(target=receive_messages, args=(client,))
receive_thread.start()

# Main loop to send messages
while True:
    message = input()
    client.send(message.encode("utf-8"))
