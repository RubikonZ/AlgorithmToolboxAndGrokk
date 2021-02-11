# Uses python3
import sys

def gcd(a, b):
    if b == 0:
        return a
    a = a % b
    return gcd(b, a)

if __name__ == "__main__":
    inpt = input().split()
    a, b = int(inpt[0]), int(inpt[1])
    print(gcd(max(a, b), min(a, b)))
