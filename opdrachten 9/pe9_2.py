import datetime
import csv

bestand = 'inloggers.csv'
with open('inloggers.csv', 'w', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    writer.writerow(('voor1', 'name', 'gbdatum', 'email'))

    while True:
        naam = input("Wat is je achternaam? ")
        einde = 'einde'
        if naam == einde:
            break
        else:
            voorl = input("Wat zijn je voorletters? ")
            gbdatum = input("Wat is je geboortedatum? ")
            email = input("Wat is je e-mail adres? ")
            print(naam, ';', voorl, ';', gbdatum, ';', email)


