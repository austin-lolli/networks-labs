#!/usr/bin/python3
# Austin Lolli 
# Lab 3 client.py

# Usage behavior: python3 client.py $host:$port $dst_file <$input_file


import random
import sys
import socket

def usage():
  usg_str = "Usage: python3 {} $host:$port $dst_file <$input_file\n"
  sys.stderr.write(usg_str.format(sys.argv[0]))
  exit(1)

try:
  host = sys.argv[1].split(':')[0]
  port = int(sys.argv[1].split(':')[1])
  dst_file = sys.argv[2]
except IndexError:
  usage()

def get_chunk(chunk_size=1024, stream=sys.stdin):
  while True:
    data = stream.read(chunk_size) 
    if not data:
      break
    yield data

def client(host, port, dst_file):
  # Creates a termination string, r
  r = str(random.randint(0, 10000))
  # creates a socket called sudp using an internet connection and UDP 
  sudp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  try:
    # connect the socket to a remote socket at host, port
    sudp.connect((host, port))
    print("Connected to host: {} \n On port: {}".format(host, port))
    # sends the termination string for server.py
    sudp.send(r.encode())
    # sends name of destination file
    sudp.send(dst_file.encode())
    # uses get_chunk to send data to the server in 1024 byte chunks
    test = sudp.recv(1024).decode()
    print(test)
    for data in get_chunk():
      sudp.send(data.encode())
    # sends the termination string (nothing else to send)
    sudp.send(r.encode())
    sudp.close()
  # invalid address = gaierror
  except socket.gaierror:
    print("{} could not be found!".format(host))
    exit(1)


if __name__ == "__main__":
  client(host, port, dst_file)


