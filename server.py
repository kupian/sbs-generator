import socket
import time

PORT = 30003

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', PORT))
sock.listen()

while True:
    conn, addr = sock.accept()
    print(f"Connection from {addr}")
    msg = bytearray([0x8f, 0x46, 0x1f, 0x36, 0x60, 0x4d, 0x74, 0x82, 0xe4, 0x4d, 0x97, 0xbc, 0xd6, 0x4])
    while conn:
        received = str(conn.recv(1024))
        print(f"> {received}")
        print("Sending data")
        conn.sendall(msg)
    sock.close()