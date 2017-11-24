import random

def dobbelen():
    while True:
        gooi = (random.randrange(1, 7) + (random.randrange(1, 7)))
        gooien = (random.randrange(1, 7) + (random.randrange(1, 7)))
        print(gooien)
        print(gooi)
        if gooi == gooien:
            randomd = (random.randrange(1, 7) + (random.randrange(1,7)))
            print(gooi + gooien)
            print('in totaal')
            print('je hebt dubbel gedobbeld')
            print(randomd)
            if randomd == gooien or randomd == gooi:
                print('je gaat gelijk naar de gevangenis!')
                break

dobbelen()