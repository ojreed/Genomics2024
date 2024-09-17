import sys
from collections import defaultdict

# Get the filenames from command line arguments
k_file = sys.argv[2]
input_file = sys.argv[1]
output_file = sys.argv[3]

index = defaultdict(list)

# Open the input file for reading and output file for writing
with open(input_file, 'r') as infile, open(k_file, 'r') as k_txt, open(output_file, 'w') as outfile:
    k = int(k_txt.read())
    infile.readline()
    DNA = infile.read().replace('\n', '')
    for i in range(len(DNA)-k+1):
        k_mer = DNA[i:i+k]
        index[k_mer].append(i)

    solo_keys = 0
    for key in index.keys():
        if len(index[key]) == 1:
            solo_keys += 1

    outfile.write(str(len(index.keys())))
    outfile.write(str(" "))
    outfile.write(str(solo_keys))
    print(index.keys())
    