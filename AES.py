#!/usr/bin/env python
# coding:utf-8

"""
AES (Rijndael)
Author : Yopiyama
"""


class AES:
    """
    AES Class

    Attributes
    ----------
    __state_array : [[ byte ]]
        State Array
    """

    "Nk : Key length, Nb : Block size, Nr : Number of round"
    KEY_128 = {"bit": 128, "Nk": 4, "Nb": 4, "Nr": 10}
    KEY_192 = {"bit": 192, "Nk": 6, "Nb": 4, "Nr": 12}
    KEY_256 = {"bit": 256, "Nk": 8, "Nb": 4, "Nr": 14}

    __sbox = {"a": "a"}

    def __init__(self, key):
        self.key = key
        self.__state_array = [[0 for i in range(4)] for i in range(4)]
        # print("__init__")

    def __sub_bytes(self):
        """ SubBytes Method """
        # print("SubBytes")

    def __shift_rows(self):
        """ ShiftRows Method """
        # print("ShiftRows")

    def __mix_columns(self):
        """ MixColumns Method """
        # print("MixColumns")

    def __add_round_key(self):
        """ AddRoundKey Method """
        # print("AddRoundKey")

    def encode(self, plain_data):
        """ Encode Method """

        print("encode")
        print(plain_data)
        cipher_text = ""
        for i in range(self.key["round"] - 1):
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
    aes = AES(AES.KEY_256)
    c = aes.encode("m")
    print(c)


if __name__ == '__main__':
    main()
