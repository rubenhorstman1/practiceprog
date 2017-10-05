import datetime

infile = open('kaartnummers.txt', 'w')
infilewrite = open('kaartnummers.txt', 'a')
infileread = open('kaartnummers.txt', 'r')


vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y ")
s1 = vandaag.strftime('%H:%M:%S')
mens = 0
maximaal = 6
for mens in range(1, maximaal, +1):
    hardlopers = input('vul de naam van de harloper in: ')
    if mens < maximaal:
        print(hardlopers+ s + s1)
    infilewrite.write(hardlopers+ ' ' +  s +' '+ s1)





