def ticker(tickersymbols):
    with open(tickersymbols, 'r') as bestand:
        regels = bestand.readlines()
        ticker = {}
    for regel in regels:
        regel = regel.strip('\n')
        regel = regel.split(':')
        ticker[regel[0]] = regel[1]
    return ticker
