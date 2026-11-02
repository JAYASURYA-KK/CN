import socket

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    string = input("Enter main string: ")
    sub = input("Enter substring: ")

    msg = string + "|" + sub
    s.sendto(msg.encode(), (HOST, PORT))

    data, addr = s.recvfrom(1024)
    print(data.decode())
