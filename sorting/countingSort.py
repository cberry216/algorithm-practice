def countingSort(array):
    maxVal = max(array)

    distArray = [0] * (maxVal + 1)
    buffer = [0] * (len(array) + 1)

    # Create distribution array
    for value in array:
        distArray[value] += 1
    # Add up dist array values
    for i in range(1, len(distArray)):
        distArray[i] = distArray[i] + distArray[i - 1]
    # Sort the array
    for value in array[::-1]:
        buffer[distArray[value]] = value
        distArray[value] -= 1

    return buffer[1::]

