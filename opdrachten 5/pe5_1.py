infile = open('kaartnummers.txt', 'r')
lines = infile.readlines()
infile.close()
aantalregels = len(lines)
print('deze file telt', aantalregels, 'regels')


hoogstekaartnummer = 0
regelnummer = 0
regel = 0

for regel in lines:
    regel += 1
    elements = lines.split(',')
    kaartnummer = int(element[0])
    if kaartnummer > hoogstekaartnummer:
        hoogstekaartnummer = kaartnumer
        regelnummer = regel
print('het grootste kaartnummer is', hoogstekaartnummer, 'en dat staat op regel', regelnummer)