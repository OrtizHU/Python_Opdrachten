def gemiddelde():
    zin = input('Type een zin: ').split()
    for woord in zin:
        aantal = len(zin)
        lengte = len(woord)
        gem = lengte/aantal
    print('De gemiddelde lengte van het woord is: ', gem)

gemiddelde()
