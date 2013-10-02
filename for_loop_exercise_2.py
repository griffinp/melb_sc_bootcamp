uniprot = open("uniprot_sprot.fasta")
number_human = 0
for i in uniprot.readlines():
    if i[0] == '>' and 'OS=Homo sapiens' in i:
        number_human+=1
    else:
        pass
print(number_human)
uniprot.close()
