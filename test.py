import argparse

# python test.py  --param1 'C:\Users\test' --param2 "C:\Users\test" --param2 ^"a b c^"

parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument("--param1")
parser.add_argument("--param2")
parser.add_argument("--param3")
args = parser.parse_args()
print("param1", args.param1)
print("param2", args.param2)
print("param3", args.param3)
