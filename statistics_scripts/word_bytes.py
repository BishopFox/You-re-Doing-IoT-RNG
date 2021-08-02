#!/usr/bin/env python3
import tqdm
import argparse
import os
import numpy as np
import matplotlib.pyplot as plt

"""
For RNGs that create numbers in 4-byte words, let's check the distribution of bytes within those words
    This will produce 4 separate and independent graphs:
        1) looking only at the 1st byte in each word, graph the frequency of each byte
        2) looking only at the 2nd byte in each word, graph the frequency of each byte
        3) ditto 3rd
        4) ditto 4th

    If an RNG produces skewed results depending on which byte within the word it is, this will help
        find that out.

    NULL HYPOTHESIS: If the numbers are completely random, then you should expect to see 4 graphs that are
        completely flat and uniform. Random variation at the tops of the graphs will occur, but it
        should be DIFFERENT variations for each of the 4 graphs. (If you see some "noise" at the top
        of the graph and it's the same "noise" for all 4, then that's non-random)
"""

parser = argparse.ArgumentParser(description='Get basic statistics on a random number file')
parser.add_argument('file', help='Input file')

args = parser.parse_args()

# The bytecounts are split up into 4: the 4 bytes of the word
bytecounts = [{}, {}, {}, {}]
for counts in bytecounts:
    for i in range(256):
        counts[i] = 0

filesize = os.path.getsize(args.file)
bytesread = 0

with open(args.file, "rb") as rng_file:
    with tqdm.tqdm(total=filesize) as pbar:
        word = rng_file.read(4)
        pbar.update(4)
        while word:
            bytesread += 4
            # Turning the bytes array into a list makes a list of integers. Python is cool
            split = list(word)
            bytecounts[0][split[0]] += 1
            bytecounts[1][split[1]] += 1
            bytecounts[2][split[2]] += 1
            bytecounts[3][split[3]] += 1

            word = rng_file.read(4)
            pbar.update(4)

for bytecount in bytecounts:
    for byte, count in bytecount.items():
        print("Byte   " + str(byte) + "\t" + str(count) + "\t" + str(round(count*100/bytesread, 4)) + "%")

    x_axis = list(bytecount.keys())
    y_pos = np.arange(len(x_axis))

    y_axis = list(bytecount.values())

    plt.bar(y_pos, y_axis, align='center', alpha=0.5)
    plt.xticks(y_pos, x_axis)
    plt.ylabel('Count')
    plt.xlabel('Bit')
    plt.title('Bit Counts')

    plt.show()
