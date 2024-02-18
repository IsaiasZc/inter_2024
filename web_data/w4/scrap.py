from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter : ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
count = 0

for tag in tags:
  if tag.get('class', None)[0] == 'comments':
    count += float(tag.contents[0])

print(f"count {len(tags)}")
print(f"Sum {count}")