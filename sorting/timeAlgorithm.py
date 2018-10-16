from countingSort import countingSort
from quickSort import quickSort
from insertionSort import insertionSort
import time


def timeAlgorithm(array, algorithm):
    if algorithm == "counting":
        start = time.time_ns()
        countingSort(array)
        end = time.time_ns()
    elif algorithm == "quick":
        start = time.time_ns()
        quickSort(array, 0, len(array) - 1)
        end = time.time_ns()
    elif algorithm == "insertion":
        start = time.time_ns()
        insertionSort(array)
        end = time.time_ns()
    else:
        return 1
    return end - start
