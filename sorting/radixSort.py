# Name: Christopher Berry
# Info: To run this program simply run 'python3 radixSort.py'. This program was run and tested using Python 3.7.0. In this program I sort an array of 100 random values rangin from values 0 to 9999. After running, the program will list all values of the array and say whether the array is sorted or not.


def normalizeValueLength(array):
    """Makes the length of all values of the array 4 characters and converts them to strings to preserve value size.
    
    Arguments:
        array {[integer]} -- array of integers to normalize
    
    Returns:
        [integer] -- array of length 4 string representations of the values
    """

    # Array to store string representations
    sameLengthValues = []

    # Normalize the length of each value
    for value in array:
        if value < 10:
            sameLengthValues.append("000" + str(value))
        elif value >= 10 and value < 100:
            sameLengthValues.append("00" + str(value))
        elif value >= 100 and value < 1000:
            sameLengthValues.append("0" + str(value))
        else:
            sameLengthValues.append(str(value))
    return sameLengthValues


def countingSortSig(array, sig=4):
    """Sorts an array of values on the given significant digit
    
    Arguments:
        array {[string]} -- array of string representation values
        pos {integer} -- significant digit to sort (1 is most significant, 4 is least significant)

    Returns:
        [string] -- array of string representations of values sorted on the given significant digit.
    """

    # Maximum digit among all values
    maxValue = max(list(map(lambda x: int(x[sig - 1]), array)))

    # Initialize distribution array
    distribution = [0 for i in range(maxValue + 1)]

    # Initialize return array
    buffer = [None for i in range(len(array) + 1)]

    # Populate distribution array
    for value in array:
        distribution[int(value[sig - 1])] += 1

    # Finalize distribution array (D[i] = D[i] + D[i - 1])
    for i in range(1, len(distribution)):
        distribution[i] = distribution[i] + distribution[i - 1]

    # Sort the array
    for value in array[::-1]:
        buffer[distribution[int(value[sig - 1])]] = value
        distribution[int(value[sig - 1])] -= 1

    # Return the array begining with index 1 to correct off-by-one
    return buffer[1::]


def radixSort(array):
    """Sorts an array of values base on radix sort algorithm
    
    Arguments:
        array {[integer]} -- array of integers to sort
    
    Returns:
        [integer] -- sorted array of integers
    """

    # Convert given array to normalized array
    normalizedArray = normalizeValueLength(array)

    # For each significant digit, starting with least, sort the array
    for i in reversed(range(1, 5)):
        normalizedArray = countingSortSig(normalizedArray, i)

    # Return array of values expressed as integers
    return list(map(lambda x: int(x), normalizedArray))


def isSorted(array):
    """Tells whether an array is sorted or not
    
    Arguments:
        array {[integer]} -- array to test sorted
    
    Returns:
        boolean -- True if array is sorted, false otherwise
    """

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            return False
    return True


randomArray = [
    7701,
    3470,
    847,
    1006,
    9122,
    3666,
    837,
    8045,
    1641,
    4457,
    6022,
    1193,
    5825,
    6824,
    1436,
    1444,
    1801,
    7293,
    9276,
    2810,
    9509,
    3928,
    4330,
    3733,
    6316,
    2032,
    9129,
    4443,
    5127,
    8808,
    8481,
    5034,
    7775,
    5996,
    2616,
    9151,
    9194,
    5884,
    9422,
    1713,
    505,
    9774,
    1789,
    9574,
    8545,
    5373,
    6563,
    5909,
    4288,
    7978,
    6943,
    4002,
    4183,
    321,
    6295,
    26,
    5571,
    9340,
    9382,
    5111,
    4243,
    3936,
    9052,
    6697,
    4384,
    2229,
    1648,
    1851,
    2972,
    9026,
    5429,
    9833,
    587,
    9302,
    916,
    6352,
    6742,
    8668,
    2727,
    575,
    513,
    5719,
    7494,
    8317,
    7561,
    2954,
    2293,
    6754,
    8679,
    3052,
    7997,
    3719,
    9153,
    3846,
    7659,
    7908,
    5070,
    6305,
    6044,
    4923,
]

sortedArray = radixSort(randomArray)

for val in sortedArray:
    print(val)
print("Is 'sortedArray' actually sorted: " + "Yes" if isSorted(sortedArray) else "No")
