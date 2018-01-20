import unittest
import rna_splice

class SpliceDNA(unittest.TestCase):

    def test_splice_dna(self):

        input_lst = [
                ('>Rosalind_1', 'AAAAAATGCTGAAAAAAAAAAAAAGCCATGCAAAAAA'),
                ('>Rosalind_2', 'ATGCTGA'),
                ('>Rosalind_3', 'GCCATGCA')
                ]
        result = rna_splice.splice_dna(input_lst)

        self.assertEqual(result, 'AAAAAAAAAAAAAAAAAAAAAA')

class ReadFASTA(unittest.TestCase):

    def test_read_fasta(self):

        in_file = open('fasta_test.txt', 'r')

        result = rna_splice.read_fasta(in_file)

        self.assertEqual(
                result, 
                [('>Rosalind_1', 'ATGCA'), ('>Rosalind_2', 'ATGCATGGACTGA'),
                    ('>Rosalind_3', 'AAATTA')]
                )
        in_file.close()

if __name__ == '__main__':
    unittest.main()
