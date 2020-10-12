from copy import deepcopy


def merge(lst1, lst2):
    lst21 = [2 * x for x in lst2]
    count = 0
    inversions = 0
    lst = []
    i = j = 0
    while i < len(lst1) and j < len(lst21):
        if lst1[i] <= lst21[j]:
            lst.append(lst1[i])
            i += 1
            inversions += count
        else:
            lst.append(lst21[j])
            j += 1
            count += 1
    inversions += (len(lst1) - i) * count

    lst = []
    i = j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            lst.append(lst1[i])
            i += 1
        else:
            lst.append(lst2[j])
            j += 1
    lst += lst1[i:] + lst2[j:]
    return lst, inversions


def count_invert(lst):
    if len(lst) <= 1:

        return lst, 0
    else:
        lst1 = lst[:len(lst)//2]
        lst2 = lst[len(lst)//2:]
        lst1, inv1 = count_invert(lst1)
        lst2, inv2 = count_invert(lst2)
        lst, inv3 = merge(lst1, lst2)

        return lst, inv1 + inv2 + inv3



print(count_invert([5, 4, 3, 2, 1]))



