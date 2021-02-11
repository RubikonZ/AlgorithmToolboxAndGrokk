# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    fib_count = 1
    nmbr1, nmbr2 = 0, 1
    if n in [0, 1]:
        return n
    else:
        while True:
            nmbr1, nmbr2 = nmbr2 % 10, (nmbr2 + nmbr1) % 10
            fib_count += 1
            if n == fib_count:
                return nmbr2

if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
