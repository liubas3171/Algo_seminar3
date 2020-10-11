import math


def partition(array, p, r):
    x = array[r]
    i = p - 1
    count = 0
    for j in range(p, r):
        if array[j] == x:
            count += 1
        if array[j] <= x:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1 - math.ceil(count / 2)
