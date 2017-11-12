import time
import csv

with open('gegevens.csv', 'w',newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=':')
    writer.writerow(('datum','naam','voorletters','geboortedatum','email'))
    datum = time.strftime('%a %d %B %Y at %I:%M')
    while True:
       naam = input("Wat is je achternaam? ")
       if naam == 'einde':
         break
       voorl = input("Wat zijn je voorletters? ")
       gbdatum = input("Wat is u geboortedatum? ")
       email = input("Wat is u email? ")
       writer.writerow((datum,naam,voorl,gbdatum,email))
