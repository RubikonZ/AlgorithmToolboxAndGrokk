# Uses python3
def calc_fib(n):
    fib_count = 1
    nmbr1, nmbr2 = 0, 1
    if n in [0, 1]:
        return n
    else:
        while True:
            nmbr1, nmbr2 = nmbr2, nmbr2 + nmbr1
            fib_count += 1
            if n == fib_count:
                return nmbr2

n = int(input())
print(calc_fib(n))
