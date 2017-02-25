import urllib2
import json
key1 = raw_input('Dwse kleidia anazhthshs: ')
spaces = key1.count(" ")
if spaces!=0:
    key = key1.split(", ")
else:
    key = key1.split(",")
key=list(key)
base = 'http://api.brewerydb.com/v2/search?'
apikey = '&p=all&type=beer&key=883706a8fdb0655ef503c1ae5f51a1cf'
for i in range(0,len(key)):
    base = base + '&q='+ key[i]
    if i!=len(key)-1:
        base = base + '/'
    url = base + apikey
print url
json_obj = urllib2.urlopen(url)
data = json.load(json_obj)
name = data['data'][0]['name']
description = data['data'][0]['description']
description = description.encode('utf-8')
print "Beer name: " + name
print "Beer description: " + description
