def standaardtarief(afstandKM):
    tarief = 0
    if afstandKM > 50:
        tarief = 15 + (afstandKM * 0.60)
    else:
        tarief = afstandKM * 0.80
    return tarief

def ritprijs(leeftijd, weekendrit, afstandKM):
    "heuhiruh"
    standaardprijs = standaardtarief(afstandKM)
    ritprijs = standaardprijs
    if weekendrit == 'ja':
        if leeftijd < 65 and leeftijd > 12:
            ritprijs = standaardprijs * 0.60
        else: ritprijs = standaardprijs * 0.65
    else:
        if leeftijd >= 65 or leeftijd <= 12:
            ritprijs = standaardprijs * 0.70
    return ritprijs

afstand = int(input('Geef de afstand: '))
weekendrit = input('Is het weekend? ja/nee ')
leeftijd = int(input('Wat is jouw leeftijd: '))
deritprijs = ritprijs(leeftijd, weekendrit, afstand)
print(deritprijs)
