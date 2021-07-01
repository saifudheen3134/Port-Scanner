import socket
from IPy import IP
import colorama
from colorama import init, Fore, Back, Style
colorama.init(autoreset=True)


def scan(target):
    converted_ip = check_ip(target)
    print("\n" + "[-_0 Scanning Target]" + str(target))
    for port in range(1, 100):
        scan_port(converted_ip, port)


def check_ip(ip):
    try:
        IP(ip)
        return (ip)
    except ValueError:
        return socket.gethostbyname(ip)


def get_banner(sock):
    return sock.recv(1024)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print("[+] Port Open " + str(port) + str(banner.decode().strip("\n")))
        except:
            print("[+] Port Open " + str(port))
    except:
        pass


print(f"{Fore.RED}=====================================")
print(f"{Fore.RED}-----------PORT SCANNER--------------")
print(f"{Fore.RED}=====================================")

print(f"{Fore.BLUE}[+] Enter Target/s To Scan(Split Targets with ,): ")
targets = input()
if "," in targets:
    for ip_add in targets.split(","):
        scan(ip_add.strip(" "))
else:
    scan(targets)
