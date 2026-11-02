import socket

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    w = input("Enter weight in kg: ")
    h = input("Enter height in meters: ")

    s.sendto((w + "," + h).encode(), (HOST, PORT))

    data, addr = s.recvfrom(1024)
    print("BMI:", data.decode())
