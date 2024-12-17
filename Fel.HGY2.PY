varosok = ["Debrecen", "Karcag", "Szolnok", "Szeged", "Miskolc"]

varos = input("Kérem, írjon be egy városnevet: ")
talalt = False
for index in range(len(varosok)):
    if varosok[index] == varos:
        talalt = True
        if index < len(varosok) - 1:
            print("A következő város:", varosok[index + 1])
        else:
            print("Ez az utolsó város, nincs következő.")
        break
if not talalt:
    varosok.append(varos)
    print(f"{varos} város hozzáadva a listához.")