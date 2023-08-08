#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        k = ((number * -1) % 10)
    else:
        k = number % 10
    print(k, end='')
    return n
