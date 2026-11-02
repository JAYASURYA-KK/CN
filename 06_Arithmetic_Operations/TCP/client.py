import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    a = input("Enter first number: ")
    op = input("Enter operator (+,-,*,/): ")
    b = input("Enter second number: ")

    msg = a + "," + op + "," + b
    s.sendall(msg.encode())

    data = s.recv(1024)
    print("Result:", data.decode())
