import random

szamok = []
for _ in range(100):
    szamok.append(random.randint(-100, 100))

pozitivok_szama = 0
negativok_szama = 0
for szam in szamok:
    if szam > 0:
        pozitivok_szama += 1
    elif szam < 0:
        negativok_szama += 1

if pozitivok_szama > negativok_szama:
    print("Több pozitív szám van.")
else:
    print("Több negatív szám van.")

talalt = False
for index in range(100):
    if szamok[index] > 50:
        print(f"Az első 50-nél nagyobb szám sorszáma: {index}")
        talalt = True
        break

if not talalt:
    print("Nincs 50-nél nagyobb szám.")

for i in range(99):  
    if abs(szamok[i] - szamok[i + 1]) > 120:
        print("Két egymás követő szám között a különbség meghaladja a 120-at.")
        break
else:
    print("Nincs olyan két egymás követő szám, amelynek a különbsége meghaladja a 120-at.")