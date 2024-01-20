# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
  fh = open(fname)
except:
   print("Error, the file doesn't exist")
   quit()

lines = 0
total = 0
avr = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    lines += 1
    idx = line.index(':')
    num = float(line[idx + 1:].strip())
    total += num

avr = total / lines
print("Average spam confidence:", avr)
