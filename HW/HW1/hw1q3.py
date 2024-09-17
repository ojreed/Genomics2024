# Import the sys module to access command-line arguments
import sys
# This module is for your reference to understand the usage
if len(sys.argv) != 3:
    print("Usage: python3 hw1q1b.py <input_file> <output_file>")
    sys.exit(1)
# Assign the input and output filenames from command-line arguments
input_file = sys.argv[1] # First argument: input filename
output_file = sys.argv[2] # Second argument: output filename

counter = 0

with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
    for line in in_file:
        for char in line:
            if char in "CTAG":
                if counter % 3 == 0 and counter != 0:
                    out_file.write("-")
                if char == "T":
                    out_file.write("U")
                else:
                    out_file.write(char)
                counter += 1
                
                