def kleinste_veelvoud7(grenswaarde):
    'return het kleinste veelvoud van 7 die groter is'
    result = 0
    for getal in range(100):
        result = result + 7
        if result > grenswaarde:
            return result

print (kleinste_veelvoud7(6700))

#next

def kleinste_veelvoud8(grenswaarde):
    'blah blah'
    result = 0
    while result < grenswaarde:
        result = result + 7

    return result

print(kleinste_veelvoud8(6700))

#next
while True:
    woord = input ('Doe mij een woord:')
    if woord == 'stop':
        break
    elif woord == 'volgende':
        continue
    print (len(woord))

#next
cijfers = [95, 00, 85, 95, 97, 100, 95]

resultaat = {}
for cijfer in cijfers:
    if cijfer in resultaat:
        resultaat[cijfer] = resultaat[cijfer] + 1
    else:
        resultaat[cijfer] = 1

print(resultaat)
