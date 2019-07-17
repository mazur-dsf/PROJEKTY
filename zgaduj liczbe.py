def main():
    print("Witaj w grze jaka to liczba")
    import random
    wylosowana_liczba = random.randint(1, 100)
    imie = input("Najpiero powiedz jak się nazywasz:  ")
    print(
        "Witaj " + imie + ", komputer wylosuje teraz jakąś liczbę od 1 do 100 a Twoim zadaniem jest odgadnąć jaka to liczba. Na końcu podam Ci liczbę prób.")
    liczba = input("A teraz spróbuj odgadnąć tę liczbę tutaj (użyj tylko cyfr):  ")
    while not liczba.isdigit():
        liczba = input("Użyj tylko cyfr!:  ")
    liczba = int(liczba)
    licznik = 0
    while wylosowana_liczba != liczba:
        print("Nie zgadłeś/aś :) ")
        if wylosowana_liczba > liczba:
            liczba = input("Twoja liczba jest mniejsza od zgadywanej, spróbuj jeszcze raz:  ")
            while not liczba.isdigit():
                liczba = input("Użyj tylko cyfr!:  ")
            liczba = int(liczba)
            licznik = (licznik + 1)
        elif wylosowana_liczba < liczba:
            liczba = input("Twoja liczba jest wieksza od zgadywanej, spróbuj jeszcze raz:  ")
            while not liczba.isdigit():
                liczba = input("Użyj tylko cyfr!:  ")
            liczba = int(liczba)
            licznik = (licznik + 1)
    wylosowana_liczba = str(wylosowana_liczba)
    licznik = str(licznik)
    print("Brawo! Udało się! ta liczba to: " + wylosowana_liczba)
    print("Liczba prób to: " + licznik)


main()
gramy = input("Chcesz zagrać jeszcze raz? (odpowiedz tak lub nie):  ")
if lower(gramy) == "tak":
    main()
else:
    exit()
