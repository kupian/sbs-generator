import socket

HOST = "127.0.0.1"
PORT = 30001

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
print(f"Connected to {HOST}:{PORT}")

while sock:
    msg = sock.recv(1024).decode("utf-8")
    print(f"> {msg}")