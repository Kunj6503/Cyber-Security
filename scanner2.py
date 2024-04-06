#!/bin/python3

import sys 
import socket
from datetime import datetime

# define target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # translate host name to ipv4
else:
    print("invalid amount of arguments")
    print("syntax: python3 scanner.py <ip>")
    sys.exit(1)

# add a banner
print("-" * 50)
print("scanning target: " + target)
print("time started: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()

except KeyboardInterrupt:
    print("\nExiting Program")
    sys.exit(0)

except socket.gaierror as e:
    print(f"Error resolving hostname: {e}")
    sys.exit(2)

except socket.error as e:
    print(f"Error connecting to socket: {e}")
    sys.exit(3)

except Exception as e:
    print(f"Unexpected error: {e}")
    sys.exit(4)
