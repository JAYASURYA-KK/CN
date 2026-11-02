import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    conn, addr = s.accept()

    with conn:
        w, h = map(float, conn.recv(1024).decode().split(","))

        if h > 0:
            bmi = w / (h * h)
            result = round(bmi, 2)
        else:
            result = "Invalid height"

        conn.sendall(str(result).encode())
