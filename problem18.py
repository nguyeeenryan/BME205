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


def expand(peptides):
    expanded = set()
    
    for pep in peptides:
        for amino in amino_to_mass.keys():
            new_pep = pep + amino
            expanded.add(new_pep)
            
    return expanded
        

def cyclopeptide_sequencing(spectrum):
    candidates = {''}
    final_peptides = []

    spectrum = [int(x) for x in spectrum]
    parent_mass = max(spectrum)
    
    #Follows the algorithm given by rosalind problem 18
    while candidates:
        candidates = expand(candidates)
        candidates_copy = candidates.copy()
        for pep in candidates_copy:

            pep_mass = peptide_mass_calc(pep)
            if pep_mass == parent_mass:
                if (cyclospectrum(pep) == spectrum) and (pep not in final_peptides):
                    final_peptides.append(pep)

                candidates.remove(pep)
            elif pep_mass not in spectrum:
                candidates.remove(pep)
    
    return final_peptides

def mass_string(peptide):
    string = []
    for x in peptide:
        string.append(str(peptide_mass_calc(x)))
    
    return "-".join(string)


def main(inFile=None, options=None):
    file_lines = []
    for line in sys.stdin:
        file_lines.append(line.strip())

    spectrum = file_lines[0]
    spectrum = spectrum.split(' ')

    sequenced = cyclopeptide_sequencing(spectrum)

   
    amino_mass_string_list = set()
    for x in sequenced:
        amino_mass_string_list.add(mass_string(x))

    print(' '.join(amino_mass_string_list))

if __name__ == "__main__":
    main()
