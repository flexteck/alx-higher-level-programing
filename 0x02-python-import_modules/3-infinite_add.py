#!/usr/bin/python3
import sys

n = len(sys.argv) - 1
sum = 0
if n <= 1:
    print(int(sys.argv[1]))

if n > 1:
    for i in range(1, n + 1):
        sum += int(sys.argv[i])

print(sum)
