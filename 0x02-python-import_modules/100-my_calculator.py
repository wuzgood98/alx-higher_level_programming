#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    import sys

    num_args = len(sys.argv) - 1
    if num_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    
    ops = {"+": calc.add, "-": calc.sub, "*": calc.mul, "/": calc.div}
    if sys.argv[2] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    print("{} {} {} = {}".format(a, op, b, ops[op](a, b)))
