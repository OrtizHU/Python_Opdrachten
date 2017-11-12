namen = {}
invoer = input('Volgende naam: ')
while invoer != '':
    if invoer in namen:
        namen[invoer] += 1
    else:
        namen[invoer] = 1
    invoer = input('Volgende naam: ')
sorted(namen)
for invoer,value in namen.items():
    if value == 1:
        print('Er is', value, 'student met de naam', invoer)
    else:
        print('Er zijn', value, 'studenten met de naam', invoer)
