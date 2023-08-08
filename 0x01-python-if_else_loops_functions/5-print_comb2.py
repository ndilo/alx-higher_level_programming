#!/usr/bin/python3

for k in range(0, 100):
    print("{:02d}{}".format(k, ", " if k <= 98 else "\n"), end="")
