# Import the sys module to access command-line arguments
import sys
# This module is for your reference to understand the usage
if len(sys.argv) != 3:
    print("Usage: python3 hw1q1b.py <input_file> <output_file>")
    sys.exit(1)
# Assign the input and output filenames from command-line arguments
input_file = sys.argv[1] # First argument: input filename
output_file = sys.argv[2] # Second argument: output filename

codon_map = {
    "UUU":"F",
    "UUC":"F",
    "UUA":"L",
    "UUG":"L",
    "UCU":"S",
    "UCC":"S",
    "UCA":"S",
    "UCG":"S",
    "UAU":"Y",
    "UAC":"Y",
    "UAA":"*",
    "UAG":"*",
    "UGU":"C",
    "UGC":"C",
    "UGA":"*",
    "UGG":"W",
    "CUU":"L",
    "CUC":"L",
    "CUA":"L",
    "CUG":"L",
    "CCU":"P",
    "CCC":"P",
    "CCA":"P",
    "CCG":"P",
    "CAU":"H",
    "CAC":"H",
    "CAA":"Q",
    "CAG":"Q",
    "CGU":"R",
    "CGC":"R",
    "CGA":"R",
    "CGG":"R",
    "AUU":"I",
    "AUC":"I",
    "AUA":"I",
    "AUG":"M",
    "ACU":"T",
    "ACC":"T",
    "ACA":"T",
    "ACG":"T",
    "AAU":"N",
    "AAC":"N",
    "AAA":"K",
    "AAG":"K",
    "AGU":"S",
    "AGC":"S",
    "AGA":"R",
    "AGG":"R",
    "GUU":"V",
    "GUC":"V",
    "GUA":"V",
    "GUG":"V",
    "GCU":"A",
    "GCC":"A",
    "GCA":"A",
    "GCG":"A",
    "GAU":"D",
    "GAC":"D",
    "GAA":"E",
    "GAG":"E",
    "GGU":"G",
    "GGC":"G",
    "GGA":"G",
    "GGG":"G"
}
codon_tracker = {
    "A":0,
    "C":0,
    "D":0,
    "E":0,
    "F":0,
    "G":0,
    "H":0,
    "I":0,
    "K":0,
    "L":0,
    "M":0,
    "N":0,
    "P":0,
    "Q":0,
    "R":0,
    "S":0,
    "T":0,
    "V":0,
    "W":0,
    "Y":0,
}

codon = ""
with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
    for line in in_file:
        for char in line:
            if char in "CTAGU":
                codon += char
                if len(codon) == 3:
                    codon_index = codon_map[codon]
                    if codon_index.isalpha():
                        codon_tracker[codon_index] += 1
                    codon = ""
    c = 0
    for val in codon_tracker.values():
        if c != 0:
            out_file.write(",")
        out_file.write(str(val))
        c+=1