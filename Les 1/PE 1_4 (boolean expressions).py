#vraag 1
a = 6
b = 7
inventaris = ['papier', 'nietjes', 'pennen']
voornaam = input('Wat is jouw voormaan? ')
tussenvoegsel = input('Wat zijn jouw tussenvoegsels? ')
achternaam = input('Wat is jouw achternaam? ')
mijnnaam = voornaam+' '+tussenvoegsel+' '+achternaam

print(b < 6.75 > a)

#vraag 2
print(len(inventaris * 5) > len(mijnnaam))

#vraag 3
if len(inventaris) == 0:
    print('inventaris is leeg')
elif len(inventaris) > 10:
    print('inventaris is langer dan 10')
else:
    print('er zitten minder dan 10 items in de inventaris')
