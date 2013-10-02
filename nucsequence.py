import string


class NucSequence:
    '''an abstract class of nucleotide sequence:
    not to be used directly.'''
    # the above 'docstring' will appear when help is called
    # on this class/method
    complements = {'g': 'c',
                   'c': 'g',
                   'a': 't',
                   't': 'a'}
    def __init__(self, sequence):
        assert isinstance(sequence, str)
        self.sequence = sequence.lower()
    
    def base_count(self, base):
        '''Returns the number of times 'base' appears
        in the sequence.'''
        basel = base.lower()
        return self.sequence.count(basel)
    tests = [
             ['AAACGCG', 'A', 3],
             ['aaacgtc', 'a', 3],
             ['CGGAUAA', 'U', 1]
             ]
    for seq, ba, expected_result in tests:
        assert base_count(seq, ba) == expected_result
    
    def gc_content(self):
        '''Returns the proportion GC content
        in the sequence.'''
        Gs = self.sequence.count('g')
        Cs = self.sequence.count('c')
        GC = float(Gs + Cs)/len(self.sequence)
        return GC, 'proportion GC'
    tests = [
             ['AAATCGCG', 0.5],
             ['aaauuauuuc', 0.1],
             ['CGCGCGCG', 1]
             ['AUAU', 0]
             ]
    for seq, expected_result in tests:
        assert gc_content(seq) == expected_result
    
    def reverse_complement(self):
        '''Returns the reverse complement of the sequence.'''
        rev = self.sequence[::-1]
        rev_c = ""
        for base in self.sequence:
            rev_c = complements[base] + rev_c
        return rev_c
    tests = [
             ['acgt', 'acgt'],
             ['AAAA', 'TTTT'],
             ['cgcgcaa', 'ttgcgcg'],
             ]
    for seq, expected_result in tests:
        assert reverse_complement(seq) == expected_result
class DNASequence(NucSequence):
    '''A specific DNA class - uses all the methods 
    defined in NucSequence.'''
    pass

#making a specific RNA class - needs a new method for rev comp
class RNASequence(NucSequence):
    '''A specific RNA class - takes its own base dictionary
    for reverse_complement.'''
    complements = {'g': 'c',
                   'c': 'g',
                   'a': 'u',
                   'u': 'a'}
    def __init__(self, sequence):
        NucSequence.__init__(self, sequence)
    tests = [
             ['acgu', 'acgu'],
             ['AAAA', 'UUUU'],
             ['cgcgcaa', 'uugcgcg'],
             ]
    for seq, expected_result in tests:
        assert reverse_complement(seq) == expected_result



