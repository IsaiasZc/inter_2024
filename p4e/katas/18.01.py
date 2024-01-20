"""first"""
# def to_camel_case(text):
#   if len(text) == 0:
#     return ''
#   new_text = ""

#   for idx, val in enumerate(text):
    
#     if val == '-' or val == '_':
#       continue
#     elif idx > 0 and (text[idx-1] == '-' or text[idx-1] == '_'):
#       new_text += val.upper()
#     else:
#       new_text += val

#   return new_text




# print(to_camel_case('hola-mundo'))

""" second """
def create_phone_number(n):
    #your code here
    n = ''.join(map(str,n))
    return f'({n[0:3]}) {n[3:6]}-{n[6:]}'

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))