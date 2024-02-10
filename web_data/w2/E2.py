# import re as regex

# f = open('assign.txt')
# total = 0

# for line in f:
#   line = line.rstrip()
#   nums = regex.findall('[0-9]+',line)
#   if len(nums) > 0:
#     total += sum([int(i) for i in nums])

# print(total)


import re
print( sum([int(i) for i in re.findall('[0-9]+', open('assign.txt').read())]) )