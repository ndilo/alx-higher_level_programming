#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

if number < 0:
    p = number % -10
else:
    p = number % 10

if p > 5:
    phrase = "greater than 5"
elif p == 0:
    phrase = "0"
else:
    phrase = "less than 6 and not 0"

print("Last digit of {} is {} and is {}".format(number, p, phrase))
