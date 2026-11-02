import socket

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    n = input("Enter a number: ")

    s.sendto(n.encode(), (HOST, PORT))

    data, addr = s.recvfrom(1024)
    print(data.decode())
