import sys
import numpy as np
import pandas as pd

def emi_prob(path, emi_path, emi_matrix):
    prob = 1
    
    for x in range(len(path)):
        state = path[x]
        emitted = emi_path[x]

        prob *= emi_matrix.loc[state, emitted]
    
    return prob



def main(inFile=None, options=None):
    lines = []

    for line in sys.stdin:
        lines.append(line.strip())

    path = lines[0]
    emi_path = lines[3]
    states = lines[4].split()
    emi_states = lines[2].split()
    emi_matrix = []
    

    for x in range(9,9+len(states)):
        emi_matrix.append(lines[x].split()[1:])

    emi_matrix_final = pd.DataFrame(emi_matrix, index=states, columns=emi_states).astype(float)

    print(emi_prob(path, emi_path,emi_matrix_final))

if __name__ == "__main__":
    main()
