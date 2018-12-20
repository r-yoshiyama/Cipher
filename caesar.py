#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Caesar Cipher
'''


def caesar(code, n):
    """
    Caesar Cipher algorithm

    Parameters
    ----------
    code : str
        plain/cipher text
    n : key
    Returns
    -------
    output : str
        cipher/plain text
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
    text = input("sentence >>>")
    mode = input("encode(e) or decode(d) >>>")
    key = int(input("key (if -1, print all pattern) >>>"))
    if key == -1:
        for i in range(26):
            print(caesar(text, i))
    else:
        if mode == "decode" | mode == "d":
            key = 26 - key
        print(caesar(text, key))
