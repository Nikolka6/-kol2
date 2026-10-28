def je_prvocislo(cislo):
    if cislo < 2:
        return False

    for i in range(2, cislo):
        if cislo % i == 0:
            return False

    return True


def vrat_prvocisla(maximum):
    seznam = []

    for cislo in range(1, maximum + 1):
        if je_prvocislo(cislo):
            seznam.append(cislo)

    return seznam
    
if __name__=="__main__":
    cislo = int
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)
    
