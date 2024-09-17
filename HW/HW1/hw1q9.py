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
    # a = in_file.readline().strip()
    a = in_file.read().replace("\n", "")
    
b = ""

opti_codon_map = {
    "F":"UUC",
    "L":"CUC",
    "S":"AGC",
    "Y":"UAC",
    "C":"UGC",
    "W":"UGG",
    "P":"CCC",
    "H":"CAC",
    "Q":"CAG",
    "R":"CGC",
    "I":"AUC",
    "M":"AUG",
    "T":"ACC",
    "N":"AAC",
    "K":"AAG",
    "V":"GUC",
    "A":"GCC",
    "D":"GAC",
    "E":"GAG",
    "G":"GGC",
}


for char in a:
    if char in opti_codon_map.keys():
        b  += opti_codon_map[char]

with open(output_file, "w") as out_file:
    for val in b:
        out_file.write(val)
