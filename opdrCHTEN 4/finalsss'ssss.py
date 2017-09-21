#made by Ruben Horstman

leeftijd = int(input('leeftijd:'))
afstandKM =float(input('geef het aantal KM:'))
weekendrit = input('reist u door de week?:')

def standaardprijs(afstandKM):
    if afstandKM >= 50:
        return float(afstandKM*0.60)

    if afstandKM < 50:
        return float(afstandKM* 0.80)

    if afstandKM == 0:
        return(0)

def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs = standaardprijs(afstandKM)
    if leeftijd <= 12 or leeftijd > 65:
        if weekendrit == 'ja':
            return (prijs/100*70)
        else:
            return (prijs/100*65)
    else:
        if weekendrit == 'ja':
            return (prijs/100*60)
        else:
            return (prijs/100*65)
print('De prijs van uw reis bedraagd' + ' ' + str(ritprijs(leeftijd, weekendrit, afstandKM)) + ' ' + 'Euro')

