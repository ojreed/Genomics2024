# Import the sys module to access command-line arguments
import sys
# This module is for your reference to understand the usage
if len(sys.argv) != 3:
    print("Usage: python3 hw1q1b.py <input_file> <output_file>")
    sys.exit(1)
# Assign the input and output filenames from command-line arguments
input_file = sys.argv[1] # First argument: input filename
output_file = sys.argv[2] # Second argument: output filename

with open(input_file, 'r') as file:
    n = int(file.read().strip())

# n = 8

def inv_rev(s):
    o = ""
    for char in s:
        if char == "C":
            o += "G"
        if char == "T":
            o += "A"
        if char == "A":
            o += "T"
        if char == "G":
            o += "C"
    return o[::-1]


string_set = ["A","C","G","T"]
if n == 1:
    sys.exit(0)

for L in range(1,int(n/2)):
    for s in string_set:
        if len(s) == L:
            string_set.append("A" + s)
    for s in string_set:
        if len(s) == L:
            string_set.append("C" + s)
    for s in string_set:
        if len(s) == L:
            string_set.append("G" + s)
    for s in string_set:
        if len(s) == L:
            string_set.append("T" + s)

for i in range(len(string_set)):
        string_set[i] = string_set[i] + inv_rev(string_set[i])

string_set = sorted(string_set, key=lambda x: (x, len(x)))
with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
    for i in range(len(string_set)):
        out_file.write(string_set[i])
        out_file.write("\n")


# print(string_set)






        
        