import sys
if len(sys.argv) != 3:
    print("Usage: python3 script.py <input_file> <output_file>")
    sys.exit(1)
    
# Assign the input and output filenames from command-line arguments
input_file = sys.argv[1] # First argument: input filename
output_file = sys.argv[2] # Second argument: output filename
# Read input from the file
with open(input_file, "r") as in_file:
    # Read the first line, remove whitespace from both ends
    a = in_file.readline().strip()
    # Read the second line, remove whitespace from both ends
    b = in_file.readline().strip()
    
#Find Hamming Distance
H = 0
for i in range(len(a)):
    if a[i] != b[i]:
        H += 1

# Write the result to the output file
with open(output_file, "w") as out_file:
    out_file.write(str(H))