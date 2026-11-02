import socket

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))

    print("Waiting for client...")

    data, addr = s.recvfrom(1024)
    r = float(data.decode())

    area = 3.14 * r * r

    s.sendto(str(area).encode(), addr)
