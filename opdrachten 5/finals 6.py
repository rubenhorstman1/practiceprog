
maximaal = 12
def lees_bestand():
    infile = open('kaartnummers.txt', 'r')
    lines = infile.readlines()
    infile.close()
    kluizen = []
    for line in lines:
        gesplist = line.strip().split(';')
        kluis = [int(gesplist[0]), gesplist[1]]
        kluizen.append(kluis)
    return kluizen

def schrijf_bestand(kluizen):
    filewrite = open('kaartnummers.txt', 'a')
    str1 = ','.join(str(x) for x in kluizen)
    filewrite.write(str1+'\n')
    filewrite.close()

def kluis_openen():
    vul1 = int(input('vul uw kluis in: '))
    vul2 = input('vul uw code in: ')
    kluizen = lees_bestand()
    for kluis in kluizen:
        if kluis[0] == vul1 and kluis[1] == vul2:
            print('je mag je kluis in')
            break
        else:
            print('error')

def nieuwe_kluis():
    kluizen = lees_bestand()
    integeven_kluizen = [1,2,3,4,5,6,7,8,9,10,11,12]
    maximaal = 12
    geef_wachtwoord = input('welk wachtwoord wilt u?')
    if len(kluizen) < maximaal:
        for kluis in kluizen:
            integeven_kluizen.remove(kluis[0])
        kluisje = []
        kluisje.append(integeven_kluizen[0])
        wachtwoord = geef_wachtwoord
        kluisje.append(wachtwoord)
        print(kluisje)
        schrijf_bestand(kluisje)
    else:
        print('geen kluis beschrikbaar')

def toon_aantal_kluizen_vrij():
    kluizen = lees_bestand()
    print('Er zijn nog' + ' '+ str(maximaal- len(kluizen)) + ' ' + 'kluisjes beschrikbaar')

while True:
    print('1: Ik wil weten hoeveel kluizen nog vrij zijn ')
    print('2: Ik wil een nieuwe kluis ')
    print('3: Ik wil even iets uit mijn kluis halen ')
    print('stop')

    keuze = eval(input('Uw keuze: '))
    if keuze == 1:
        toon_aantal_kluizen_vrij()
    elif keuze == 2:
        nieuwe_kluis()
    elif keuze == 3:
        kluis_openen()
    else:
        print('error')