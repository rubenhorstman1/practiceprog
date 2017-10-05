invoer = '5-9-7-1-7-8-3-2-4-8-7-9'
words = invoer.split('-')
words.sort()
print('dit is de lijst' + ' ' + str(words))
print('grootste getal ' + ' ' + max(words) + ' ' +' kleinste getal' + ' ' + min(words))
print('aantal getallen' + ' ' +str(len(words)) + ' ' + words)
print()
