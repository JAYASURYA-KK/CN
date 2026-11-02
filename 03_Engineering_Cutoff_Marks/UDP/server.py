import socket

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))

    data, addr = s.recvfrom(1024)

    m, p, c = map(float, data.decode().split(","))

    cutoff = m + p / 2 + c / 2

    s.sendto(str(cutoff).encode(), addr)
