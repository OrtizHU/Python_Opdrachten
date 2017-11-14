stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'AmsterdamCentraal', 'Amsterdam Amstel', 'Utrecht Centraal', 's-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

def inlezen_beginstation(stations):
    while True:
        global beginstation
        beginstation = input('Wat is je beginstation? : ')
        if beginstation in stations:
            return beginstation
        elif beginstation != stations:
            print('Deze trein komt niet in {}'.format(beginstation))
def inlezen_eindstation(stations, beginstation):
    while True:
        global eindstation
        eindstation = input('Wat is je eindstation? : ')
        if eindstation in stations:
            if stations.index(eindstation) > stations.index(beginstation):
                return eindstation
        elif eindstation != stations:
            print('Deze trein komt niet in {}'.format(eindstation))

def omroepen_reis(stations, beginstation, eindstation):
    print('Het beginstation {} is het {}e station in het traject'.format(beginstation, stations.index(beginstation) + 1))
    print('Het eindstation {} is het {}e station in het traject'.format(eindstation, stations.index(eindstation) + 1))
    rangnummer_bs = stations.index(beginstation)+1
    rangnummer_es = stations.index(eindstation)+1
    ritprijs = (rangnummer_es-rangnummer_bs)*5
    print('De afstand bedraagt {} station(s).'.format(rangnummer_es-rangnummer_bs))
    print('De prijs van het kaartje is {} euro.'.format(ritprijs))
    print('Jij stapt in de trein in:', beginstation)
    for i in range(rangnummer_bs, rangnummer_es):
        print(' -', stations[i])
    print('Jij stapt uit in:', eindstation)

print(inlezen_beginstation(stations))
print(inlezen_eindstation(stations,beginstation))
omroepen_reis(stations,beginstation,eindstation)
