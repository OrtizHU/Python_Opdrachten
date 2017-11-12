invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
list = str(invoer[0::]).split('-')
for i in range(len(list)):
    list[i] = int(list[i])

for i in range(0,10):
   for i in range(len(list)-1):
       if list[i] > list[i+1]:
          value = list[i]
          list[i] = list[i+1]
          list[i+1] = value

gemiddelde = int(sum(list)) / len(list)
print('Gesorteerde list van ints: {}'.format(list))
print('Grootste getal: {} en Kleinste getal: {}'.format(max(list), min(list)))
print('Aantal getallen: {} en Som van de getallen: {}'.format(len(list), sum(list)))
print('Gemiddelde: {}'.format(gemiddelde))
