import sys
from randomArray import randomArray
from timeAlgorithm import timeAlgorithm

output = open("/Users/christopherberry/Desktop/countingSortAnalysis.csv", "w")
output.write("size,runtime\n")

if len(sys.argv) > 3 and (
    sys.argv[1] != "counting" or sys.argv[1] != "bucket" or sys.argv[1] != "radix"
):
    print("usage: analyze [counting | bucket | radix] <number of tests>")


for i in range(1, int(sys.argv[2]) + 1):
    algorithm = sys.argv[1]
    avg_time = 0
    for j in range(10):
        avg_time += timeAlgorithm(randomArray((i * 10)), algorithm)
    avg_time /= 10
    output.write(str(i * 50) + "," + str(avg_time) + "\n")
