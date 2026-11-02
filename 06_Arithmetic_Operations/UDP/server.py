import socket

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))

    data, addr = s.recvfrom(1024)
    a, op, b = data.decode().split(",")

    a = float(a)
    b = float(b)

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/" and b != 0:
        result = a / b
    else:
        result = "Invalid operation"

    s.sendto(str(result).encode(), addr)
