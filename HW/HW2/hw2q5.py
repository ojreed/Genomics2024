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

template_to_pattern = defaultdict(set)

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
        
        if not name or not sequence or not p or not base_q:
            break 
        
        full_match = defaultdict(set)
        for i in range(0,len(sequence),6):
            k_mer_match = []
            k_mer = sequence[i:i+6]
            if k_mer in index.keys():
                for j in index[k_mer]:
                    allowance = 4
                    if (j - i >= 0 and j - i + len(sequence) <= len(DNA)):
                        for k in range(j - i,j - i + len(sequence)):
                            if DNA[k] != sequence[k - j + i]:
                                allowance -= 1
                        if allowance >= 0:
                            full_match[4-allowance].add(j - i)
                            for char_index in range(30):
                                template_to_pattern[j-i+char_index].add((sequence[char_index],base_q[char_index],sequence,base_q))

    # print(template_to_pattern)
    results = defaultdict(list)
    for key in template_to_pattern.keys():
        sequences = [list(template_to_pattern[key])[i][0] for i in range(len(template_to_pattern[key]))]
        base_qs = [list(template_to_pattern[key])[i][1] for i in range(len(template_to_pattern[key]))]
        ref_base = DNA[key]
        valid = True
        ACTG = defaultdict(int)
        for j in range((len(sequences))):
            ACTG[sequences[j]] += ord(base_qs[j]) - 33
        if max(ACTG, key=ACTG.get) == DNA[key]:
            valid = False
        nr_base = " " + max(ACTG, key=ACTG.get)
        if ACTG[max(ACTG, key=ACTG.get)] <= 20:
            valid = False
        nr_weight = ACTG[max(ACTG, key=ACTG.get)]
        ACTG[max(ACTG, key=ACTG.get)] = 0
        if ref_base != max(ACTG, key=ACTG.get) and ACTG[max(ACTG, key=ACTG.get)] > 20:
            nr_base2 = " " + max(ACTG, key=ACTG.get)
            nr_weight2 = ACTG[max(ACTG, key=ACTG.get)]
        else:
            nr_base2 = " -"
            nr_weight2 = 0
        if valid:
            outfile.write(str(key) + " " + ref_base + nr_base + " " + str(nr_weight) + nr_base2 + " " + str(nr_weight2))
            outfile.write("\n")