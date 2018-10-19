from heapq import *


def heapSort(array, start, end):
    subArray = array[start:end]
    heapify(subArray)
    for i in range(start, end):
        array[i] = heappop(subArray)

