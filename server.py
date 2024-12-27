import socket
import time

PORT = 30001

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', PORT))
sock.listen()

while True:
    conn, addr = sock.accept()
    print(f"Connection from {addr}")
    msg = "MSG,3,,,738065,,,,,,,35000,,,34.81609,34.07810,,,0,0,0,0".encode("utf-8")
    for i in range(60):
        conn.sendall(msg)
        time.sleep(1)
    sock.close()