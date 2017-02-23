sentence = raw_input('Dwse protash: ')
s = list(sentence)
for i in range(1,len(sentence)-1):
    if s[i-1]=='!' and ((i-1)!=len(sentence)-1): #i-1 giati alliws meta to i+1 8a evgaine ektos range
        if s[i].islower():
            s.pop(i-1)
print "".join(s)
