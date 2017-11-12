import random
def monopolyworp():
    DS1 = 0
    DS2 = 0
    worpen = 0

    while DS1 == DS2 and worpen != 3:
        DS1 = random.randint(1, 6)
        DS2 = random.randint(1, 6)
        worpen += 1
        if DS1 == DS2:
           if worpen == 3:
              print(DS1, '+', DS2, '= (direct naar gevangenis)')
           else:
              print(DS1, '+', DS2, '=', (DS1+DS2), '(dubbel)')
        else:
            print('{} + {} = {}'.format(DS1, DS2, (DS1+DS2)))

monopolyworp()
