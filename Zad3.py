# Zadanie 3

imie = input("Podaj imię: ")
print("Witaj", imie)

wiek = input("Podaj wiek: ")
print("Twój wiek to:", wiek)

imie2 = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")
print("Inicjały:", imie2[0] + nazwisko[0])

tekst = input("Podaj łańcuch: ")
print(tekst * 5)

t1 = input("Podaj 1. łańcuch: ")
t2 = input("Podaj 2. łańcuch: ")
t3 = t1 + t2
print("Połączenie:", t3)

a = input("Podaj pierwszy łańcuch: ")
b = input("Podaj drugi łańcuch: ")

srodek_a = len(a) // 2
srodek_b = len(b) // 2

polaczony = a[:srodek_a] + b[srodek_b:]
print("Nowy łańcuch:", polaczony)
