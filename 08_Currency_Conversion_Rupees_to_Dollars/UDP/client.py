import socket

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    rs = input("Enter amount in rupees: ")

    s.sendto(rs.encode(), (HOST, PORT))

    data, addr = s.recvfrom(1024)
    print("Dollars:", data.decode())
