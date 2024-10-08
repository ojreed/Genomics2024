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
    BWT = []
    for i in range(len(read_string)):
        if SA[i][1] > 0:
            BWT.append(read_string[SA[i][1]-1])
        else:
            BWT.append("$")
    BWT_STR = ""
    for char in BWT:
        BWT_STR += char
    outfile.write(BWT_STR)
    outfile.write("\n")
    runs = 1 if len(BWT_STR) != 0 else 0
    longest_run = 0
    current_run = 1 if len(BWT_STR) != 0 else 0
    for i in range(1, len(BWT_STR)):
        if BWT_STR[i] != BWT_STR[i - 1]:
            runs += 1
            if longest_run < current_run:
                longest_run = current_run
            current_run = 1
        else:
            current_run += 1
    if longest_run < current_run:
        longest_run = current_run
    RATIO_STR = str(len(BWT_STR)) + ":" + str(runs)
    outfile.write(RATIO_STR)
    outfile.write("\n")
    outfile.write(str(longest_run))
    outfile.write("\n")
        
        
        
        
        