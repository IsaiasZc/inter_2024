"""
Para recorrer un 'string', un ciclo for nos da una forma mas sencilla de hacerlo

for letter on 'banana':
  print(letter)

Slicing: we can extract just a part of a string
>>>  = 'Monty Python'

"""
# data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# pos = data.find('.')
# print(data[pos:pos+3])

text = "X-DSPAM-Confidence:    0.8475"
init = text.find('0')
sliced = text[init:]
sliced = float(sliced)
print(sliced)