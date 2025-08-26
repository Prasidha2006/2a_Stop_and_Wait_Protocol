# server.py
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Server is waiting for a connection...")

conn, addr = server_socket.accept()
print(f"Connected to client at {addr}")

while True:
    data = conn.recv(1024).decode()  
    if not data:
        break
    print(f"Server received: {data}")

    conn.send("ACK".encode())
    print("ACK sent")

conn.close()
print("Connection closed.")
