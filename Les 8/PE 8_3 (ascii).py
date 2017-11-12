def code():
    invoer = input('Wat is uw naam? ')
    for letter in invoer:
        cijfers = ord(letter) + 3
        letters = chr(cijfers)
        print(letters, end='',)
    print('\n')
    invoer2 = input('Wat is uw beginstation? ')
    for letter in invoer2:
        cijfers = ord(letter) + 3
        letters = chr(cijfers)
        print(letters, end='')
    print('\n')
    invoer3 = input('Wat is uw eindstation? ')
    for letter in invoer3:
        cijfers = ord(letter) + 3
        letters = chr(cijfers)
        print(letters, end='')
code()
