#!/Users/Ryota/.pyenv/shims/python
# -*- coding:utf-8 -*-

code = input("sentence >>>")

for n in range(1,26):
    output = ""
    for s in code:
        if "A" <= s <= "Z":
            output += chr((ord(s)-ord("A")+n)%26+ord("A"))
        elif "a" <= s <= "z":
            output += chr((ord(s)-ord("a")+n)%26+ord("a"))
        else:
            output += s
    print (str(n) + " " +output)

