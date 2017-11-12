def inlezen_beginstation(stations):
    begin = input('Wat is je beginstation?')
    return inlezen_beginstation(stations)

def inlezen_eindstation(stations, beginstation):
    return

def omroepen_reis(stations, beginstation, eindstation):
    return

stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Amstel', 'Utrecht Centraal', '\'s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)

'menu'
print(beginstation)
print(input('Wat is je eindstation?'))
if format(eindstation) > format(beginstation):
    print('Het beginstation {} is het {} station in het traject.\nHet eindstation {} is het {} station in het traject.\nDe afstand bedraagt {} station(s).\nDe prijs van het kaartje is {} euro.')
else:
    print('Deze trein komt niet in {}'.format(stations))
