import socket

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))

    data, addr = s.recvfrom(1024)
    n = int(data.decode())

    digits = str(n)
    power = len(digits)

    total = sum(int(d) ** power for d in digits)

    if n >= 0 and total == n:
        result = "Armstrong number"
    else:
        result = "Not an Armstrong number"

    s.sendto(result.encode(), addr)
