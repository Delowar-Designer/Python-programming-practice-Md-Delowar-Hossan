# Get Your IP Address by Python Socket
import socket as sc

hostName = sc.gethostname()
ipAddress = sc.gethostbyname(hostName)

print("My IP Addres is: ", ipAddress)