#!/usr/bin/env python3
import tqdm
import argparse
import os
import random

parser = argparse.ArgumentParser(description='"Fix" a binary file that is biased \
                                 towards 0 or 1 by some amount. Produces a new \
                                 file named FILE_fixed.bin')
parser.add_argument('file', help='Input file')

args = parser.parse_args()


def countOnes(i):
    """
    This is magic. I copied it from stack overflow and have no idea how it works.
        It seems to work though.
    """
    i = i - ((i >> 1) & 0x55555555)
    i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
    return (((i + (i >> 4) & 0xF0F0F0F) * 0x1010101) & 0xffffffff) >> 24


def flipbits(byte, flip_the_zeros, probability):
    """ Given a byte, stochastically flip the bits and return the result

        byte - a byte from the file you want to flip
        flip_the_zeros - boolean value. Is it the zeros or the ones that we flip?
        probability - float. Probability that we flip any given bit
    """
    # For each bit in the byte...
    for i in range(8):
        # Is it the right kind of bit?
        masked = byte & (1 << i)
        if (masked == 0) == flip_the_zeros:
            if random.random() < probability:
                # Which way do we need to flip it?
                if flip_the_zeros:
                    byte |= (1 << i)
                else:
                    byte &= ~(1 << i)

    # Convert back to a bytes string and return
    return byte.to_bytes(1, 'big')


ones = 0

filesize = os.path.getsize(args.file)
bytesread = 0

print("Measuring the bit bias...")
with open(args.file, "rb") as rng_file:
    with tqdm.tqdm(total=filesize) as pbar:
        byte = rng_file.read(1)
        while byte:
            ones += countOnes(int.from_bytes(byte, byteorder='big'))
            bytesread += 1
            byte = rng_file.read(1)

            pbar.update(1)

bias = ones / (bytesread * 8)
print("ones", ones)
print("zeros", (bytesread * 8) - ones)
print("bits read", bytesread * 8)
print("Bias percentage: ", bias)

flipchance = (0.5 - bias) / (1 - bias)
print("Flip chance", flipchance)

flip_the_zeros = bias < 0.5

# Read the whole file into memory
whole_file = open(args.file, "rb").read()

# Now we loop through the file a second time and flip some bits to make it fair
with open(args.file + "_fixed", "wb") as output_file:
    with tqdm.tqdm(total=len(whole_file)) as pbar:
        for byte in whole_file:
            output_file.write(flipbits(byte, flip_the_zeros, flipchance))
            pbar.update(1)
