# import sys

# name = sys.argv[1]   # Getting argument from command line
# print(f"Hello, {name}! Welcome!")


import argparse

parser = argparse.ArgumentParser(description="Simple Greeting Utility")
parser.add_argument("name", help="Your Name")

args = parser.parse_args()

print("Hello,", args.name)