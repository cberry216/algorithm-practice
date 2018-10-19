import sys
import os
import time
from randomArray import randomArray
from timeAlgorithm import timeAlgorithm
from onlyOne import onlyOne

if len(sys.argv) > 6:
    print(
        "usage: analyze [counting | quick | insertion | merge | heap] [-n min max] [-sraz] <number of tests>"
    )

# Extract algorithm
algorithm = sys.argv[1]
# Extract minimum list value
try:
    minVal = int(sys.argv[sys.argv.index("-n") + 1])
except ValueError:
    minVal = 0
# Extract maximum list value
try:
    maxVal = int(sys.argv[sys.argv.index("-n") + 2])
except ValueError:
    maxVal = 10
# Extract sorting method
try:
    s = sys.argv[sys.argv.index("-s")]
except ValueError:
    s = ""
try:
    r = sys.argv[sys.argv.index("-r")]
except ValueError:
    r = ""
try:
    a = sys.argv[sys.argv.index("-A")]
except ValueError:
    a = ""
try:
    z = sys.argv[sys.argv.index("-Z")]
except ValueError:
    z = ""

# Extract number of tests to run
numTests = int(sys.argv[len(sys.argv) - 1])

print("Running " + str(numTests) + " trial runs for " + algorithm + " sort.")
if s:
    print("Running with arrays in sorted order.")
if r:
    print("Running with arrays in reverse sorted order.")
if a:
    print("Running with arrays in almost sorted order.")
if z:
    print("Running with arrays in reverse almost sorted order.")

if algorithm == "counting":
    output = open("/Users/christopherberry/Desktop/countingSort.csv", "w")
elif algorithm == "quick":
    output = open("/Users/christopherberry/Desktop/quickSort.csv", "w")
elif algorithm == "insertion":
    output = open("/Users/christopherberry/Desktop/insertionSort.csv", "w")
elif algorithm == "merge":
    output = open("/Users/christopherberry/Desktop/mergeSort.csv", "w")
elif algorithm == "heap":
    output = open("/Users/christopherberry/Desktop/heapSort.csv", "w")
output.write("size,runtime\n")

start = time.time_ns()

for i in range(1, numTests + 1):
    sys.stdout.write("\rRunning test " + str(i) + " out of " + str(numTests))
    avg_time = 0
    for j in range(10):
        avg_time += timeAlgorithm(
            randomArray((i * 10), minVal, maxVal, onlyOne(s, r, a, z)), algorithm
        )
    avg_time /= 10
    output.write(str(i * 10) + "," + str(avg_time) + "\n")
print()

end = time.time_ns()

totalTime = (end - start) / 1000000000.0

print("Total elapsed time: " + str(totalTime) + " seconds")

output.close()
