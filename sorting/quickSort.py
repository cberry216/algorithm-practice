def quickSort(array, start, end):
    if start < end:
        array, pivotPos = partition(array, start, end)
        quickSort(array, start, pivotPos - 1)
        quickSort(array, pivotPos + 1, end)


def partition(array, start, end):
    pivot = array[end]
    pos = start - 1
    for j in range(start, end):
        if array[j] <= pivot:
            pos += 1
            array[pos], array[j] = array[j], array[pos]  # swap
    array[pos + 1], array[end] = array[end], array[pos + 1]
    return array, pos + 1
