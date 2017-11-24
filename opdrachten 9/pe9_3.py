import csv
with open('scores.csv') as csvfile:
    reader = csv.reader(csvfile,   delimiter=';')
    for regel in reader:
        if regel[2] == 69:
            print(regel[1:2])
        else:
            print(regel[2])




