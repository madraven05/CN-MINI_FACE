from Backend.server import Server
import socket

host = socket.gethostname()
PORT = 12345

server = Server(PORT=PORT, host=host)

server.create_server_socket()
server.bind_server_socket()
server.server_socket_listen()

server.connect_to_clients()