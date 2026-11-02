import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    conn, addr = s.accept()

    with conn:
        c = float(conn.recv(1024).decode())

        f = (c * 9 / 5) + 32

        conn.sendall(str(f).encode())
