#!/usr/bin/env python
# coding:utf-8

"""
AES (Rijndael)
Author : Yopiyama
"""

import copy



class AES:
	"""
	AES Class

	Attributes
	----------
	__state_array : [[ byte ]]
		State Array
	"""

	__state_array = [[]]
	__sbox = {"a":"a"}

	def __init__(self):
		self.bit = 256
		self.round = 14
		self.__state_array = [["" for i in range(4)] for i in range(4)]
		# print("__init__")

	def __sub_bytes(self):
		""" SubBytes Method """
		# print("SubBytes")

	def __shift_rows(self):
		""" ShiftRows Method """
		# print("ShiftRows")
		for i in range(4):
			self.__state_array[i] = self.__state_array[i][i:4] + self.__state_array[i][:i]

	def __mix_columns(self):
		""" MixColumns Method """
		# print("MixColumns")
		def gfm(a, b):
			""" Multiplication on Galois Field
			https://www.samiam.org/galois.html
			"""
			# print("Galois Field Multiplication")
			p = 0
			for i in range(8):
				if b & 1:
					p ^= a
				high_bit = a & 0x80
				a <<= 1
				a &= 0xFF
				if high_bit == 0x80:
					a ^= 0x1B
				b >>= 1
			return p

		tmp = copy.deepcopy(self.__state_array)
		for i in range(4):
			self.__state_array[0][i] = gfm(tmp[0][i], 2) ^ gfm(tmp[1][i], 3) ^ tmp[2][i] ^ tmp[3][i]
			self.__state_array[1][i] = tmp[0][i] ^ gfm(tmp[1][i], 2) ^ gfm(tmp[2][i], 3) ^ tmp[3][i]
			self.__state_array[2][i] = tmp[0][i] ^ tmp[1][i] ^ gfm(tmp[2][i], 2) ^ gfm(tmp[3][i], 3)
			self.__state_array[3][i] = gfm(tmp[0][i], 3) ^ tmp[1][i] ^ tmp[2][i] ^ gfm(tmp[3][i], 2)

	def __add_round_key(self):
		""" AddRoundKey Method """
		# print("AddRoundKey")

	def __split_data(self, data):
		""" Divide the data into 16 bytes for each 8 bits """
		# print("Split Data")

	def encode(self, plain_data):
		""" Encode Method """
		cipher_text = ""
		print("encode")
		for i in range(self.round):
			self.__split_data(plain_data)
			self.__sub_bytes()
			self.__shift_rows()
			self.__mix_columns()
			self.__add_round_key()
		self.__sub_bytes()
		self.__shift_rows()
		self.__add_round_key()
		return cipher_text

def main():
	""" Main Function """
	aes = AES()
	m = "a"
	c = aes.encode(m)

if __name__ == '__main__':
	main()
