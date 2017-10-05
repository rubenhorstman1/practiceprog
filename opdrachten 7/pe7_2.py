maximaal = 10000
teksten = input('vul een string in van 4 letters: ')
for tekst in range(1, maximaal, +1):
    if len(teksten) != 4:
        tel = str(len(teksten))
        print(teksten + ' ' +'telt ' + tel + ' ' + 'letters')
        teksten = input('vul een string in van 4 letters:')
    else:
        print('Inlezen van correcte string'+ ' ' + teksten + ' ' +'is geslaagd!')
        break