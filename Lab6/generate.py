#!/usr/bin/python3
# Austin Lolli 
# Lab 7
# generate.py

import random
import sys




def random_data(size):
  """<Write what this function does here>
  """
  i = 0
  while i < size:
    data = random.randint(0, 255)
    sys.stdout.write(chr(data))
    i += 1
  sys.stdout.write("\n")

def perfect_eight():
  """<Write what this function does here>
  """ 
  string = ""
  while len(string) < 256:
    data = chr(random.randint(0, 255))
    if data not in string:
      string += data
  sys.stdout.write(string)
  sys.stdout.write("\n")

# the following code is provided to you for free
if __name__ == "__main__":
  try:
    which = sys.argv[1]
    if which == "random":
      size = int(sys.argv[2])
      random_data(size)
    elif which == "perfect":
      perfect_eight()
    else:
      raise IndexError("invalid option")
  except IndexError as e:
    usage_str = "Usage:\n"                 \
                "\tpython3 {prog} random <size>\n" \
                "\tpython3 {prog} perfect\n"
    sys.stderr.write(usage_str.format(prog=sys.argv[0]))
    sys.exit(1)




