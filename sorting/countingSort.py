def countingSort(array):
    """Sorts an array of numbers according to the counting sort algorithm
    
    Arguments:
        array {[integer]} -- array of integers to be sorted

    Returns:
        [integer] -- array containing sorted integers
    """

    maxVal = max(array)

    # Initializing the distribution array
    distArray = [0] * (maxVal + 1)
    # Initializing return array
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

