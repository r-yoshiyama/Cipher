#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
This program can encode & decode about caesar cipher.
'''
mode = input("encode or decode >>>")
n = int(input("key >>>"))
code = input("sentence >>>")
if mode == "decode":
	n = 26 - n

output = ""
for s in code:
	if "A" <= s <= "Z":
		output += chr((ord(s)-ord("A")+n)%26+ord("A"))
	elif "a" <= s <= "z":
		output += chr((ord(s)-ord("a")+n)%26+ord("a"))
	else:
		output += s

print (output)
