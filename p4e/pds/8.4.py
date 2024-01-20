fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    line = line.split()
    for el in line:
        if el in lst : continue
        lst.append(el)
    
print(lst.sort())