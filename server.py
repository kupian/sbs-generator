import socket
import time
import struct

PORT = 30003

def generate_beast_packet():
    # Example values for the BEAST packet
    sync_byte = b'\x1A'  # BEAST sync byte
    packet_type = b'\x31'  # ADS-B message type
    timestamp = struct.pack(">Q", int(123456789))[-6:]  # Microsecond timestamp (last 6 bytes)
    
    # Example ADS-B Mode-S payload (7 bytes, DF17 with ICAO address and short squitter data)
    adsb_payload = b'\x8D\x48\x23\x19\x44\x87\xAF'  
    
    # Calculate payload length (timestamp + ADS-B payload)
    payload_length = len(timestamp) + len(adsb_payload)
    length_byte = struct.pack(">B", payload_length)
    
    # Combine all parts into the final BEAST packet
    beast_packet = sync_byte + packet_type + length_byte + timestamp + adsb_payload
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