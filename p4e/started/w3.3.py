score = input("Enter Score: ")

try:
  s = float(score)
except:
  print("Error, value must be numeric")

if s > 1 and s < 0:
  print("Error, score out of range")
elif s >= 0.9:
  print("A")
elif s >= 0.8:
  print("B")
elif s >= 0.7:
  print("C")
elif s >= 0.6:
  print("D")
elif s < 0.6:
  print("F")