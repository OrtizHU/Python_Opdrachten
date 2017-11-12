while True:
    l = input('Geef een string van vier letters: ')
    if len(l) != 4:
        continue
    else:
        print('Inlezen van correcte string: {} is geslaagd'.format(l))
        break
