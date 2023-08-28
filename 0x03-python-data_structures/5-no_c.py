#!/usr/bin/python3

def no_c(my_string):
    chars = list(my_string)
    chars = [c for c in chars if c not in "cC"]
    return "".join(chars)
