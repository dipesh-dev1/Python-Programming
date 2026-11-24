# Calculator Using argparse

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("num1", type=float)
parser.add_argument("num2", type=float)
parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"])

args = parser.parse_args()

if args.operation == "add":
    result = args.num1 + args.num2
elif args.operation == "subtract":
    result = args.num1 - args.num2
elif args.operation == "multiply":
    result = args.num1 * args.num2
else:
    result = args.num1 / args.num2

print("Result:", result)