# Uses python3
import sys

def get_optimal_value(capacity, data):
    max_value = 0
    # write your code here
    for item in data:
        if capacity == 0:
            return max_value
        max_value += min(item[1], capacity) * item[2]
        capacity -= min(item[1], capacity)
    return max_value


if __name__ == "__main__":
    data = list(map(int, input().split()))
    n, capacity = data[0:2]
    data = []
    for _ in range(n):
        value, weight = map(int, input().split())
        data.append((value, weight, value/weight))
    # Wrapped data in a weird way by using tuple
    data = sorted(data, key=lambda item: item[2], reverse=True)

    opt_value = get_optimal_value(capacity, data)
    print("{:.4f}".format(opt_value))

    # print(get_optimal_value(50, [(120, 30, 4.0), (60, 20, 3.0), (100, 50, 2.0)]))
    # print(get_optimal_value(10, [(500, 30, 16.66667)]))
