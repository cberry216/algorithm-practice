from countingSort import countingSort
import time


def timeAlgorithm(array, algorithm):
    start = time.time_ns()
    if algorithm == "counting":
        countingSort(array)
    else:
        return 1
    end = time.time_ns()
    return end - start
