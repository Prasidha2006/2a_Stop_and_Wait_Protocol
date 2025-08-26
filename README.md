# 2a_Stop_and_Wait_Protocol
## AIM 
To write a python program to perform stop and wait protocol
## ALGORITHM
1. Start the program.
2. Get the frame size from the user
3. To create the frame based on the user request.
4. To send frames to server from the client side.
5. If your frames reach the server it will send ACK signal to client
6. Stop the Program
## PROGRAM

### server.py:
# server.py

```
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
```

### client.py

```
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

```

## OUTPUT

### server.py

![alt text](<Screenshot 2025-08-21 160316-1.png>)

### client.py

![alt text](<Screenshot 2025-08-21 160304.png>)

## RESULT
Thus, python program to perform stop and wait protocol was successfully executed.
