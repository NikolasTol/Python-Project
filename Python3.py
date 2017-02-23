import urllib2
import json
numberset = raw_input("Dwse seira ari8mwn apotelesmatwn: ")
if numberset.count(',')!=0:
    numberset = numberset.split(',')
url = "http://applications.opap.gr/DrawsRestServices/proto/last.json"
json_obj = urllib2.urlopen(url)
data = json.load(json_obj)
number = data['draw']['drawNo']
y=0
for number in range(number,number - 8,-1):
    x=0
    url2 = "http://applications.opap.gr/DrawsRestServices/proto/%s.json" % (number)
    json_obj2 = urllib2.urlopen(url2)
    data2 = json.load(json_obj2)
    result = data2['draw']['results']
    for i in range(0,7):
        res = result[i]
        num = numberset[i]
        if int(res) == int(num):
            x = x + 1
    if (x == 7):
        y =+1
if y == 1:
    print 'Ton teleutaio mhna o syndiasmos emfanistike:'
    print '1 fora'
elif y == 0:
    print 'O syndiasmos den emfanistike kamia fora ton teleutaio mhna'
else:
    print 'Ton teleutaio mhna o syndiasmos emfanistike:'
    print y, 'fores'
