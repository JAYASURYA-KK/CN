import socket

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))

    data, addr = s.recvfrom(1024)

    string, sub = data.decode().split("|", 1)

    if sub in string:
        result = "Substring exists"
    else:
        result = "Substring does not exist"

    s.sendto(result.encode(), addr)
