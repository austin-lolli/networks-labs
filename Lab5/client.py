#!/usr/bin/python3
# Austin Lolli
# Lab 5 client.py 

import json
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
except (IndexError, ValueError):
  usage()

def get_chunk(chunk_size=512, stream=sys.stdin):
  while True:
    data = stream.read(chunk_size) 
    if not data:
      break
    yield data

def compute_checksum(data, bound=256):
  return sum(data.encode()) % bound






def reliable_send(udp_socket, sequence, data, packet_size=1024):
  # creates packet dictionary
  packet = dict()
  packet["data"] = data
  packet["sequence"] = sequence
  packet["checksum"] = compute_checksum(data)  i
  #serializes packet
  packet = json.dumps(packet).encode()
  while True:
    # sends packet
    udp_socket.send(packet)    
    ack = int(udp_socket.recv(1024).decode())
    # if recieved acknowledge is not equal to sequence, break (data recieved correctly)
    if ack != sequence:
      break
  return ack





def client(host, port, dst_file):
  sequence = 0
  termination_string = str(random.random())

  udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  try:
    udp_socket.connect( (host, port) )
  except socket.gaierror:
    sys.stderr.write("Invalid Host: {}\n".format(host))
    exit(1)

  sequence = reliable_send(udp_socket, sequence, termination_string)
  sequence = reliable_send(udp_socket, sequence, dst_file)

  for chunk in get_chunk():
    sequence = reliable_send(udp_socket, sequence, chunk)

  sequence = reliable_send(udp_socket, sequence, termination_string)
  udp_socket.close()


if __name__ == "__main__":
  client(host, port, dst_file)





