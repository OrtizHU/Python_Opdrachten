def convert():
    graden = int(input('Hoeveel graden celcius is het? '))
    farenheit = (graden*1.8)+32
    farenheit = int(farenheit)
    return farenheit

def table():
    for i in range(-30, 50,10):
        farenheit = i * 1.8 + 32
        print('{0:4} {1:9}'.format(farenheit, i))

print(convert())
table()
