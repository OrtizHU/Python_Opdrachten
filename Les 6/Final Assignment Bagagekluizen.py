kluizen = open('kluizen.txt', 'r+')

def nieuwe_kluis():
    kluizen = open('kluizen.txt', 'r+')
    read_kluis = kluizen.readlines()
    lijst_kluizen = ['']
    totaal_kluizen = len(kluizen.readlines())
    for kluis in read_kluis:
        kluisnummer = kluis.split('; ')[0]
        lijst_kluizen == kluisnummer
    if len(lijst_kluizen) > 0 and len(lijst_kluizen) < 13:
        print('U kunt een kluis nemen.')
        if len(lijst_kluizen) > 0 and len(lijst_kluizen) < 13:
            ww = input('Maak een wachtwoord aan: ')
            kluisn = input('Kies een kluis nummer ')
        kluizen.write('{}; {}\n'.format(kluisn, ww))
        return('Jouw kluisnummer is ' + str(kluisn) + ' en je wachtwoord is: ' + ww)
    else:
        return 'Alle kluizen zijn al genomen.'
    kluizen.close('kluizen.txt')

def kluis_openen():
    kluisnummer = eval(input('Wat is jouw kluisnummer? '))
    kluiscode = input('Voer jouw wachtwoord in ')
    for i in kluizen.readlines():
        split = i.split('; ')
        nummer = int(split[0])
        wachtwoord = split[1].strip('\n')
        if kluisnummer == nummer and kluiscode == wachtwoord:
            return 'Kluis nummer {} is geopend'.format(kluisnummer)
        else:
            return 'Wachtwoord klopt niet\nDe kluis is niet geopend!\nDit komt waarschijnlijk omdat het kluisnummer of wachtwoord fout is.\nAls u nog geen kluis heeft kunt u een nu aanvragen.'


def kluis_teruggeven():
    return

def aantal_kluizen_vrij():
    kluizen_vrij = 12 - len(kluizen.readlines())
    return 'Nu zijn er {} kluizen vrij'.format(kluizen_vrij)


menu = format(input('1: Ik wil een nieuwe kluis\n'
                 '2: Ik wil mijn kluis openen\n'
                 '3: Ik geef mijn kluis terug\n'
                 '4: Ik wil weten hoeveel kluizen nog vrij zijn\n'
                 'Kies een optie '))
"de menu"
#de-menu

if menu == '1':
    print(nieuwe_kluis())
elif menu == '2':
    print(kluis_openen())
elif menu == '3':
    print('\nDeze optie is momenteel niet beschikbaar.\nNeem contact op met een baliemedewerken om uw kluis terug te geven.')
elif menu == '4':
    print(aantal_kluizen_vrij())
else: print('Deze optie bestaat niet!')
