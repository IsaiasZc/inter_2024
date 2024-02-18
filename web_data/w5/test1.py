from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
xml = urlopen(url, context=ctx).read()

tree = ET.fromstring(xml)

counts = sum([int(i.text) for i in tree.findall('.//count')])

print(counts)