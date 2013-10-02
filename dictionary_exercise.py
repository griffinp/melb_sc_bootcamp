import sys
sequence = sys.argv[1]
Gs = sequence.count('G')
As = sequence.count('A')
Cs = sequence.count('C')
Ts = sequence.count('T')
Us = sequence.count('U')

print(Us)
if Us == 0:
    base_dictionary = {'A': As, 'C': Cs, 'G': Gs, 'T': Ts}
else: 
    base_dictionary = {'A': As, 'C': Cs, 'G': Gs, 'U': Us}

print(base_dictionary)
print(Gs+Cs)
print(len(sequence))
GC_content = float(Gs + Cs)/len(sequence)
print(GC_content, 'proportion GC')
