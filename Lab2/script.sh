#!/bin/sh


user="alolli"

blockSize=1024
numBlock=1000000
stepSize=50000

for i in $(seq 1 10); do
  count=0
  while [ $count -lt $numBlock ]; do
    size=$(echo "$count * $blockSize" | bc)
    echo "run $i size $size"
    time dd if=/dev/urandom bs=$blockSize count=$count 2>/dev/null \
        | ssh -q $user@linux.dc.engr.scu.edu "dd of=/dev/null 2>/dev/null"
    count=$(echo "$stepSize + $count" | bc)
    echo
    echo ----------
    echo
  done
done



