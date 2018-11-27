#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
This program can encode & decode about caesar cipher.
'''

def caesar(code, n):
	""" Caesar Cipher Function
	args : code -> plain or cipher text
	       n    -> key
	"""

	output = ""
	for s in code:
		if "A" <= s <= "Z":
			output += chr((ord(s) - ord("A") + n) % 26 + ord("A"))
		elif "a" <= s <= "z":
			output += chr((ord(s) - ord("a") + n) % 26 + ord("a"))
		else:
			output += s
	return output

if __name__ == '__main__':
	mode = input("encode or decode >>>")
	key = int(input("key >>>"))
	text = input("sentence >>>")
	if mode == "decode":
		key = 26 - key
	print(caesar(text, key))
