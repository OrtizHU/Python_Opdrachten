try:
  gasten = int(input('Hoeveel personen reizen mee: '))
  kosten = 4356
  delen = kosten/gasten
  if gasten < 0:
      raise Exception
  print(delen)

except ZeroDivisionError:
    print('Delen door nul kan niet!')
except Exception:
    print('Negatieve getallen zijn niet toegestaan!')
except ValueError:
    print('Gebruik cijfers voor het invoeren van het aantal!')
except:
    print('Onjuiste invoer!')
