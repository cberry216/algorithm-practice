from heapq import *


def heapSort(array):
    heapify(array)
    sortArray = []
    for i in range(len(array)):
        sortArray.append(heappop(array))
    return sortArray

