#18 How Hacker Create Github Tools
# Domine name to IP
import socket
import pyfiglet
from termcolor import colored

banner = colored(pyfiglet.figlet_format("Domain To IP"), color='green')
print(banner)

domain_name = input("Enter your target Domain: ")
ip = socket.gethostbyname(domain_name)

print(ip)

