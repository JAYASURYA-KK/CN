import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    m = input("Enter Mathematics mark: ")
    p = input("Enter Physics mark: ")
    c = input("Enter Chemistry mark: ")

    msg = m + "," + p + "," + c
    s.sendall(msg.encode())

    data = s.recv(1024)
    print("Engineering cutoff:", data.decode())
