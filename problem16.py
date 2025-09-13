import sys


DNA_Codons = {
    # 'M' - START, '_' - STOP
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TGT": "C", "TGC": "C",
    "GAT": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "TTT": "F", "TTC": "F",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAT": "H", "CAC": "H",
    "ATA": "I", "ATT": "I", "ATC": "I",
    "AAA": "K", "AAG": "K",
    "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATG": "M",
    "AAT": "N", "AAC": "N",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TGG": "W",
    "TAT": "Y", "TAC": "Y",
    "TAA": "_", "TAG": "_", "TGA": "_"
}

inv_DNA_Codons = {v: k for k, v in DNA_Codons.items()}




def reverse_c(seq):
    '''returns reverse compliment of provided sequence'''
    return seq[::-1].translate(str.maketrans('ACGTN', 'TGCAN'))

def frame_split(seq, frame=0):
    '''splits provided sequence into codons into given frame, default is frame 1'''
    return [seq[i+frame:i + 3 + frame] for i in range(0, len(seq), 3)]

def sequence_to_peptide(seq):
    '''translates a sequence into corresponding amino acid peptide'''
    amino = ''
    
    split_seq = frame_split(seq)
    for codon in split_seq:
        if codon in DNA_Codons.keys():
            amino += DNA_Codons[codon]   

    return amino


def find_amino_substrings(seq, peptide):
    '''provided a sequence of bases and a peptide, returns a list of all sub-sequences
        that translate into the given peptide'''
    substrings = []
    
    sequence = seq.upper()
    rev_sequence = reverse_c(sequence)
    peptide = peptide.upper()
    base_length = len(peptide) * 3

    for k in range(len(sequence) - base_length + 1):
        kmer = sequence[k:k+base_length]
        if sequence_to_peptide(kmer) == peptide:
            substrings.append(kmer)
    
    for k in range(len(rev_sequence) - base_length + 1):
        kmer = rev_sequence[k:k+base_length]
        if sequence_to_peptide(kmer) == peptide:
            substrings.append(reverse_c(kmer))

    return substrings

def main(inFile=None, options=None):
    sequence = ''
    amino = ''

    file_lines = []
    for line in sys.stdin:
        file_lines.append(line.strip())

    sequence = file_lines[0]
    amino = file_lines[1]

    substrings = find_amino_substrings(sequence, amino)

    for x in substrings:
        print(x)


if __name__ == "__main__":
    main()
