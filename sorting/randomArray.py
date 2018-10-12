from random import randint


def randomArray(n=10, a=0, b=10):
    array = []
    for i in range(0, n):
        array.append(randint(a, b))
    return array
