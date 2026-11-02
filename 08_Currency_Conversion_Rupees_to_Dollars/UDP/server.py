import socket

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))

    data, addr = s.recvfrom(1024)
    rs = float(data.decode())

    dollars = rs / 85

    s.sendto(str(round(dollars, 2)).encode(), addr)
