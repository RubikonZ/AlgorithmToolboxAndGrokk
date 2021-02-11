# Uses python3
import sys

def get_change(m):
    coin_count = 0
    for denom_coin in sorted([1, 10, 5], reverse=True):
        # if denom_coin > m:
        #     pass
        # else:
        while m >= denom_coin and m > 0:
            m -= denom_coin
            coin_count += 1
    return coin_count

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))

    # print(get_change(10) == 1)
    # print(get_change(2) == 2)
    # print(get_change(28) == 6)