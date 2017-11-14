import xmltodict

with open('faxml.xml') as file:
    context = file.read()
    dict = xmltodict.parse(context)

stationslijst = dict['Stations'] ['Station']

print('Dit zijn de codes en types van de 4 stations:')
for station in stationslijst:
    print('{0:4} - {1:4}'.format(station['Code'],station['Type']))

print('\nDit zijn alle stations met één of meer synoniemen:')
for station in stationslijst:
  if station['Synoniemen'] != None:
      for synoniem in station['Synoniemen']['Synoniem']:
          syno = []
          if synoniem in station:
              syno.append(synoniem)
          print(syno, '-', station)

print('\nDit is de lange naam van elk station:')
for station in stationslijst:
    print('{0:4} - {1:8}'.format(station['Code'],station['Namen'] ['Lang']))
