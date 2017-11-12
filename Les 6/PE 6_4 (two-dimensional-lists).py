studentencijfers = [[95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0]]
def gemiddelde_per_student(studentencijfers):
  antw = []
  for i in studentencijfers:
      gem = sum(i)/len(i)
      antw.append(gem)
  return antw
def gemiddelde_van_alle_studenten(studentencijfers):
  list = []
  for i in studentencijfers:
      gem = sum(i)/len(i)
      list.append(gem)
  totaal_gemiddelde = sum(list) / len(list)
  return int(totaal_gemiddelde)
print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))
