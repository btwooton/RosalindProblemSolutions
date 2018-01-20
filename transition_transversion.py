import rna_splice

def num_transitions(seq1, seq2):

    """
    Takes in two DNA strings and returns the number of
    transition point mutations between the two sequences
    The sequences are assumed to be of the same length
    """

    result = 0
    i = 0
    
    while i < len(seq1):
        if seq1[i] == 'A' and seq2[i] == 'G':
            result += 1
        elif seq1[i] == 'G' and seq2[i] == 'A':
            result += 1
        elif seq1[i] == 'C' and seq2[i] == 'T':
            result += 1
        elif seq1[i] == 'T' and seq2[i] == 'C':
            result += 1
        i += 1

    return result

def num_transversions(seq1, seq2):

    """
    Takes in two DNA strings of equal length and returns
    the number of transversion point mutations between the
    two sequences
    """

    result = 0
    i = 0

    while i < len(seq1):
        if seq1[i] in 'AG' and seq2[i] in 'CT':
            result += 1
        elif seq1[i] in 'CT' and seq2[i] in 'AG':
            result += 1
        i += 1

    return result

def transition_transversion_ratio(seq1, seq2):

    """
    Takes in two DNA strings of equal length and returns
    the transition/transversion ratio of the two sequences
    """

    return num_transitions(seq1, seq2) / num_transversions(seq1, seq2)

def main():

    in_file = open('input.txt', 'r')
    out_file = open('output.txt', 'w')

    fasta_list = rna_splice.read_fasta(in_file)

    seq1 = fasta_list[0][1]
    seq2 = fasta_list[1][1]

    out_file.write(str(transition_transversion_ratio(seq1, seq2)))


if __name__ == '__main__':
    main()
