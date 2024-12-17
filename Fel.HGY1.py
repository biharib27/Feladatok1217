mondatok = []
for _ in range(5):
    mondat = input("Kérem, írjon be egy mondatot: ")
    mondatok.append(mondat)
max_szokoz = -1
max_mondat = ""
for mondat in mondatok:
    szokoz = 0
    for karakter in mondat:
        if karakter == " ":
            szokoz += 1
    if szokoz > max_szokoz:
        max_szokoz = szokoz
        max_mondat = mondat
print("A legtöbb szóközt tartalmazó mondat:", max_mondat)