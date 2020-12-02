from Backend.server import ClientThread
import socket
from threading import Thread
host = socket.gethostname()
PORT = 12345
threads= []
server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, PORT))




while True:
    server_socket.listen(5)
    print("Waiting for clients to connect...")
    client,(ip,port)=server_socket.accept()
    print(f"Got connection from {(ip,port)} ")
    new=ClientThread(ip,port,client)
    new.start()
    threads.append(new)
    
for t in threads:
    t.join()