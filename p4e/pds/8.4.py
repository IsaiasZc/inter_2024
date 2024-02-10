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


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
text = open(name)

maxauthor = dict()

for line in text:
    line.rstrip()
    if not line.startswith("From "): continue
    words = line.split()
    maxauthor[words[1]] = maxauthor.get(words[1],0)+1

largest = None
largest_author = None

for key in maxauthor:
    if largest is None: largest = maxauthor[key]

    if largest < maxauthor[key]:
        largest = maxauthor[key]
        largest_author = key

print(largest_author, largest)