#!/usr/bin/python3
import sys

n = len(sys.argv) - 1
if n == 0:
    print(f"{n} arguments.")

if n == 1:
    print(f"{n} argument:")
    print(f"{n}: {sys.argv[n]}")
 
if n > 1:
    print(f"{n} arguments:")

    for i in range(1, n + 1):
        print(f"{i}: {sys.argv[i]}")

