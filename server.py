import socket
import json
import users


HOST = '192.168.0.40'
PORT = 33000
BUFFER = 1024
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(2)

clientsy = ['Admin']
clients = '''
{
    "users": [
     {
        "id": "Olaf",
        "password": "ABC"
     },
     {
         "id": "Admin",
         "password": "Admin"
     }
    ]
}
'''
data = json.loads(clients)
print(data)

while True:
    client_socket, address = server_socket.accept()
    print(f"Received connection from {address}")

    name = client_socket.recv(BUFFER).decode("utf8")
    if name in clientsy:
        print(f"{name} joined server")
    elif name not in clientsy:
        print(f"New user joined server - {name}")
        clientsy.append(name)

    msg = f"Welcome, {name}".encode("utf8")
    client_socket.send(msg)
