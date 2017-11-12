import time

datum = time.strftime('%a %d %B %Y')
tijd = time.strftime('%I:%M:%S')
naam = input('Geef uw naam:')

with open('hardlopers.txt', 'a') as file:
    file.write('{}, {}, {}\n'.format(datum,tijd,naam))
