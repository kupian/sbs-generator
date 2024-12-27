import socket
import time
import struct

PORT = 30003

def generate_beast_packet():
    # Example values for the BEAST packet
    sync_byte = b'\x1a'  # BEAST sync byte
    packet_type = b'\x32'  # ADS-B message type
    mlat = b'\x00\x00\x00\x00\x00\x00'
    rssi = b'\xff'
    signal = b'\x1a\x1a'
    
    adsb_payload = b'\x00\xa1\x84\x1a\x1a\xc3\xb3\x1d'  
    
    # Combine all parts into the final BEAST packet
    beast_packet = sync_byte + packet_type + mlat + rssi + signal + adsb_payload
    return beast_packet

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', PORT))
sock.listen()

while True:
    conn, addr = sock.accept()
    print(f"Connection from {addr}")
    packet = generate_beast_packet()
    while conn:
        print(f"Sending packet: {packet.hex()}")
        conn.sendall(packet)
        time.sleep(3)
    sock.close()