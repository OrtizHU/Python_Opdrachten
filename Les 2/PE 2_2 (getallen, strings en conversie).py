icor = int(input('Wat is uw ICOR cijfer? '))
prog = int(input('Wat is uw PROG cijfer? '))
csn = int(input('Wat is uw CSN cijfer? '))

gemiddelde = (csn+icor+prog)/3
beloning = (int((300/10))*csn)+(int((300/10))*icor+int(((300/10))*prog))
overzicht = 'Uw gemiddelde is {} en uw beloning daarvoor is {} euro.'.format(gemiddelde, beloning)
print('Uw gemiddelde is ', gemiddelde)
print('Uw beloning is ', beloning, 'euro.')
print(overzicht)
