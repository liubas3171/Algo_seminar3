def quick_sort(lst):
    indexes = [(0, len(lst) - 1)]
    while indexes:
        start, end = indexes.pop()
        x = lst[end]
        i = start - 1
        for j in range(start, end):
            if lst[j] <= x:
                i += 1
                lst[j], lst[i] = lst[i], lst[j]
        lst[i + 1], lst[end] = lst[end], lst[i + 1]
        if start < i:
            indexes.append((start, i))
        if end > i + 2:
            indexes.append((i + 2, end))
    return lst


print(quick_sort([44, 2, 7, 1, 9, 0, 5]))
