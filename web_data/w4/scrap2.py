from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter Count: '))
positiion = int(input('Enter position: '))

def get_data(url, pos):
  html = urlopen(url, context=ctx).read()
  soup = BeautifulSoup(html, "html.parser")
  tags = soup('a')

  return tags[pos].get('href', None)

for i in range(count):
  print(f'Retrieving: {url}')
  url = get_data(url, positiion - 1)

print(f'Result: {url}')


