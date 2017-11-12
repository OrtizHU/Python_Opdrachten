import csv
with open('93.csv', 'r',newline='') as file:
    read = csv.reader(file, delimiter=';')
    naam = ''
    datum = ''
    hoogstescore = 0

    for row in read:
        if int(row[2]) > hoogstescore:
            hoogstescore = int(row[2])
            datum = row[1]
            naam = row[0]

    print('De hoogste score: {} op {} behaald door {}'.format(hoogstescore,datum,naam))
