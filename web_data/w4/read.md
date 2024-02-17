# ASCII

Unicode es un codigo que basicamente el codigo original de los caracteres que utilizamos, y luego nuestras computadoras lo traducen para que nosotros entendamos, por ejemplo la letra 'H' tiene un codigo ASCII de 72.

```py
>>> print(ord('H'))
72
>>> print(ord('e'))
101
>>> print(ord('\n'))
10
>>>
```

Unicode soluciona un problema que existe al intercambiar información con diferentes lenguajes donde se utilizan simbolos diferentes. Unicode abraza todos estos caracteres y los pone como parte de un solo grupo.

- UTF-8 es la codificacion que manejamos actualmente y es la mejor practica.


## Python Strings to bytes

```py
while True:
  data =mysock.recv(512) # data is bytes
  if ( len(data) < 1>):
    break
  mystring = data.decode()
  print(mystring) # mystring is unicode (indepente of UTF-8 or other)
```

Hay funciones en python para hacer `encode` (Convertir de Unicode a bytes) y `decode` (Convertir de Bytes a Unicode).
