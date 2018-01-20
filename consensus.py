def read_fasta(in_file):
    """ (text_file) -> dict{str: str}

    Reads in a file containing at most 10 DNA strings of equal length
    in FASTA format and returns a dictionary where the key is the FASTA label
    and the value is the corresponding DNA string

    """

    result = {}

    strings = []

    i = 0

    build_string = ""

    for line in in_file:
        if line.find('>') == 0:
            if build_string != "":
                strings.append(build_string)
                build_string = ""
            strings.append(line.rstrip())
        else:
            build_string += line.rstrip()
    strings.append(build_string)
    
    while i < len(strings) - 1:
        result[strings[i]] = strings[i + 1]
        i += 2
    return result


def profile_matrix(dna_strings):
    """ (dict{str: str}) -> dict{char: [int]}

    Reads in a dictionary where the key is the FASTA label and the value is its
    corresponding DNA string. Returns a dictionary where the key is one of ATCG
    and the value is a list of the occurences of each bases at the given position
    in all of the strings combined. Returns the "profile matrix" of the strings

    """

    result = { 'A': [], 'C': [], 'G': [], 'T': [] }

    i = 0
    key_list = list(dna_strings)
    while i < len(dna_strings[key_list[0]]):
        result['A'].append(0)
        result['C'].append(0)
        result['G'].append(0)
        result['T'].append(0)
        i += 1

    for key in dna_strings:
        i = 0
        for char in dna_strings[key]:
            result[char][i] += 1
            i += 1

    return result
    
def print_profile_matrix(profile_matrix, out_file = None):
    """ (dict{char: [int]}) -> IO

    Reads in the profile matrix for a collection of n length DNA strings
    and prints out the profile matrix so that it is nicely formatted

    """
    if out_file == None:
        for key in profile_matrix:
            print(key + ':', end=' ')
            for count in profile_matrix[key]:
                print(count, end=' ')
            print()
    else:
        for key in profile_matrix:
            out_file.write(key + ':' + ' ')
            for count in profile_matrix[key]:
                out_file.write(str(count) + ' ')
            out_file.write('\n')


def consensus_string(profile_matrix):
    """ (dict{char: [int]}) -> str

    Reads in the profile matrix for a collection of n length DNA strings and returns
    the corresponding consensus DNA string

    """

    length = len(profile_matrix['A'])

    i = 0

    result = ""

    while i < length:
        numA = profile_matrix['A'][i]
        numC = profile_matrix['C'][i]
        numG = profile_matrix['G'][i]
        numT = profile_matrix['T'][i]

        if max(numA, numC, numG, numT) == numA:
            result += 'A'
        elif max(numA, numC, numG, numT) == numT:
            result += 'T'
        elif max(numA, numC, numG, numT) == numC:
            result += 'C'
        elif max(numA, numC, numG, numT) == numG:
            result += 'G'

        i += 1

    return result

    
def main():

    in_file = open('input.txt', 'r')

    out_file = open('output.txt', 'w')

    fasta_dict = read_fasta(in_file)

    p_matrix = profile_matrix(fasta_dict)

    out_file.write(consensus_string(p_matrix) + '\n')

    print_profile_matrix(p_matrix, out_file)

    in_file.close()
    out_file.close()

if __name__ == '__main__':
    main()
