import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    conn, addr = s.accept()

    with conn:
        data = conn.recv(1024).decode()
        a, op, b = data.split(",")

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

        conn.sendall(str(result).encode())
