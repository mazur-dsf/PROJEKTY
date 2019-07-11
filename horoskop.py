import random

# oczywiście hasło jest w kodzie nieszyfrowane
haslo = "skype"
# tak jest - haslo to skype, brawo :)
print("Program 'HOROSKOPY' zabezpieczony hasłem.")
haslo_podane = ""
while not haslo_podane:
    haslo_podane = input("Podaj hasło dostępu:  \n")
while not haslo_podane == haslo:
    haslo_podane = input("Hasło nieprawidłowe.\n Podaj haslo dostepu:   \n")
print("\nDostęp udzielony. ")
print("""          WCZYTUJE PROGRAM HOROSKOPY""")
print("""          


                    Witaj w programie 'TWÓJ HOROSKOP'

                   Poprzez astralne połączenie Twojej energii z energią Kobaltowego Tygrysa Trzeciej Rangi podam Ci horoskop. 
                   Nie potrzebuję znać Twojego znaku zodiaku - wystarczy mi Twoja energia.

                   """)
imie = input("Na początek podaj mi swoje imie:  ")
print("Witaj " + imie + ".")
horoskop = random.randint(1, 8)

input("""           Połóż ręce delikatnie na klawiaturze... 
                    Uspokój myśli...
                    Kiedy poczujesz chęć - naciśnij klawisz  ENTER \n""")
print("""\n                    TWÓJ HOROSKOP NA DZISIAJ TO :           """)
if horoskop == 1:
    print(
        "\nMasz szansę współtworzenia z innymi czegoś wspaniałego. Spadnie zasłona projekcji i iluzji w kwestii materialnej.")
elif horoskop == 2:
    print(
        "\nJesteś gotowy, by zacząć działać tu i teraz. Nie odkładaj niczego na później. Masz szansę na powodzenie w kwestii materialnej ale musisz zacząć działać już teraz.")
elif horoskop == 3:
    print(
        "\nCzas na miłość i przyjaźń. Masz szansę na głębokie odczuwanie każdej emocji. Możesz więc oddać się uczuciom. Pozwól sobie przeżywać prawdziwie.")
elif horoskop == 4:
    print(
        "\nMasz dużą szansę na sukces i bogactwo. Musisz tylko posłuchać głosu intuicji, gdy staniesz przed trudnym wyborem.")
elif horoskop == 5:
    print(
        "\nTo bardzo intensywny czas. Znajdź więc czas żeby doładować akumulatory. Posłuchaj głosu swojej intuicji, ona Cię poprowadzi.")
elif horoskop == 6:
    print(
        "\n Masz szansę nawiązać nowe znajomości. Możesz zrozumieć siebie i innych. Nie walcz ze sobą, przyjmij dary życia i bądź za nie wdzięczny.")
elif horoskop == 7:
    print(
        "\n Wyśmienity dzień jeśli chodzi o sprawy zawodowe. Za sprawą korzystnego trygonu Księżyca do Jowisza możesz teraz liczyć na pomyśle zrządzenia losu oraz duży zapał do pracy.")
elif horoskop == 8:
    print(
        "\nSekstyl Wenus do Księżyca w sferze uczuć zapowiada, że poczujesz miłość. Może to być uczucie skierowane do twojego partnera,\n a jeśli jesteś sam odkryjesz, że bardzo, ale to bardzo kochasz... siebie. I to jest dobre! ")

print("\n          A teraz musisz zapłacić za wróżbę")
zaplata = input(
    "          \nPodaj kwotę w złotówkach  (cyfry) jaką przelejesz na konto WRÓŻA ROBERTA, który przygotował dla Ciebie ten horoskop: ")
while not zaplata.isdigit():
    zaplata = input(
        "          \nPodaj kwotę w złotówkach (cyfry) jaką przelejesz na konto WRÓŻA ROBERTA, który przygotował dla Ciebie ten horoskop: ")

zaplata = int(zaplata)

while zaplata < 100:
    zaplata = input("KWOTA " + str(zaplata) + " JEST ZA MAŁA - horoskop sie nie spełni, \n podaj inną kwotę: ")
    while not zaplata.isdigit():
        zaplata = input("Podaj kwotę w złotówkach (cyfry)")
    zaplata = int(zaplata)

print("                \nDZIĘKUJĘ! zobowiązałeś się do wpłaty " + str(
    zaplata) + "zł ale PAMIĘTAJ!!!:\nJeśli nie wpłacisz tego na konto WRÓŻA ROBERTA w ciągu 3 dni -  horoskop spełni się odwrotnie.")
print(
    "                  WYŚLIJ TEN PROGRAM DO 5 LUDZI a jeszcze w tym tygodniu spotka Cię coś wspaniałego, jeśli nie wyślesz to czeka Cię 5 lat pecha.\n Miłego dnia")
input("\n\n\nNacisnij enter by zakonczyć.")
