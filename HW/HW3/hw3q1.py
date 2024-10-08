import sys

# Get the filenames from command line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]


SA = []
# Open the input file for reading and output file for writing
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    read_string = infile.read().strip()
    for i in range(len(read_string)):
        suffix = (read_string[i:],i)
        SA.append(suffix)
    SA.sort()
    for pair in SA:
        outfile.write(str(pair[1]))
        outfile.write(" " if pair != SA[-1] else "") 
        
        