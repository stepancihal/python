
while True:
    print("Zadejte evě čísla")
    cislo1 = int(input("zadej první číslo"))
    cislo2 = int(input("zadej druhé číslo"))
    vysledek = str(input("chces použít pro čísla sčítání, odčítáí, násobení nebo dělení?"))
    if vysledek == "sčítání":
        print(cislo1 + cislo2)
    elif vysledek == "odčítání":
        print(cislo1 - cislo2)
    elif vysledek == "násobení":
        print(cislo1*cislo2)
    elif vysledek == "dělení":
        print(cislo1/cislo2)
    opak = input("chcete počítat znovu? ano/ne ")
    if opak == "ne":
        break