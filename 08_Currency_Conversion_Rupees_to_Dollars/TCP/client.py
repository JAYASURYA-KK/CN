import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    rs = input("Enter amount in rupees: ")
    s.sendall(rs.encode())

    data = s.recv(1024)
    print("Dollars:", data.decode())
