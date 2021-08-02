#!/bin/bash
# This is a list of the valid tests to run in Dieharder
# According to the documentation, 1 and 14 are bad. So we don't use them
# https://webhome.phy.duke.edu/~rgb/General/dieharder.php
tests="0 2 3 4 5 6 7 8 9 10 11 12 13 15 16 17 100 101 102 200 201 202 203 204"
# File with random bits. Raw binary
filename=$1

if [ -z "$filename" ]
then
  echo "Provide an argument: the filename of your random numbers in binary form"
  exit 1
fi

# Iterate the string variable using for loop
for val in $tests; do
  dieharder -g 201 -d $val -f $filename
done
