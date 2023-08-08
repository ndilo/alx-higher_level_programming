#!/usr/bin/python3
for k in range(0, 90):
    if k % 10 != k / 10 and k % 10 > k / 10:
        print("{:02d}{}".format(k, ", " if k < 89 else '\n'), end="")
