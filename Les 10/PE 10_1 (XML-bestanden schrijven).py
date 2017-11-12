import xmltodict

with open('10_1') as xmlfile:
    file = xmlfile.read()
    artikeldict = xmltodict.parse(file)
artikellijst = artikeldict['artikelen'] ['artikel']
for artikel in artikellijst:
    if artikel['naam'] is not None:
        print(artikel['naam'])
