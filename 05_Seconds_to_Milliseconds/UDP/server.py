import socket

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))

    data, addr = s.recvfrom(1024)

    sec = float(data.decode())
    ms = sec * 1000

    s.sendto(str(ms).encode(), addr)
