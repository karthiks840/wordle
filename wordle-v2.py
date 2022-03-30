import json
import re
from collections import Counter
import string

def openfile():
    with open('words_dictionary2.json','r') as myfile:
        data = myfile.read()
    return data

def return5wordlist():
    d = openfile()
    obj = json.loads(d)
    wl = list(obj.keys())
    return [w.lower() for w in wl if len(w)==5]

wordlist5 = return5wordlist()


def filter5word(wordlist5, correctlettersinposition, correctlettersnotinposition, unusedletters, correctlettersnotinpositionlist):
    matchstring = correctlettersinposition.replace('-','['+unusedletters+']')
    raw_string = r"{}".format(matchstring)
    
    retlist = [w for w in wordlist5 if re.match(raw_string,w)]
    
    final = []
    lettersnotinposition={}
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        lettersnotinposition[letter]=[]
    
    for word in correctlettersnotinpositionlist:
        i = 0
        for letter in word:
            if letter in lettersnotinposition:
                lettersnotinposition[letter].append(i)
            i=i+1
    #print(lettersnotinposition)
    
    newlettersnotinposition = {key:value for key, value in lettersnotinposition.items() if value}
    print(newlettersnotinposition)
    
    for word in retlist:
        i = 0
        for letter in correctlettersnotinposition:
            if word.find(letter)>=0 and word.find(letter) not in newlettersnotinposition[letter]:
                i=i+1
        if(i >= len(correctlettersnotinposition)):
            final.append(word)
        #print(word+'-'+str(i)+'-'+str(len(correctlettersnotinposition)))
        
    return final

def rank5word(wordlist5):
    rankedlist = {}
    alpha={}
    for x in 'abcdefghijklmnopqrstuvwxyz':
        alpha[x]=0
    
    for word in wordlist5:
        rank=0
        rank = rank + len([l for l in word if l in ('a','e','i','o','u')])
        rank = rank + (len([l for l in word if l not in ('a','e','i','o','u')]) * 2)
        
        for l in word:
            alpha[l] = alpha[l] + 1
    
    for word in wordlist5:
        rankedlist[word]=0
        for l in list(set(word)):
            rankedlist[word] = rankedlist[word] + alpha[l]
    #print(rankedlist)
    return rankedlist
    
#x = filter5word(wordlist5, 'sto-e','','qwetyuiosdfghjklzxcvbnm', ['---s-'] )
x = filter5word(wordlist5, '-----','kln','qwertyuiopasdfghjklzxcvbnm', ['----k','----l','----n'] )
#bfhmpw
y = rank5word(x)
print(x)
print(y)
#print(y['adieu'])
#z = {k: dict(Counter(y[k]).most_common(10)) for k in y}
z = dict(Counter(y).most_common(10))
print(z)



#qwertyuiop
#asdfghjkl
#zxcvbnm

#qwertyuiopasdfghjklzxcvbnm

