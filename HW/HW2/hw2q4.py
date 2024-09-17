import sys
from collections import defaultdict

# Get the filenames from command line arguments
temp_file = sys.argv[1]
pat_file = sys.argv[2]
output_file = sys.argv[3]

index = defaultdict(list)

hit_map = defaultdict(int)
hits = 0
best_read = []

# Open the input file for reading and output file for writing
with open(temp_file, 'r') as tfile, open(pat_file, 'r') as pfile, open(output_file, 'w') as outfile:
    #build index
    k = 6
    tfile.readline()
    DNA = tfile.read().replace('\n', '')
    for i in range(len(DNA)-k+1):
        k_mer = DNA[i:i+k]
        index[k_mer].append(i)

    #read patterns    
    while True:
        name = pfile.readline().strip()      # 1st line
        sequence = pfile.readline().strip()  # 2nd line
        p = pfile.readline().strip()         # 3rd line
        base_q = pfile.readline().strip()    # 4th line
        
        print(sequence)
        
        if not name or not sequence or not p or not base_q:
            break 
        
        full_match = defaultdict(set)
        output_hits = ""
        for i in range(0,len(sequence),6):
            k_mer_match = []
            k_mer = sequence[i:i+6]
            if k_mer in index.keys():
                output_hits = output_hits + str(len(index[k_mer])) + " "
                for j in index[k_mer]:
                    allowance = 4
                    if (j - i >= 0 and j - i + len(sequence) <= len(DNA)):
                        for k in range(j - i,j - i + len(sequence)):
                            if DNA[k] != sequence[k - j + i]:
                                allowance -= 1
                        if allowance >= 0:
                            full_match[4-allowance].add(j - i)
            else:
                output_hits = output_hits + "0 "
        output_full_match = ""
        for i in range(0, 5):
            if i in full_match:
                output_full_match += f"{i}:{','.join(map(str, sorted(full_match[i])))} "
            else:
                output_full_match += f"{i}: "
        print()
        outfile.write(output_hits+output_full_match)
        outfile.write(str("\n"))
                        
                        
    
                    
            
            

    
    