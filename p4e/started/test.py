def computepay(h, r):
  total = 0
  if h > 40:
    before40 = 40 * r
    total = before40 + (h - 40) * r * 1.5
  else:
    total = h * r
  return total

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

try:
  h = float(hrs)
  r = float(rate)
except:
  print("Error, please enter numeric input")
  quit()

p = computepay(h, r)
print("Pay", p)