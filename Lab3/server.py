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

def server(port, chunk_size=1024):
  test = "hello!"
  # creates a socket using internet and UDP
  sudp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  # binds the socket to the address, using its own IP and the designated port
  sudp.bind(('', port))
  # receives the termination string, saves for ending data loop later
  term = sudp.recv(1024).decode()
  # receives name of destination file
  dst_file = sudp.recv(1024).decode()
  sudp.send(test.encode())
  # writes data received over the connection to the file until the termination 
  # string is received, when this happens, close connection and break loop
  with open(dst_file, 'w') as f:
    while True:
      data = sudp.recv(1024).decode()
      if data != term:
        f.write(data)
      else:
        sudp.close()
        break


if __name__ == "__main__":
  server(port)



