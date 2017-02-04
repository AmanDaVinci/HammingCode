#!/usr/bin/env python3
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
import getopt

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
	
	return "Not Implemented"


def hamming_decode(code):
	"""Decodes hamming code after error correction and detection

	Args:
		Hamming code to be decoded

	Returns:
		Original Data if error can be corrected, null otherwise
	"""

	return "Not Implemented"

if __name__ == "__main__":
	main(sys.argv[1:])