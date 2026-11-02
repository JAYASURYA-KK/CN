import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    conn, addr = s.accept()

    with conn:
        data = conn.recv(1024).decode()

        string, sub = data.split("|", 1)

        if sub in string:
            result = "Substring exists"
        else:
            result = "Substring does not exist"

        conn.sendall(result.encode())
