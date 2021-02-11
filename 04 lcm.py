# Uses python3
import sys


def lcm_naive(a, b):

    def gcd(a, b):
        if b == 0:
            return a
        a = a % b
        return gcd(b, a)

    return (a * b) // gcd(a, b)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_naive(a, b))

