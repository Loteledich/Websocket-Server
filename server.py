import socket
import json
import logging
logging.basicConfig(filename='logs.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s:')
logging.info("Server starts")

HOST = '192.168.0.40'
PORT = 33000
BUFFER = 1024
clients = []
try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(2)

    try:
        while True:
            client_socket, address = server_socket.accept()
            print(f"Received connection from {address}")
            logging.info('received connection from: ' + str(address))
            message = client_socket.recv(BUFFER).decode("utf8")
            data = json.loads(message)
            userid=data['data']

            if data['code'] == 'login':
                clients.append(userid)
                data['code'] = 'login_res'
                data['data'] = {"logged_in": "true", "id":userid['id']}
            elif data['code'] == 'logout':
                clients.remove(userid['id'])
                data['code'] = 'logout_res'
                data['data'] = {"logged_in": "false", "id":userid['id']}
            elif data['code'] == 'get_all_logged_in_clients':
                data['code'] = 'get_all_logged_in_clients_res'
                data['data'] = {"client_list": clients}
            else:
                logging.critical("WRONG CODE")

            answer = str(str(data).replace("\'", "\""))
            client_socket.send(str.encode(answer))  # .encode("utf8")

    except KeyboardInterrupt:
        logging.critical("Server has been interrupted")
except Exception as e:
    print("Error: Could be anything but most probably port is already used. Terminate client.py")
    logging.critical("Client is blocking PORT")