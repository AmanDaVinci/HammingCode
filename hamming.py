#! /home/aman/anaconda3/bin/python3
""" hamming.py

Error correction and detection using Hamming Codes

Usage:
	$ ./hamming.py [options] [input_string]

Options:
	-e ..., --encode=...		string to encode to hamming code
	-d ..., --decode=...		hamming code to decode into message after error correction

Examples:
	$ ./hamming.py -e secretmessgage

	$ ./hamming.py -d

"""

import sys
import math
import copy
import getopt
import binascii
from itertools import zip_longest

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "he:d:", ["help", "encode=", "decode="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    if not opts:
    	usage()
    	sys.exit()

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        
        elif opt in ("-e", "--encode"):
            data = arg
            print(hamming_encode(data))
            sys.exit()

        elif opt in ("-d", "--decode"):
            data = arg
            print(hamming_decode(data))
            sys.exit()

def usage():
	usage = "Usage: ./hamming.py [options] [input_string]"
	print(usage)

def hamming_encode(data):
	"""Encodes data into hamming code

	Args:
		Data to be encoded

	Returns:
		Hamming coded data
	"""
	# Convert string into binary bits
	databits = list(text_to_bits(data))

	# Set parity bits and return the hamming code
	code = set_parity(databits)

	return ''.join(code)

def hamming_decode(code):
	"""Decodes hamming code after error correction and detection

	Args:
		Hamming code to be decoded

	Returns:
		Original Data if error can be corrected, null otherwise
	"""

	# Converting string to list
	code = list(code)

	# Getting the positions of incorrect parity bits
	error_pos = check_parity(code) - 1

	code[error_pos] = '1' if (code[error_pos] == '0') else '0'

	return ''.join(code)

def check_parity(code):

	error_sum = 0

	# Checking with the correct parity bits
	for i in range(len(code)):

		# Parity locations
		if isPowerOf2(i+1):
			parity = compute_parity(code, i+1)
			
			# Computed parity does not match
			if parity != code[i]:
				error_sum = error_sum + i+1

	return error_sum


def set_parity(bits):
	"""Sets parity bits into the original data bits"""
	
	# Inserting the parity positions
	for i in range(len(bits)):
		if isPowerOf2(i+1):
			bits.insert(i,'_')
	
	# Filling up the parity bits
	for i in range(len(bits)):
		if isPowerOf2(i+1):
			bits[i] = compute_parity(bits, i+1)

	return bits

			
def compute_parity(bits, pos):
	"""Computes the parity bit of a given position"""
	
	tempbits = copy.deepcopy(bits)

	# Adding a temp bit in the beginning
	# for the hamming code algorithm to work
	tempbits.insert(0, '*')

	# Grouping the bits which are needed to
	# compute parity of position pos  
	chunks = list(grouper(tempbits, pos))

	# Chunks to check parity in, skipping others
	parity_chunks = chunks[1::2]

	# Finding the number of ones in the groups
	# To perform XOR over the bits
	ones = 0
	for li in parity_chunks:
		ones+=li.count('1')

	# Parity is one for odd number of ones
	if ones%2 != 0:
		return '1'
	# Parity is zero otherwise
	elif ones%2 == 0:
		return '0'

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def isPowerOf2(n):
    m = math.log(n, 2)
    return m == int(m)

if __name__ == "__main__":
	main(sys.argv[1:])
