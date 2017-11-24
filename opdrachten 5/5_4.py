import datetime

infile = open('kaartnummers.txt', 'w')
infilewrite = open('kaartnummers.txt', 'a')
infileread = open('kaartnummers.txt', 'r')


vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y ")
s1 = vandaag.strftime('%H:%M:%S')

while True:
    for mensen in range(1, 6, +1):
        hardlopers = input('vul de naam van de harloper in: ')
        infilewrite.write(hardlopers + ' ' + ' ' + s + ' ' + s1)
        if mensen <= 6:
            print(hardlopers+ ' ' + s + s1)
        else:
            print('klaar')
            break







