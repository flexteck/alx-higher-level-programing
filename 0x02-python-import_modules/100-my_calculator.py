#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if (len(sys.argv) - 1) != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

operators = ['+', '-', '*', '/']
arg1 = int(sys.argv[1])
arg2 = sys.argv[2]
arg3 = int(sys.argv[3])

if arg2 not in operators:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

if arg2 == "+":
    result = add(arg1, arg3)
elif arg2 == "-":
    result = sub(arg1, arg3)
elif arg2 == "*":
    result = mul(arg1, arg3)
elif arg2 == "/":
    result = div(arg1, arg3)

print(f"{arg1} {arg2} {arg3} = {result}")
