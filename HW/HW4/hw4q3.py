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
    
    for line in infile:
        parts = line.strip().split()
        if len(parts) == 3:
            id_a, overlap, id_b = parts
            bmr[id_a] = (id_b, int(overlap))
            if bml[id_b][1] < int(overlap):
                bml[id_b] = (id_a, int(overlap))
            elif bml[id_b][1] == int(overlap) and bml[id_b][0]>id_a:
                bml[id_b] = (None, int(overlap))

    unitigs = []

    seen = set()

    for bmr_key in bmr:
        if bmr_key in seen:
            continue
        
        current_unitig = []
        current_read = bmr_key
        
        seen.add(current_read)
        
        if current_read != None and current_read not in bml: #confirm that current read is not in the middle of a chain
            current_unitig.append(current_read)
            while current_read in bmr: #follow the rest of the chain
                next_read, overlap_len = bmr[current_read]
                if next_read in bml and bml[next_read][0] == current_read:
                    current_unitig.append((overlap_len, next_read))
                    seen.add(next_read)
                    current_read = next_read
                else:
                    break
            unitigs.append(current_unitig)

    unitigs.sort(key=lambda x: x[0])

    for unitig in unitigs:
        outfile.write(f"{unitig[0]}\n")
        for overlap_len, read_id in unitig[1:]:
            outfile.write(f"{overlap_len} {read_id}\n")