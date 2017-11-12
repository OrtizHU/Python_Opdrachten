def kwadraten_som(grondgetallen):
    list = []
    for i in grondgetallen:
        if i <= 0:
            i = 0
        list.append(i ** 2)
    return sum(list)

print(kwadraten_som([4, 5, 3, -81]))
