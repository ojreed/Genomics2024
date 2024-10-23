import sys

if len(sys.argv) != 3:
    print("Incorrect Command Line INput")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r') as infile:
    T = infile.readline().strip()
    P = infile.readline().strip()
    
    
def LCS_len(T,P,m,n):
    if m == 0 or n == 0:
       return 0
    elif T[m-1] == P[n-1]:
       return 1 + LCS_len(T, P, m-1, n-1)
    else:
       return max(LCS_len(T, P, m, n-1), LCS_len(T, P, m-1, n))
   
with open(output_file, 'w') as outfile:
    outfile.write(f"{LCS_len(T,P,len(T),len(P))}\n")