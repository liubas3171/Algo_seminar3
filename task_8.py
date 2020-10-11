# Complexity: T(n) = T(n/2) + Θ(1)
# T(n) = Θ(logn)

def find_peak_index(array):
    '''

    :param array: list, Unimodal list of numbers
    :return: int, index of peak element
    '''
    start = 0
    finish = len(array) - 1
    while finish >= start:
        pointer = (start + finish) // 2
        if array[pointer] > array[pointer + 1]:
            if array[pointer] > array[pointer - 1]:
                return pointer
            else:
                finish = pointer - 1
        else:
            start = pointer + 1


if __name__ == '__main__':
    a = [1, 3, 6, 8, 11, 10, 5, 2]
    print(find_peak_index(a))
