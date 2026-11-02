import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    conn, addr = s.accept()

    with conn:
        n = int(conn.recv(1024).decode())

        digits = str(n)
        power = len(digits)

        total = sum(int(d) ** power for d in digits)

        if n >= 0 and total == n:
            result = "Armstrong number"
        else:
            result = "Not an Armstrong number"

        conn.sendall(result.encode())
