age = input('leeftijd:')
KM = int(input('geef het aantal KM:'))
week = input('reist u door de week?:')
antwoord ='ja'
prijs = int(KM* 0.80)
standaard =int(KM*0.60)
kortingprijs = prijs/100*30
nprijs = prijs/100*35
if KM >= 50:
    print(standaard)
else:
    print(prijs)
def ritprijs(leeftijd, weekendrit, afstandKM):
    if