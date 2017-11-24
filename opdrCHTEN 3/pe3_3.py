leeftijd = eval(input('Geef je leeftijd: '))
paspoort = (input('Nederlands paspoort: '))
antwoord = ('ja')
if leeftijd >= 18:
    print('je bent ouder dan achttien')
    if paspoort == antwoord:
        print('gefeliciteerd, je mag stemmen')
    else:
        print('je mag niet stemmen')
else:
    print('je mag niet stemmen')
