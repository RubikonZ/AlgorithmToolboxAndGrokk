# python3
import sys


# def compute_min_refills(distance, tank, stops):
#     refill = 0
#     current_dist = 0
#     for i in range(len(stops) - 1):
#         if stops[i+1] <= tank or current_dist > stops[i]:
#             continue
#         if (stops[i+1] - stops[i]) > tank:
#             return -1
#         current_dist = stops[i]
#         refill += 1
#     return refill

def compute_min_refills(distance, tank, stops, n):
    stops.append(distance)
    last_stop, current_stop, refills = 0, 0, 0
    while current_stop <= n:
        last_stop = current_stop
        while current_stop <= n and stops[current_stop + 1] - stops[last_stop] <= tank:
            current_stop += 1
        if current_stop == last_stop:
            return -1
        if current_stop <= n:
            refills += 1
    return refills


if __name__ == '__main__':
    d, m, n = int(input()), int(input()), int(input())
    stops = [0] + list(map(int, input().split()))
    print(compute_min_refills(d, m, stops, n))



    # print(stops)

    # print(compute_min_refills(950, 400, [0, 200, 375, 550, 750], 4) == 2)
    # print(compute_min_refills(10, 3, [0, 1, 2, 5, 9], 4) == -1)
    # print(compute_min_refills(500, 200, [0, 100, 200, 300, 400], 4) == 2)
    # print(compute_min_refills(700, 200, [0, 100, 200, 300, 400], 4) == -1)
