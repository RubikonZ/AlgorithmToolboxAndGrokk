# Uses python3
import sys

def calc_fib_period(n: int, m: int):
    """
    :param n: number of fibonacci iterations
    :param m: Divider
    :return: remainder of fibonacci iteration and m divider
    """
    nmbr1, nmbr2 = 0, 1
    fib_period = 0

    def calc_fib(n_rem: int):
        """
        :param n_rem: This is a remainder of initial n and length of n's periodic sequence, which is much smaller and simpler to calculate
        :return: remainder of 'n' fibonacci iteration and initial 'm' divider
        """
        fib_count = 1
        nmbr1, nmbr2 = 0, 1
        if n_rem in [0, 1]:
            return n_rem
        else:
            while True:
                nmbr1, nmbr2 = nmbr2, nmbr2 + nmbr1
                fib_count += 1
                if n_rem == fib_count:
                    return nmbr2 % m

    # this gets us fib number
    while True:
        nmbr1, nmbr2 = nmbr2, nmbr2 + nmbr1
        fib_period += 1

        # Here we figure out length of fib's periodic sequence
        if nmbr1 % m == 0 and nmbr2 % m == 1:
            # print(f"Length of periodic sequence: {fib_period}\nRemainder of initial n: {n % fib_period}")
            return calc_fib(n % fib_period)


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(calc_fib_period(n, m))
