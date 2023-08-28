#!/usr/bin/python3
def uppercase(str):
    for k in str:
        c = ord(k)
        if ord(k) >= 97 and ord(k) <= 122:
            c -= 32
        print("{:c}".format(c), end='')
    print()
