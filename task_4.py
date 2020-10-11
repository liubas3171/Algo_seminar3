def partition(array, p, r):
    '''
    :param array: list of values
    :param p: int, index of last element in the array
    :param r: int, index of first element in the array
    :return: int,
    '''
    x = array[r]
    i = p - 1
    for j in range(p, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


def quick_sort(array, low, high):
    '''
    :param array: list of numbers
    :param low: int, index of the very first element in array
    :param high: int, index of last element in array
    :return: None, sorts a given array.
    '''
    stack = []
    stack.append(low)
    stack.append(high)
    while stack:
        high = stack.pop()
        low = stack.pop()
        ind = partition(array, low, high)
        if ind - 1 > low:
            stack.append(low)
            stack.append(ind - 1)
        if ind + 1 < high:
            stack.append(ind + 1)
            stack.append(high)


if __name__ == '__main__':
    arr = [4, 3, 5, 2, 1, 3, 2, 3]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
