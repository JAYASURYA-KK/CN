import socket

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    sec = input("Enter seconds: ")

    s.sendto(sec.encode(), (HOST, PORT))

    data, addr = s.recvfrom(1024)
    print("Milliseconds:", data.decode())
