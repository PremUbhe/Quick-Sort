def quicksort(array):
    frist = 0
    last = len(array)-1
    code(array, frist, last)
    return array


def code(arrya, first, last):
    if first < last:
        partition_pos = partition(arrya, first, last)
        code(arrya, first, partition_pos - 1)
        code(arrya, partition_pos + 1, last)
    return arrya


def partition(array, first, last):
    i = first
    j = last - 1
    p = array[last]

    while i < j:
        while i < last and array[i] < p:
            i += 1
        while j > first and array[j] >= p:
            j -= 1

        if i < j:
            array[i], array[j] = array[j], array[i]

    if array[i] > p:
        array[i], array[last] = array[last], array[i]

    return i


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
