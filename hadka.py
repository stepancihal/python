import random
elektronika = ["telefon","hodinky","sluchatka","notebook","stolní počítač","tablet"]
for i in range (10):
    osoba1 = random.choice(elektronika)
    osoba2 = random.choice(elektronika)
    if osoba1 == osoba2:
        print("Kupme",osoba1)
        print("Ne, kupme jiný",osoba2)
    else:
        print("Kupme",osoba1)
        print("Ne, kupme",osoba2)
