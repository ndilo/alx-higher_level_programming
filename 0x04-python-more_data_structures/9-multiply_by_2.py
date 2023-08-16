#!/usr/bin/python3

def multiply_by_2(a_dictionary: dict):
    new_dict = a_dictionary.copy()
    for l in new_dict:
        new_dict[l] = new_dict[l]*2

    return new_dict
