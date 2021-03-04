# Alguns exemplos de uso de listas

import string
a = list(string.ascii_lowercase) # Alfabeto
b = string.hexdigits # exadecimais
c = []
for i in b:
    c.append(i)

for index, i in enumerate(a):
    print(f"Posição {index} valor: {i}")

# Ou pode ser feito de outra forma

print("\nOutra forma:")
for i in a:
    print(f"Posição {a.index(i)} valor: {i}")

print(f"lista duas vezes {a * 2}")
print(f"Junta duas listas {a + c}")