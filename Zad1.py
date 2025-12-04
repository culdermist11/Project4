# Zadanie 1

Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]
print(Moja_lista)

print(len(Moja_lista))
print(Moja_lista[0])
print(Moja_lista[-1])
print(Moja_lista[2:6])

Moja_lista.append(100)
Moja_lista.extend([200])
Moja_lista.insert(1, 999)
print(Moja_lista)

Moja_lista.remove(3)
print(Moja_lista)

print(Moja_lista.pop())
print(Moja_lista)

print(Moja_lista.count(5))
print(Moja_lista.index(86))

Moja_lista.sort()
print(Moja_lista)

Moja_lista.reverse()
print(Moja_lista)

Moja_lista.clear()
print(Moja_lista)
