import csv

with open('94.csv', 'r') as file:
    bestand_94 = csv.DictReader(file,delimiter=';')
    rowprijs = 0
    rowvoorraad = []
    rownaam = ''
    rowartikel = []
    for row in bestand_94:
        if float(row['Prijs'])>rowprijs:
             rowprijs = float(row['Prijs'])
             rownaam = row['Naam']
        rowvoorraad.append(int(row['Voorraad']))
        rowartikel.append(int(row['Artikelnummer']))
    min_voorraad = min(rowvoorraad)
    index_minV = rowvoorraad.index(min_voorraad)


    print('Het duurste artikel is {} en die kost {:.2f} euro'.format(rownaam,rowprijs))
    print('Er zijn slechts {} examplaren in voorraad van het product met nummer {}'.format(min_voorraad,rowartikel[index_minV]))
    print('In totaal hebben wij {} producten in one magazijn liggen'.format(sum(rowvoorraad)))
