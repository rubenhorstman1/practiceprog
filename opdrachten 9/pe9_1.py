bedrag = 4356
try:
    personen = input('hoeveel personen gaan er mee op reis:')
    print(bedrag / int(personen))
except ZeroDivisionError:
    print('je kan niet door nul delen')
except ValueError:
    print('gebruik cijfers bij het invoeren')
except RecursionError:
    print('je kan niet door negatieve getallen delen')
except:
    print('onjuiste invoer')