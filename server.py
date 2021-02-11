import socket
import json
import ast

HOST = '192.168.0.40'
PORT = 33001
BUFFER = 1024
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(2)

clientsy = ['Admin']

while True:
    client_socket, address = server_socket.accept()
    print(f"Received connection from {address}")

    message = client_socket.recv(BUFFER).decode("utf8")
    # json_data = ast.literal_eval(json.dumps(message))
    # print(json_data)

    data = json.loads(message)
    userid=data['data']

    if data['code'] == 'login':
        print("itsworkingxD")
        data['code'] = 'login_res'
        data['data'] = {"logged_in": "true", "id":userid['id']}

    #elif data['code'] == 'logout':
    #elif data['code'] == 'get_all_logged_in_clients':
    answer = str(str(data).replace("\'", "\""))
    client_socket.send(str.encode(answer))  # .encode("utf8")
