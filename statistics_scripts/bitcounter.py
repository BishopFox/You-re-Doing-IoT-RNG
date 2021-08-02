#!/usr/bin/env python3
import tqdm
import argparse
import os

parser = argparse.ArgumentParser(description='Get basic statistics on a random number file')
parser.add_argument('--file', help='Input file')

args = parser.parse_args()


def countOnes(i):
    """
    This is magic. I copied it from stack overflow and have no idea how it works.
        It seems to work though.
    """
    i = i - ((i >> 1) & 0x55555555)
    i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
    return (((i + (i >> 4) & 0xF0F0F0F) * 0x1010101) & 0xffffffff) >> 24


ones = 0

filesize = os.path.getsize(args.file)
bytesread = 0

with open(args.file, "rb") as rng_file:
    with tqdm.tqdm(total=filesize) as pbar:
        byte = rng_file.read(1)
        while byte:
            ones += countOnes(int.from_bytes(byte, byteorder='big'))
            bytesread += 1
            byte = rng_file.read(1)

            pbar.update(1)

print("Total bits: ", bytesread * 8)
print("Ones: ", ones)
print("Percentage: ", ones / (bytesread * 8))
