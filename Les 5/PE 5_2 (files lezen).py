with open('kaartnummers.txt', 'r') as file:
    regels = file.readlines()

for regel in regels:
    old_list = regel.split(',')
    woord = 'heeft kaartnummer:'
    new_list = '{} {} {}'.format(old_list[1].strip('\n'),woord,old_list[0])
    print(new_list)
print()
