#!/usr/bin/python3
# Austin Lolli 
# Lab 4 talk.py

# Usage behavior: python3 talk.py $host:$port

import sys
import socket

def usage():
  usg_str = "Usage: python3 {} $host:$port\n"
  sys.stderr.write(usg_str.format(sys.argv[0]))
  exit(1)

try:
  host = sys.argv[1].split(':')[0]
  port = int(sys.argv[1].split(':')[1])
except IndexError:
  usage()

def talk(host, port):
  # creates a socket called sudp using internet and UDP
  sudp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  # continually read messages 
  while True:
    # reads lines from stdin stores as message, strips newline and trailing whitespace
    message = sys.stdin.readline()
    message = message.rstrip()
    # while theres a message to send (anything but ctrl-D)
    if message:     
      # sends message to host at port
      sudp.sendto(message.encode(), (host, port))
      # quit already sent so listen can close, if quit was message, close here
      if message == "quit":
        sudp.close()
        sys.exit(0)
    # if ctrl-D pressed, close talk (listen will keep running)
    else:
      sudp.close()
      sys.exit(0)

if __name__ == "__main__":
  talk(host, port)


