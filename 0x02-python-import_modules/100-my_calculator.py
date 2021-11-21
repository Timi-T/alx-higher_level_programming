#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit("1")
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    operators = ['+', '-', '*', '/']
    op_exist = -1
    for i in range(len(operators)):
        if op == operators[i]:
             op_exist = i
    if op_exist == -1:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit("1")
    if op_exist == 0:
        c = add(a, b)
    elif op_exist == 1:
        c =  sub(a, b)
    elif op_exist == 2:
        c = mul(a, b)
    else:
        c =  div(a, b)
    print("{:d} {:s} {:d} = {:d}".format(a, op, b, c))
