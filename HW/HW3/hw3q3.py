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
    BWT_P = []
    for i in range(len(read_string)):
        if SA[i][1] > 0:
            BWT_P.append(SA[i][1]-1)
        else:
            BWT_P.append(len(read_string)-1)
    for i in range(len(BWT_P)):
        outfile.write(str(BWT_P[i]))
        if i != len(BWT_P)-1:
            outfile.write(" ") 
    

        
        
        
        
        