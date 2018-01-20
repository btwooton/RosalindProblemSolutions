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

def get_gc_content(dictionary):
    """(dict{str : str}) -> dict{str : float}

    Takes in a dictionary containing mappings for FASTA labels to 
    DNA strings and computes the GC content for those DNA strings
    Returns a new dictionary containing mappings for the FASTA labels
    to their appropriate GC contents
    """

    result = {}

    for label, strand in dictionary.items():
        count = 0

        for base in strand:
            if base == 'C' or base == 'G':
                count += 1

        result[label] = (count / len(strand)) * 100

    return result


def main():
    f = open('rosalind_gc.txt', 'r');

    table = read_fasta(f)

    gc_counts = get_gc_content(table)

    max_label = ""
    max_content = 0
    for label, gc_content in gc_counts.items():
        if max_label == "":
            max_label = label
            max_content = gc_content
        elif gc_content > max_content:
            max_label = label
            max_content = gc_content
    print(max_label)
    print(max_content)

if __name__ == '__main__':
    main()


