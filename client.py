import socket
import json
import random

HOST = '192.168.0.40'
PORT = 33000
BUFFER = 1024
yourid = str(random.randint(11111111,99999999))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))

message = '''
{   

}
'''
data = json.loads(message)

id = []
id.append(yourid)

data['code'] = input('Code: ')
data['data'] = {"id": yourid}
dataSEND = str(str(data).replace("\'", "\""))

client_socket.send(str.encode(dataSEND))
print( client_socket.recv(BUFFER).decode())