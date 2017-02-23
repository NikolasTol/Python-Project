text=raw_input('Dwse lista: ')
print "Arxikh Lista: "
t = list(text)
print t
zer = t.count('0')
for i in range(0,zer):
    t.remove('0')
for i in range(0,zer):
    t.append('0')
print "Telikh Lista: "
for i in range(0,len(t)):
    print t[i]
