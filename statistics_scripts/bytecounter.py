#!/usr/bin/env python3
import tqdm
import argparse
import os
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Get basic statistics on a random number file')
parser.add_argument("--file", '-f', help='Input file')

args = parser.parse_args()

bytecounts = {}
for i in range(256):
    bytecounts[i] = 0

filesize = os.path.getsize(args.file)
bytesread = 0

with open(args.file, "rb") as rng_file:
    with tqdm.tqdm(total=filesize) as pbar:
        byte = rng_file.read(1)
        while byte:
            bytesread += 1
            byte_as_int = int.from_bytes(byte, byteorder='little')
            bytecounts[byte_as_int] += 1
            byte = rng_file.read(1)
            pbar.update(1)

for byte, count in bytecounts.items():
    print("Byte   " + str(byte) + "\t" + str(count) + "\t" + str(round(count*100/bytesread, 4)) + "%")


x_axis = list(bytecounts.keys())
y_pos = np.arange(len(x_axis))

y_axis = list(bytecounts.values())


plt.bar(y_pos, y_axis, align='center', alpha=0.5)
plt.xticks(y_pos, x_axis)
plt.ylabel('Count')
plt.xlabel('Byte')
plt.title('Byte Counts')

plt.show()
