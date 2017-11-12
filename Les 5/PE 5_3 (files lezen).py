list = []
with open('kaartnummers.txt', 'r') as file:
    regels = file.readlines()
for regel in regels:
    regel = regel.strip('\n')
    list2 = regel.split(',')
    nummers = int(list2[0])
    list.append(nummers)

print('Deze file telt {} regels.'.format(len(regels)))
print('Het grootste kaartnummer is: {} en dat staat op regel {}'.format(max(list),list.index(max(list))+1))
