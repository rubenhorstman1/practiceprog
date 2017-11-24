dict1 = {'Yahoo': 'YHOO', 'Google': 'GOOG','Harley-Davidson': 'HOG', 'Yamana Gold': 'AUY', 'Sotheby’s': 'BID', 'inBev': 'BUD'}
def ticker(dict1):
    invul = input('enter company name:')
    for keys, value in dict1.items():
        if invul == keys:
            print('Ticker sybool:'+ ' ' + value)
            break
    invullen = input('enter ticket symbool:')
    for keys, value in dict1.items():
        if invullen == value:
            print('Company Name:' + ' ' +keys)
            break
ticker(dict1)