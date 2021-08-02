#!/usr/bin/env python3
from tqdm import trange
import numpy as np
import random

"""
This is a python script that will generate some test data files
    The test data file are useful for evaluating our stats scripts
"""


def zeros():
    """ Make a 10MB file with just all zeros
    """
    with open("test_data/zeros.bin", "wb") as file:
        chunk = b'\x00' * 10240
        for _ in range(1024):
            file.write(chunk)

    pass


def ff():
    """ Make a file with all 0xff bytes.
    """
    with open("test_data/ff.bin", "wb") as file:
        chunk = b'\xff' * 10240
        for _ in range(1024):
            file.write(chunk)


def uniform():
    """ Make a file that cycles through each byte so that there's always exactly
            the same amount.
    """
    with open("test_data/uniform.bin", "wb") as file:
        chunk = b''
        for byte in range(256):
            chunk = b''.join([chunk, bytes([byte])])

        for _ in range(1024):
            file.write(chunk)


def alternating():
    """ Alternating 0x00000000 and 0xffffffff
    """
    with open("test_data/alternating.bin", "wb") as file:
        chunk_0 = b'\x00' * 4
        chunk_f = b'\xff' * 4

        for _ in range(1024):
            file.write(chunk_0)
            file.write(chunk_f)


def wordnormal():
    """ Treat numbers as 32-bit words. There's too many (2**32) to enumerate
            them all reasonably, it would make for a file many GB in size.
            So instead, let's make a normal distribution of the words bit-wise.
            Basically, each 32-bit word will be randomly generated with
            the middle bits being more likely than the outter bits.

        NOTE: This is super slow. There's probably a more efficient way to do it
    """
    with open("test_data/wordnormal.bin", "wb") as file:

        iterations = 1024*1024
        for i in trange(iterations):
            # Construct a word
            word = 0
            for j in range(32):
                probability = 1 - (abs(16 - j) + 16) / 32
                bit = np.random.binomial(1, probability, 1)
                word += bit[0] << j
            # Write it to file
            file.write(int(word).to_bytes(4, "big"))


def unfair_coin():
    """ This simulates an "unfair coin flip" and what that would look like

        If our bit generator were biased towards making 0's, what would the data
            it produces look like in our stats scripts?
    """
    with open("test_data/unfaircoin.bin", "wb") as file:
        iterations = 1024*1024*4
        for i in trange(iterations):
            # Construct a word
            word = 0
            for j in range(32):
                bit = int(random.random() > 0.503)
                word += bit << j
            # Write it to file
            file.write(int(word).to_bytes(4, "big"))


# Actually call the functions
zeros()
ff()
uniform()
alternating()
print("Creating wordnormal.bin...")
wordnormal()
print("Creating unfaircoin.bin...")
unfair_coin()
