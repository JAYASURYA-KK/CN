import socket

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    r = input("Enter radius: ")

    s.sendto(r.encode(), (HOST, PORT))

    data, addr = s.recvfrom(1024)
    print("Area of circle:", data.decode())
