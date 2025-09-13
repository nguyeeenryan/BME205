import sys


amino_to_mass = {
    "G":57, "A":71, "S":87, "P":97, "V":99,
    "T":101, "C":103, "I":113, "L":113, "N":114, 
    "D":115, "K":128, "Q":128, "E":129, "M":131,
    "H":137, "F":147, "R":156, "Y":163, "W":186
}

def peptide_mass_calc(peptide):
    '''returns mass of peptide by giving the sum of the masses of its amino acids'''
    mass = 0
    for amino in peptide:
        if amino in amino_to_mass.keys():
            mass += amino_to_mass[amino]
        
    return mass


def cyclic_fragment(string):
    '''splits a provided string into fragments in a cyclic fashion,
        that is at every possible connecting bond'''   
    fragments = []
    
    str_len = len(string)
    string_cycle = string + string # LEQN + LEQN = LEQNLEQN lets me cycle over when im iterating
    
    for x in range(str_len):
        for y in range(1,str_len):    
            fragments.append(string_cycle[x:x+y])
    
    return fragments


def cyclospectrum(peptide):
    '''returns the masses of all possible subpeptides in a cyclic peptide'''
    spectrum = [0, peptide_mass_calc(peptide)]
    
    pep_len = len(peptide)
    
    combos = cyclic_fragment(peptide)
                    
    for x in combos:
        spectrum.append(peptide_mass_calc(x))

        
    return sorted(spectrum, key=lambda x: x)
        
        
    

def main(inFile=None, options=None):
    sequence = ''
    amino = ''

    file_lines = []
    for line in sys.stdin:
        file_lines.append(line.strip())

    sequence = file_lines[0]

    spectrum = cyclospectrum(sequence)

    s = ' '.join(repr(item) for item in spectrum)
    print(s)



if __name__ == "__main__":
    main()
