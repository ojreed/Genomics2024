import sys
from collections import defaultdict

# Get the filenames from command line arguments
temp_file = sys.argv[1]
pat_file = sys.argv[2]
output_file = sys.argv[3]

index = defaultdict(list)

hit_map = set()
hits = 0
best_read = []

# Open the input file for reading and output file for writing
with open(temp_file, 'r') as tfile, open(pat_file, 'r') as pfile, open(output_file, 'w') as outfile:
    #build index
    k = 6
    tfile.readline()
    input_string = "".join(tfile.readlines())
    DNA = "".join(x for x in input_string if x in "ACTG")
    # DNA = tfile.read().replace('\n', '')
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
       
        k_mer = sequence[0:k]
        local_hits = []
        if k_mer in index.keys():
            for i in index[k_mer]:
                if len(sequence) + i <= len(DNA) and sequence[k:] == DNA[i+k:i+len(sequence)]:
                    hits += 1
                    local_hits.append(i)
                    hit_map.add((sequence,i))
                    
        if len(best_read) < len(local_hits) or (len(best_read) > 0 and len(best_read) == len(local_hits) and local_hits[0]< best_read[0]):
            best_read = local_hits
    
    print(hit_map)
    
    max_len = max(len(v) for v in index.values())
    max_keys = [k for k, v in index.items() if len(v) == max_len]
    max_keys.sort()
    best_str = ','.join(max_keys)
    hits = len(hit_map)
    print(best_str)
    print(hits)
    print(best_read[0])

    outfile.write(str(best_str))
    outfile.write(str(" "))
    outfile.write(str(hits))
    outfile.write(str(" "))
    outfile.write(str(best_read[0]))
            

    
    