# Use words.txt as the file name
fname = input("Enter file name: ")
try:
  fh = open(fname)
except:
  print("Error, The file does not exist")
  quit()

for line in fh:
  print(line.upper().rstrip())
