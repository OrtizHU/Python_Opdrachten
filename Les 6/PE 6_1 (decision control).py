def seizoen(maand):
    if 0 <= maand <= 2:
        print('Het is winter')
    elif 3 <= maand <= 5:
        print('Het is lente')
    elif 6 <= maand <= 8:
        print('Het is zomer')
    elif 9 <= maand <= 12:
        print('Het is herfst')
    else:
        print('Foute invoer')
