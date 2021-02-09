import socket
import json

HOST = '192.168.0.109'
PORT = 33000
BUFFER = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))

name = input('Your name: ').encode("utf8")
client_socket.send(name)
print( client_socket.recv(BUFFER).decode("utf8"))