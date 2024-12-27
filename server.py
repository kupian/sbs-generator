import socket
import time

PORT = 30003

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', PORT))
sock.listen()

while True:
    conn, addr = sock.accept()
    print(f"Connection from {addr}")
    msg = "MSG,3,,,738065,,,,,,,35000,,,34.81609,34.07810,,,0,0,0,0".encode("utf-8")
    while conn:
        received = conn.recv(1024)
        print(f"> {received}")
        print("Sending data")
        conn.sendall(msg)
    sock.close()