xfile = open('mbox.txt')

count = 0
for line in xfile:
  line = line.rstrip() # delete the new line command \n
  count += 1
  print(line)

print(count)

xfile.seek(0) # reset the point to the first line

for line in xfile:
  line = line.strip()
  if not 'gmail' in line: # print just the line thas has 'gmail'
    continue
  print(line)

xfile.seek(0) # reset the point to the first line

for line in xfile:
  line = line.strip()
  if line.startswith('an'): # print just the line thas has 'gmail'
    print('line with an',line)