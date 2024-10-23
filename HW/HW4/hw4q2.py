import sys
from collections import defaultdict

def suffix_prefix_match(str1, str2, min_overlap):
    if len(str2) < min_overlap:
        return 0
    str2_prefix = str2[:min_overlap]
    str1_pos = -1
    while True:
        str1_pos = str1.find(str2_prefix, str1_pos + 1)
        if str1_pos == -1:
            return 0
        str1_suffix = str1[str1_pos:]
        if str2.startswith(str1_suffix):
            return len(str1_suffix)


def make_kmer_table(seqs, k):
    """ Given read dictionary and integer k, return a dictionary that
    maps each k-mer to the set of names of reads containing the k-mer. """
    table = {}
    for name, seq in seqs.items():
        for i in range(0, len(seq) - k + 1):
            kmer = seq[i:i+k]
            if kmer not in table:
                table[kmer] = set()
            table[kmer].add(name)
    return table


if len(sys.argv) != 4:
    print("Incorrect Command Line INput")
    sys.exit(1)

input_file = sys.argv[1]
K = int(sys.argv[2])
output_file = sys.argv[3]


with open(input_file, 'r') as qfile, open(output_file, 'w') as outfile:
    id_to_string = defaultdict(str)
    while True:
        name = qfile.readline().strip()      # 1st line
        sequence = qfile.readline().strip()  # 2nd line
        p = qfile.readline().strip()         # 3rd line
        base_q = qfile.readline().strip()    # 4th line
        id_to_string[name[1:]] = sequence
        
        if not name or not sequence or not p or not base_q:
            break 
        

    kmer_table = make_kmer_table(id_to_string, K)
    res = []
    
    for id_a, seq_a in id_to_string.items():
        b_match = (None,0)
                
        potential_matches = set()
        for i in range(len(seq_a) - K + 1):
            kmer = seq_a[i:i + K]
            if kmer in kmer_table:
                potential_matches.update(kmer_table[kmer])
        potential_matches.discard(id_a)
        
        for id_b in potential_matches:
            seq_b = id_to_string[id_b]
            if id_a != id_b:
                len_same = suffix_prefix_match(seq_a,seq_b,K)
                if len_same > b_match[1]:
                    b_match = (id_b, len_same)
                elif ( len_same == b_match[1]):
                    b_match = (None, len_same)
                    
        if b_match[0] != None:
            res.append(f"{id_a} {b_match[1]} {b_match[0]}")
                    
    res.sort()

    outfile.write("\n".join(res) + "\n")