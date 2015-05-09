import string
import random

class Queue(object):
    def __init__(self):
        self.vals = []
    def insert(self,e):
        self.vals.insert(0,e)
    def remove(self):
        try:
            return self.vals.pop()
        except IndexError,e:
            print "Empty List "+str(e)
            
    def __len__(self):
        return len(self.vals)

    def __str__(self):
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
def Trim(text):
    tt=text.split(' ')
    cha=string.ascii_uppercase+string.ascii_lowercase
    new=[]
    for qo in tt:
        m=""
        for w in range(0,len(qo)):
            if qo[w] in cha:
                m+=qo[w]
        new.append(m)
    return new
