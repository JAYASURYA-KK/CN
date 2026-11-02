import socket

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))

    data, addr = s.recvfrom(1024)
    w, h = map(float, data.decode().split(","))

    if h > 0:
        result = round(w / (h * h), 2)
    else:
        result = "Invalid height"

    s.sendto(str(result).encode(), addr)
