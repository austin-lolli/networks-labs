#!/usr/bin/python3
# Austin Lolli
# Lab 6 entropy.py

import sys
import math

def entropy(probability):
  return probability*math.log2(probability)

def sum_entropy(probabilities):
  entropy = 0
  for i in range(len(probabilities)):
    entropy += probabilities[i]
  return entropy

if __name__ == "__main__":
  # initialize a new dictionary
  size = 0
  occurences = dict()
  prob_arr = []
  char = sys.stdin.read(1)
  num_rep = ord(char)
  while len(char) is not 0:
    # read one character at a time, convert it to an int
    char = sys.stdin.read(1)
    if len(char) is not 0: 
      num_rep = ord(char)
    else:
      break
    # every non-empty read, increment the size variable 
    size += 1
    # record an occurence of char
    if num_rep in occurences:
      occurences[num_rep] += 1
    else:
      occurences[num_rep] = 1
  # loop through every character found in the string    
  for key in occurences:
    # take the number of occurences for each character, divided by the size of string
    prob = occurences[key] / size
    # intermediate step function calculates prob*base2log(prob)
    ent = entropy(prob)
    # appends the result to an array, so we can sum everything at the end
    prob_arr.append(ent)
  # returns the result of the sum function, total entropy
  print(sum_entropy(prob_arr))
    
