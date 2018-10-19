from random import randint
from math import ceil


def randomArray(n=10, a=0, b=10, sort="none"):
    if a == b:
        raise ValueError("min and max value cannot be the same")
    array = []
    if sort == "none":
        for i in range(0, n):
            array.append(randint(a, b))
    if sort == "-s":
        array = getSortedArray(n, a, b)
    if sort == "-r":
        array = list(reversed(getSortedArray(n, a, b)))
    if sort == "-a":
        array = getAlmostSortedArray(n, a, b)
    if sort == "-z":
        array = list(reversed(getAlmostSortedArray(n, a, b)))
    return array


def getSortedArray(n, a, b):
    array = []
    if (b - a) <= n:
        # amount of duplicate elements in array
        numCount = ceil(n / (b - a))
        numbersAdded = 0
        currentNum = a
        while numbersAdded < n:
            add = (
                numCount
                if (n - numbersAdded) >= numCount
                else numCount - (n - numbersAdded)
            )
            array.extend([currentNum] * add)
            currentNum += 1
            numbersAdded += numCount
    else:
        numSkip = ceil((b - a) / n)
        numbersAdded = 0
        currentNum = a
        while numbersAdded < n:
            array.append(currentNum)
            currentNum += numSkip
            numbersAdded += 1
    return array


def getAlmostSortedArray(n, a, b):
    refArray = getSortedArray(n, a, b)
    refRange = max(refArray) - min(refArray)
    array = list(
        map(
            lambda x: x
            + randint(
                int(-(max(refArray) - min(refArray)) / 10),
                int((max(refArray) - min(refArray)) / 10),
            ),
            refArray,
        )
    )
    return array
