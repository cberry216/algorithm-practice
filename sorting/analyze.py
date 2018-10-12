import sys
import os
from randomArray import randomArray
from timeAlgorithm import timeAlgorithm

if len(sys.argv) > 6:
    print("usage: analyze [counting | quick] [-n min max] <number of tests>")

algorithm = sys.argv[1]
try:
    minVal = int(sys.argv[sys.argv.index("-n") + 1])
except ValueError:
    minVal = 0
try:
    maxVal = int(sys.argv[sys.argv.index("-n") + 2])
except ValueError:
    maxVal = 10
numTests = int(sys.argv[len(sys.argv) - 1])

if sys.argv[1] == "counting":
    output = open("/Users/christopherberry/Desktop/countingSort.csv", "w")
elif sys.argv[1] == "quick":
    output = open("/Users/christopherberry/Desktop/quickSort.csv", "w")
output.write("size,runtime\n")

for i in range(1, numTests + 1):
    sys.stdout.write("\rRunning test " + str(i) + " out of " + str(numTests))
    avg_time = 0
    for j in range(10):
        avg_time += timeAlgorithm(randomArray((i * 10), minVal, maxVal), algorithm)
    avg_time /= 10
    output.write(str(i * 50) + "," + str(avg_time) + "\n")
print()

output.close
