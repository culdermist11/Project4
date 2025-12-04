# Zadanie 8

stopnie = (
    "Szeregowy",
    "Kapral",
    "Sierżancie",
    "Porucznik",
    "Kapitan",
    "Major",
    "Pułkownik",
)

ilosc_stopni = len(stopnie)
Major_index = stopnie.index("Major")
Pulkownik_wystepowanie = "Pułkownik" in stopnie

print("Liczba stopni:", ilosc_stopni)
print("Indeks 'Major':", Major_index)
print("Czy 'Pułkownik' jest w krotce?", Pulkownik_wystepowanie)
