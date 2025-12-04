# Zadanie 2

imiona = ["Ala", "Kasia", "Tomek", "Marek"]

imiona.sort()
print("Posortowana lista:", imiona)

imiona.append("Ola")
imiona.append("Jan")
print("Po dodaniu osób:", imiona)
print("Pop() zwróciło:", imiona.pop())

imiona.insert(3, "Piotr")
print("Po dodaniu osoby na pozycji 3:", imiona)

imiona.reverse()
imiona = imiona * 2
print("Odwrócona i zdublowana lista:", imiona)
