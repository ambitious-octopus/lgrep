import sys

def hello(variable):
    print(f"result: {variable}")

data = sys.stdin.read()
hello(data)