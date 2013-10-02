class DNASequence:
    def __init__(self, sequence):
        self.sequence = sequence.lower()
    
    def base_count(self, base):
        basel = base.lower()
        return self.sequence.count(basel)
    
    def gc_content(self):
        Gs = self.sequence.count('g')
        Cs = self.sequence.count('c')
        GC = float(Gs + Cs)/len(self.sequence)
        return GC, 'proportion GC'
    
    def reverse_complement(self):
        rev = self.sequence[::-1]
        complements = {'g': 'c', 'c': 'g', 'a': 't', 't': 'a'}
        rev_c = ""
        for base in self.sequence:
            rev_c = complements[base] + rev_c
            
        return rev_c


