import socket

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    a = input("Enter first number: ")
    op = input("Enter operator (+,-,*,/): ")
    b = input("Enter second number: ")

    msg = a + "," + op + "," + b
    s.sendto(msg.encode(), (HOST, PORT))

    data, addr = s.recvfrom(1024)
    print("Result:", data.decode())
