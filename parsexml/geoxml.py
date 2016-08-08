import urllib
import xml.etree.ElementTree as ET


while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    print 'Retrieving', address
    uh = urllib.urlopen(address)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    tree = ET.fromstring(data)

    ans = 0
    counts = tree.findall('.//count')
    for count in counts:
        ans += int(count.text)
    print ans
