
import sys


# do not modify this function
def get_input():
  # default prime and base
  prime = 64303
  base = 6

  # attempt to get input
  try:
    a_pk = int(sys.argv[1])
    b_pk = int(sys.argv[2])
    if len(sys.argv) > 3:
      prime = int(sys.argv[3])
      base = int(sys.argv[4])
  except (IndexError, ValueError):
    fmt_str = "Usage:\n" \
              "\tpython3 {} <a_pk> <b_pk> [<prime> <base>]\n"
    sys.stderr.write(fmt_str.format(sys.argv[0]))
    sys.exit(1)

  # return input
  return a_pk, b_pk, prime, base




if __name__ == "__main__":
  a_pk, b_pk, prime, base = get_input()
  # do your computation here
  # compute the private key, generator to power of private keys mod finite field 
  public = ((base**a_pk)**b_pk) % prime
  # should be unnessecary, but just confirms shared public key is same for Alice and Bob
  assert (public == ((base**b_pk)**a_pk) % prime)
  sys.stdout.write("Shared Key: {}\n".format(public))

# More realistic version, some pseudocoded:
  # Alice chooses a large prime and a generator of that prime (use prime and base here)
  # Alice chooses a private key that is in the range of finite field
  # Alice computes generator^private mod finite field, intermediate,  and sends to Bob
#  a_int = (base**a_pk) % prime
#  sendto(a_int, Bob)
  # Bob does the same thing, sends Alice generator^private mod ff
#  b_int = (base**b_pk) % prime
#  sendto(b_int, Alice) 
  # Both Alice and Bob receive the intermediate keys, and raise it to power of their private keys mod ff
#  recvfrom(intermediate_key, A || B)
#  shared_key = (intermediate_key**b_pk) % prime 
#  sys.stdout.write("Shared Key: {}".format(shared_key))
