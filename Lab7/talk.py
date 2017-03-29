
import sys
import socket

def usage():
  usg_str = "Usage: python3 {} $host:$port\n"
  sys.stderr.write(usg_str.format(sys.argv[0]))
  exit(1)

try:
  host = sys.argv[1].split(':')[0]
  port = int(sys.argv[1].split(':')[1])
except (IndexError, ValueError):
  usage()

def get_message(stream=sys.stdin):
  try:
    for line in stream:
      yield line.strip()
  except KeyboardInterrupt:
    return





def encrypt(plaintext, key):
  # pretend this function is already implemented
  return plaintext




def secure_send(udp_socket, message):
  # Note that choose/select would realistically be done by the computer/program, not the user
  # Alice connects to Bob using talk(Bob, port)
  # Alice chooses a large prime for the finite field, and g, a generator of said prime
  # Alice selects a number in the range of the finite field to be her private key
  # Alice takes the generator and raises it to the power of her private key, modulo the prime
  # Alice does this:   intermediate_val = (generator ^ Alice_priv_key) % prime 
  # Alice sends intermediate_val to Bob, waits for Bob to take that value and raise it to the power
  #   of his private key, mod it by the prime, and send it back. This result is the shared_key
  # Bob does this:   shared_key = (intermediate_val ^ Bob_priv_key) % prime
  # Both Alice and Bob can now send secure messages between each other
  # Alice will take her plaintext message and encrypt using encrypt(plaintext, key)
  # Alice sends encrypted message to Bob
  return udp_socket.send(message.encode())





def talk(host, port):
  udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  
  term_string = "quit"
  
  try:
    udp_socket.connect( (host, port) )
  except socket.gaierror:
    sys.stderr.write("Invalid Host: {}\n".format(host))
    exit(1)

  for message in get_message():
    secure_send(udp_socket, message)
    if message == term_string:
      break

  udp_socket.close()


if __name__ == "__main__":
  talk(host, port)
