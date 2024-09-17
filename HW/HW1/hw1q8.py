import sys
if len(sys.argv) != 3:
    print("Usage: python3 script.py <input_file> <output_file>")
    sys.exit(1)
# Assign the input and output filenames from command-line arguments
input_file = sys.argv[1] # First argument: input filename
output_file = sys.argv[2] # Second argument: output filename
# Read input from the file
with open(input_file, "r") as in_file:
    # Read the first line, remove whitespace from both ends
    a = in_file.readline().strip()

# a = "AGCAAATTTAAATTTAAACC"
    
tracker = {}

for i in range(len(a)-5):
    six = a[i:i+6]
    if six not in tracker.keys():
        tracker[six] = [0,[]]
    tracker[six][0] += 1
    tracker[six][1].append(i)

bk = None
bval = 0

for key in tracker.keys():
    if bk == None or tracker[key][0] > bval:
        bk = key
        bval = tracker[key][0]
    elif tracker[key][0] == bval:
        comp = [key,bk]
        comp = sorted(comp, key=lambda x: (x, len(x)))
        bk = comp[0]
        bval = tracker[comp[0]][0]

# print(tracker[bk][1])
c = 0
with open(output_file, "w") as out_file:
    for val in tracker[bk][1]:
        if c != 0:
            out_file.write(",")
        out_file.write(str(val))
        c+=1
        
    