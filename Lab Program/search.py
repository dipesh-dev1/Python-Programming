import argparse
import re

parser = argparse.ArgumentParser()

parser.add_argument("filename")
parser.add_argument("pattern")

args = parser.parse_args()

try:
    with open(args.filename, "r") as file:
        text = file.read()

    matches = re.findall(args.pattern, text)

    print("Matches:", matches)

except FileNotFoundError:
    print("Error: File does not exist.")

except re.error:
    print("Error: Invalid regex pattern.")