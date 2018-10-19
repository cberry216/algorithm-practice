from math import floor, log2
from heapSort import heapSort
from quickSort import partition


def introSort(array):
    maxDepth = floor(log2(len(array))) * 2
    introSortRec(array, 0, len(array), maxDepth)


def introSortRec(array, start, end, maxDepth):
    if end - start > 1:
        array, pivot = partition(array, start, end)
        if maxDepth == 0:
            heapSort(array, start, end)
        elif start < end:
            introSortRec(array, start, pivot, maxDepth - 1)
            introSortRec(array, pivot + 1, end, maxDepth - 1)

