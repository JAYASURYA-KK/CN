import socket

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    a = input("Enter first number: ")
    b = input("Enter second number: ")

    s.sendto((a + "," + b).encode(), (HOST, PORT))

    data, addr = s.recvfrom(1024)
    print("Sum:", data.decode())
