#!/usr/bin/python3
def remove_char_at(str, k):
    if k < 0:
        return str
    else:
        return str[:k] + str[k+1:]
