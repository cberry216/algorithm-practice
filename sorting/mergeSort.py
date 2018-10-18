from math import ceil


def mergeSort(array):
    if len(array) > 1:
        a1, a2 = partition(array)
        a1 = mergeSort(a1)
        a2 = mergeSort(a2)
        array = merge(a1, a2)
    return array


def partition(array):
    splitLength = ceil(len(array) / 2.0)
    return array[:splitLength], array[splitLength:]


def merge(a1, a2):
    b = []
    posA1 = 0
    posA2 = 0
    while posA1 < len(a1) or posA2 < len(a2):
        if posA2 == len(a2):
            b.append(a1[posA1])
            posA1 += 1
        elif posA1 == len(a1):
            b.append(a2[posA2])
            posA2 += 1
        elif a1[posA1] < a2[posA2]:
            b.append(a1[posA1])
            posA1 += 1
        else:
            b.append(a2[posA2])
            posA2 += 1
    return b
