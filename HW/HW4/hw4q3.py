import sys
from collections import defaultdict


if len(sys.argv) != 3:
    print("Incorrect Command Line Input")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]



with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    bmr = defaultdict(lambda: (None, 0))
    bml = defaultdict(lambda: (None, 0))
    
    #get BMR and BML dicts 
    for line in infile.readlines():
        parts = line.strip().split()
        if len(parts) == 3:
            id_a, overlap, id_b = parts
            #setup BMRs
            if id_a not in bmr.keys():
                bmr[id_a] = (id_b, int(overlap))
            if id_b not in bml:
                bml[id_b] = (id_a, int(overlap))
            else:
                #ensures BMLs are only true BMLs
                if bml[id_b][1] < int(overlap):
                    bml[id_b] = (id_a, int(overlap))
                elif bml[id_b][1] == int(overlap):
                    bml[id_b] = (None, int(overlap))

    unitigs = []
    
    attached = set()
    non_leading = set()

    #pre process elements of chains
    for bmr_key in bmr:
        bml_of_bmr = bml[bmr[bmr_key][0]][0]
        if bmr_key == bml_of_bmr:
            non_leading.add(bmr[bmr_key][0])
            attached.add(bmr_key)
            
    # Assemble chains
    used = set()  
    for bmr_key in sorted(list(bmr.keys())):
        if bmr_key in used or bmr_key in non_leading or not bmr_key in attached:
            continue

        current_unitig = []
        current_read = bmr_key
        
        current_unitig.append(current_read)
        while current_read in bmr: #follow the rest of the chain
            next_read, overlap_len = bmr[current_read]
            if next_read in bml and bml[next_read][0] == current_read:
                current_unitig.append((overlap_len,next_read))
                used.add(next_read)
                current_read = next_read
            else:
                break
        unitigs.append(current_unitig)

    #print chains
    for unitig in unitigs:
        outfile.write(f"{unitig[0]}\n")
        for overlap_len, read_id in unitig[1:]:
            outfile.write(f"{overlap_len} {read_id}\n")