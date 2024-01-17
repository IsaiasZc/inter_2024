# Solucion 1
# name = input('Write your name: ')

# print('¡Hola', name + '!')


# Solucion 2

# result = ((3 + 2) / (2 * 5)) ** 2

# print("Exercise 2:",result)

# Solution 3

n = input("Escribe un valor para <n>: ")
m = input("Esribe un valor para <m>: ")

try:
  n = int(n)
  m = int(m)
except:
  print("Error, digita numeros enteros")
  quit()

c = int(n / m)
r = n % m

print(f"{n} entre {m} da un cociente {c} y un resto {r}")