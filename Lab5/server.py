#!/usr/bin/python3
# Austin Lolli
# Lab 5 server.py

import json
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

def compute_checksum(data, bound=256):
  return sum(data.encode()) % bound




def reliable_recv(udp_socket, packet_size=1024):
  # initialize/create acknowledgement packet
  packet = dict()
  whle True:
    # receives and deserializes the packet
    packet = json.loads(udp_socket.recv(1024).decode())
    # computes the checksum of the data 
    ccsum = compute_checksum(packet["data"])
    # if checksum is equal, send acknowledge signal of sequence += 1 and break loop
    if ccsum == packet["checksum"]:
      ack = str(packet["sequence"] + 1)
      udp_socket.send(ack.encode())
      break
    # if checksum not equal (corrupted data), send ack signal equal to sequence number
    else:
      ack = packet["sequence"] 
      udp_socket.send(ack.encode())
  return packet["data"]



def server(port):
  udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  udp_socket.bind( ("", port) )
  term_string = reliable_recv(udp_socket)
  dst_file = reliable_recv(udp_socket)

  with open(dst_file, "w") as stream:
    while True:
      data = reliable_recv(udp_socket)
      if data == term_string:
        break
      stream.write(data)
  udp_socket.close()




if __name__ == "__main__":
  server(port)





