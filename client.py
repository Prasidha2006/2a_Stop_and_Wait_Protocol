# client.py
import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

frame_count = int(input("Enter the number of frames to send: "))

for i in range(1, frame_count + 1):
    frame = f"Frame {i}"
    print(f"Sending: {frame}")
    client_socket.send(frame.encode())

    ack = client_socket.recv(1024).decode()
    print(f"Received from server: {ack}")

    time.sleep(1)

client_socket.close()
print("Client finished sending frames.")
