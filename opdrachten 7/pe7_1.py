getal = eval(input('je moet hier een getal ivullen: '))
maximaal = 100000
totaal = []
for getallen in range(1,maximaal, +1):
    if getal == 0:
        totaal.append(getal)
        print (sum(totaal))
        break
    else:
        getal = eval(input('je moet hier een getal ivullen:'))


