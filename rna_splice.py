from translate import translate 


def read_fasta(f):
    """
    file -> list
    Reads in a text file in fasta format and returns
    a list of tuples with the fasta label as the first
    value and the DNA sequence as the second value
    """
    tags = []
    sequences = []
    sequence = ""

    for line in f:
        if line.startswith('>'):
            tags.append(line.rstrip('\n').lstrip('>'))
            if sequence != "":
                sequences.append(sequence)
                sequence = ""
        else:
            sequence += line.rstrip('\n')
    sequences.append(sequence)

    return list(zip(tags, sequences))


def splice_dna(sequences):
    """
    [(label, sequence)] -> spliced_sequence
    Takes in a list of tuples of fasta labels and
    DNA sequences and returns the spliced DNA sequence
    with introns removed as a result
    """
    unspliced = sequences[0][1]

    for label, sequence in sequences[1::]:
        while unspliced.find(sequence) != -1:
            index = unspliced.find(sequence)
            unspliced = unspliced[0:index] + unspliced[index + len(sequence)::]
    
    return unspliced

def transcribe_dna(sequence):
    """
    DNA -> RNA
    Takes in a string representing a DNA sequence
    and transcribes it, returning an RNA string
    """

    result = ""
    
    for base in sequence:
        if base == 'T':
            result += 'U'
        else:
            result += base
    return result

def main():

    in_file = open('rosalind_splc.txt', 'r')
    out_file = open('protein.txt', 'w')

    data = read_fasta(in_file)
    spliced = splice_dna(data)
    result = translate(transcribe_dna(spliced))
    out_file.write(result)

    in_file.close()
    out_file.close()

if __name__ == '__main__':
    main()



        
