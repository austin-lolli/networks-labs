
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




def decrypt(ciphertext, key):
  # pretend this function is already implemented
  return ciphertext




def secure_recv(udp_socket, chunk_size):
  (data, addr) = udp_socket.recvfrom(chunk_size)
  # Bob listens for connection from Alice using listen function
  # Bob selects a private key in the range of the finite field (prime)
  # Bob takes the generator, raises to power of private_key, reduce mod prime, sends to Alice
  # Bob and Alice will both take the received intermediate keys from each other, and raise them
  #    to the power of their private keys and reduce, the result is their shared keys. 
  # Alice's message was encrypted using the shared key derived through diffie-hellman
  # Bob receives the ciphertext and the key over the connection and decrypts it using the decrypt function
  # data = decrypt(ciphertext, key)  
  return (data, addr)





def listen(port, chunk_size=1024):
  udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  udp_socket.bind( ("", port) )

  term_string = "quit"
  terminated = False

  while not terminated:
    (data, addr) = secure_recv(udp_socket, chunk_size)
    msg = data.decode().strip()
    ip = addr[0]
    port = addr[1]
    if msg == "quit":
      terminated = True
    else:
      sys.stdout.write("{}: {}\n".format(ip, msg))

  udp_socket.close()


if __name__ == "__main__":
  listen(port)
