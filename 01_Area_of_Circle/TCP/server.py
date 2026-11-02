import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    print("Waiting for client...")
    conn, addr = s.accept()

    with conn:
        data = conn.recv(1024).decode()
        r = float(data)

        area = 3.14 * r * r

        conn.sendall(str(area).encode())
