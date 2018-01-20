import rna_splice

def generate_adjacency_list(fasta_list):

    """
    Takes in a list of tuples produced by the read_fasta()
    procedure defined in rna_splice and produces the corresponding
    adjacency list for the overlap graph O3. The adjacency list
    will be structured as a list of tuples.
    """

    adjacencies = []

    for label1, sequence1 in fasta_list:
        for label2, sequence2 in fasta_list:
            l = len(sequence1)
            if label1 != label2 and sequence1[l - 3:l:] == sequence2[0:3:]:
                adjacencies.append((label1, label2))
    return adjacencies

def main():

    in_file = open('input.txt', 'r')

    fasta_list = rna_splice.read_fasta(in_file)

    adjacency_list = generate_adjacency_list(fasta_list)

    out_file = open('output.txt', 'w')

    for label1, label2 in adjacency_list:
        out_file.write(label1 + ' ' + label2 + '\n')

    in_file.close()
    out_file.close()


if __name__ == '__main__':
    main()
