import sys

# Get the filenames from command line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

read_counter = 1
low_read = (0, sys.maxsize)
high_read = (0, 0)
l_10 = 0
ge_30 = 0
non_ATCG = 0

# Open the input file for reading and output file for writing
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    while True:
        # Read 4 lines at a time
        name = infile.readline().strip()    # 1st line
        sequence = infile.readline().strip()  # 2nd line
        p = infile.readline().strip()         # 3rd line
        base_q = infile.readline().strip()    # 4th line
        
        # Break if end of file is reached (no more lines to read)
        if not name or not sequence or not p or not base_q:
            break 
        
        q_sum = 0
        for char in base_q:
            q = ord(char) - 33
            q_sum += q
            if q < 10:
                l_10 += 1
            if q >= 30:
                ge_30 += 1
                
        if q_sum < low_read[1]:
            low_read = (read_counter, q_sum)
        if q_sum > high_read[1]:
            high_read = (read_counter, q_sum)
            
        for char in sequence:
            if char not in "ATCG":
                non_ATCG+=1
        
        read_counter+=1
    
    outfile.write(str(low_read[0]))
    outfile.write(str(" "))
    outfile.write(str(high_read[0]))
    outfile.write(str(" "))  
    outfile.write(str(l_10))  
    outfile.write(str(" "))
    outfile.write(str(ge_30))    
    outfile.write(str(" "))
    outfile.write(str(non_ATCG))  

            
            
            
        