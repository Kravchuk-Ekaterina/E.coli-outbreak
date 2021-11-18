seq = ''
with open('../assembly2/scaffolds.fasta') as scaffolds:
    seq = scaffolds.read()
seq = ''.join(seq.split('\n')[1:])
print(seq[291457:292994])
print(seq[333038:334575])
print(seq[906257:907794])
