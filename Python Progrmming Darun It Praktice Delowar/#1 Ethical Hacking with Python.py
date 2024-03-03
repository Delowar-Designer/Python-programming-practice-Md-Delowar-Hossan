# Ethical Hacking with Python
import socket
sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

ip = input("Enter your ip address: ")

port = int(input("Enter the port your want to scan: "))


def scan_port(port):
    if sock.connect_ex((ip,port)):
        print("port is closed")
    else:
        print("port is opened")


scan_port(port)
