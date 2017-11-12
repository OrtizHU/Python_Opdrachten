leeftijd = int(input('Geef je leeftijd: '))
paspoort = input('Nederlands paspoort?(ja/nee) ')
if leeftijd >= 18:
    if paspoort[0] == 'j':
        print('Gefeliciteerd, je mag stemmen!')
