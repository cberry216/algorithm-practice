from countingSort import countingSort
from quickSort import quickSort
import time


def timeAlgorithm(array, algorithm):
    start = time.time_ns()
    if algorithm == "counting":
        countingSort(array)
    elif algorithm == "quick":
        quickSort(array, 0, len(array) - 1)
    else:
        return 1
    end = time.time_ns()
    return end - start
