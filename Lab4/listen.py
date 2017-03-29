#!/usr/bin/python3
# Austin Lolli
# Lab 3 server.py
#
# Usage behavior: python3 server.py $port

import sys
import socket

def usage():
  usg_str = "Usage: python3 {} $port\n"
  sys.stderr.write(usg_str.format(sys.argv[0]))
  exit(1)

try:
  port = int(sys.argv[1])
except (IndexError, ValueError):
  usage()

def listen(port):
  # creates a socket called sudp using an internet connection and udp
  sudp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  # binds the socket to the address, using its own IP and designated port
  sudp.bind(('', port))
  # want to continually listen for messages
  while True:
    # recvfrom returns message and address of sender, store both
    message, addr = sudp.recvfrom(1024)
    message = message.decode()
    # if quit message received from talk program, close socket & stop listening
    if message == "quit":
      sudp.close()
      sys.exit(0)
    # any other message is printed as "IP: message"
    else:
      print("{}: {}".format(addr[0], message))

if __name__ == "__main__":
  listen(port)



