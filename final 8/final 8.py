treintraject = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

def inlezen(treintraject):
    while True:
        vertrek = input('geef de naam van het vertekstation:')
        if vertrek in treintraject:
            print('het vertrek station is' + ' ' + vertrek)
            return treintraject.index(vertrek)
        elif vertrek not in treintraject:
            print('Dit station klopt niet.')

def uitlezen(beginstation):
    while True:
        eindpunt = input('geef de naam van het eindstation:')
        if eindpunt in treintraject:
            index = treintraject.index(eindpunt)
            if index > beginstation:
                print('Het eindstation is' + ' ' + eindpunt)
                return index
            else:
                print('beginstation is na eindstation')
        else:
            print('dit is geen mogelijkheid')


def omroepreizen(stations, beginstation, eindstation):
    print('Het beginstation is',  stations[beginstation], ' is het', beginstation, 'nummer in de rij van stations')
    print('Het eindstation is',  stations[eindstation], 'is het', eindstation, 'nummer in de rij van stations')
    print('de afstand is', eindstation - beginstation, 'stations')
    print('de prijs van het kaartje',  (eindstation - beginstation)*5, 'euro')
    print('jij stapt in de trein', stations[beginstation])
    for aantal in range(beginstation+1, eindstation):
        print('-', stations[aantal])
    print('jij stapt uit in', stations[eindstation])

beginstation = inlezen(treintraject)
eindstation = uitlezen(beginstation)
omroepreizen(treintraject, beginstation, eindstation)
