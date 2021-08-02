#!/usr/bin/env python3
import tqdm
import argparse
import os
import numpy as np
import matplotlib.pyplot as plt
import math

"""
For RNGs that create numbers in 4-byte words, let's check the distribution of bits within those words

    This will produce a graph of the frequency of each of the 32-bits in a word. This test will try to
        find any instance of where some bits within the 32-bit word are more occuring more often
        than others.

    NULL HYPOTHESIS: If the nubmers are completely random, we'd expect to see a flat and uniform
        graph with little to no variation.
"""


def bits(n):
    """ Iterator over the bits of an integer
    ex: bits(109) will iterate on 1, 4, 8, 32, 64 (not the 0's)
    """
    while n:
        b = n & (~n+1)
        yield int(math.log(b, 2))
        n ^= b


parser = argparse.ArgumentParser(description='Get basic statistics on a random number file')
parser.add_argument('file', help='Input file')

args = parser.parse_args()

# This will keep track of how often each bit in the 32-bit word gets used
bitcounts = {}
for i in range(32):
    bitcounts[i] = 0

filesize = os.path.getsize(args.file)
bytesread = 0

with open(args.file, "rb") as rng_file:
    with tqdm.tqdm(total=filesize) as pbar:
        word = rng_file.read(4)
        pbar.update(4)
        while word:
            bytesread += 4
            byte_as_int = int.from_bytes(word, byteorder='little')

            for bit in bits(byte_as_int):
                bitcounts[bit] += 1

            word = rng_file.read(4)
            pbar.update(4)

for byte, count in bitcounts.items():
    print("Bit   " + str(byte) + "\t" + str(count) + "\t" + str(round(count*100/bytesread, 4)) + "%")


x_axis = list(bitcounts.keys())
y_pos = np.arange(len(x_axis))

y_axis = list(bitcounts.values())


plt.bar(y_pos, y_axis, align='center', alpha=0.5)
plt.xticks(y_pos, x_axis)
plt.ylabel('Count')
plt.xlabel('Bit')
plt.title('Bit Counts')

plt.show()
