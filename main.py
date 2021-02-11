import sys
from random import randint
# def zadacha_one()

def zad_odin():
    nmbr_lst = []
    curr = 0
    best = 0

    n = input()
    if n == '':
        exit()
    else:
        for _ in range(int(n)):
            nmbr_lst.append(int(input()))

        for nmbr in nmbr_lst:
            if nmbr > 0:
                curr += 1
                best = max(best, curr)
            else:
                curr = 0

        print(best)

    # zadacha_adin([1, 1, 1, 1, 1])
    # zadacha_adin([0])
    # zadacha_adin([1, 0, 1, 0, 1])
    # zadacha_adin([1, 1, 1, 0, 1])
    # zadacha_adin([1, 1, 0, 1, 1, 0])
    # zadacha_adin([1, 1, 0, 1, 1, 1])
    # zadacha_adin([])
    # zadacha_adin([0, 0, 0])

def zad_dva():
    n = input()

    last = 0
    ind = 0
    nmbr_lst = []
    while ind < int(n):
        curr = int(input())
        if curr != last:
            print(curr)
            last = curr
        ind += 1


def gen(st, open_count, close_count, n):
    if len(st) == n*2:
        if open_count == close_count:
            print(st)
        return
    gen(st+'(', open_count+1, close_count, n)
    if open_count > close_count:
        gen(st+')', open_count, close_count+1, n)

def zad_tri():
    n = int(input())
    gen('', 0, 0, n)

def binary_search(lst, item):
    low = 0
    high = len(lst) - 1
    guess_counter = 0

    while low <= high:
        mid = (high + low) // 2
        guess = lst[mid]
        guess_counter += 1
        if guess == item:
            return guess_counter
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1

    return None

def rec_sum(n_list):
    if not n_list:
        return 0
    return n_list[0] + rec_sum(n_list[1:])

def list_counter(nlist):
    if not nlist:
        return 0
    return 1 + list_counter(nlist[1:])

def count_max(nlist):
    if not nlist:
        return 0
    return max(nlist[0], count_max(nlist[1:]))

if __name__ == '__main__':
    # print(binary_search([1, 3, 5, 7, 9], 3))
    # print(binary_search([1, 3, 5, 7, 9], -1))
    # print(binary_search([1, 3, 5, 7, 9], 7))
    #
    # lst1 = [x for x in range(128)]
    # lst2 = [x for x in range(256)]

    # print(rec_sum([1, 2, 4, 4, 4]))
    #
    # print(list_counter([1, 2, 4, 4]))
    # print(list_counter([0]))
    # print(list_counter([]))

    print(count_max([0]))
    print(count_max([5, 4, 3, 2]))
    print(count_max([4, 10, 6, 8]))
    print(count_max([]))