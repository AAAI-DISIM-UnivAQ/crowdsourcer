__author__ = 'subhasis'

from pylinkgrammar.linkgrammar import Parser

def contains(l1,i1):
    ret  = 0
    for i in range(0,len(l1),1):
        if l1[i] == i1:
            ret = 1
    return ret


def sen1(p1,p2,p3,p4,p5):
    return p1+' ' + p2 + ' ' + p3 +' '+ p4 +' '+p5

def con2(l1):
    ret = ""
    for i in range(0,len(l1),1):
        ret = ret + " ~~" + "POS" +  " " + str(l1[i])
    return ret


def con1(l1):
    ret = ""
    for i in range(0,len(l1),1):
        ret = ret + " ~~" + "agent" + str(i) + " " + str(l1[i])
    return ret


class agent:
    def __init__(self,p1,pos1):
        self.p2 = p1
        self.pos = pos1
        self.score = 0
        self.str1 = []
        self.group = "L"


    def setGroup(self,g):
        self.group = g

    def setScore(self,score1):
        self.score = score1

    def setStr(self,str2):
        self.str1 = str2

    def agentFun(self):

         p = Parser()
         linkages = p.parse_sent(self.p2)
         print len(linkages)
         if len(linkages)>0:
                print linkages[0].diagram
         else:
             print 'none'
    def change(self):
        if self.pos>3:
           return self.pos-1
        else:
            return self.pos+1
    def checkNeigh(self,p3):
        str1 = self.p2+' '+ p3
        str2 = p3 + ' ' + self.p2
        flag  = 0
        parser1 = Parser()
        linkages = parser1.parse_sent(str1)
        print len(linkages)
        if len(linkages)>0:
            flag = 1
        linkages = parser1.parse_sent(str2)
        print len(linkages)
        if len(linkages)>0:
            flag = 2
        return flag





def constructSen(list1):
    len1 = len(list1)
    str1 = ''
    for i in range(1,len1+1,1):
        str1 = str1 + list1[i-1] + ' '
    return str1

def sequence1(a):
    ret=[]
    for i in range(0,a,1):
        ret.append(i)
    return ret



def findPos(list1,id1):
    ret = 0
    for i in range(0,len(list1),1):
        if id1 == list1[i]:
            ret = i
    return ret

def findlength(len1,len2,pos):
    ret = []
    v1 = len1 - pos
    if v1 > 1:
        if v1 >= len2/2:
            ret.append(len2/2)
        else:
            v2 = len2/2 - v1
            if v2 > 0:
                ret.append(v2)
            else:
                ret.append(0)
    else:
        ret.append(0)
    return ret


def findlength1(len1,len2,pos):
    ret = []
    if pos >= len2/2:
        ret.append(len2/2)

    if pos == 0 :
        ret.append(0)

    if pos>0:
        if pos < len2/2:
            ret.append(pos)

    return ret

def findStr1(wordList,intPos,pos1,lim):
    ret = []
    lim1 = lim
    l1 = findlength1(len(wordList),lim1,pos1)
    l2  = findlength(len(wordList),lim1,pos1)
    if l1[0] < (lim1/2) :
        l2[0] = l2[0] + (lim1/2 - l1[0])
    if l2[0] < (lim1/2) :
        l1[0] = l1[0] + (lim1/2 - l2[0])

    for i in range(pos1-l1[0],pos1+1,1):
        if i < len(intPos):
           local1 = intPos[i]
           local2 = wordList[int(local1)]
           ret.append(local2)
    for i in range(pos1+1,pos1+l2[0]+1,1):
        if i< len(intPos):
            local1 = intPos[i]
            local2 = wordList[int(local1)]
            ret.append(local2)
    return ret

def findStr2(wordList,intPos,pos1,lim,str2):
    ret = []
    lim1 = lim
    l1 = findlength1(len(wordList),lim1,pos1)
    l2  = findlength(len(wordList),lim1,pos1)
    if l1[0] < (lim1/2) :
        l2[0] = l2[0] + (lim1/2 - l1[0])
    if l2[0] < (lim1/2) :
        l1[0] = l1[0] + (lim1/2 - l2[0])

    for i in range(pos1-l1[0],pos1+1,1):
        if i != pos1:
            local1 = intPos[i]
            local2 = wordList[int(local1)]
            ret.append(local2)
        else:
            ret.append(str2)

    for i in range(pos1+1,pos1+l2[0]+1,1):
        if i < len(intPos):
            local1 = intPos[i]
            local2 = wordList[int(local1)]
            ret.append(local2)
    return ret





def updatetotalwt(t1,w1):
    for i in  range(0,len(w1),1):
        t1.append(w1[i])
    return t1


def replaceStr(otherStr1,localP2,otherP2):
    ret = otherStr1
    pos = 0
    for i in range(0,len(otherStr1),1):
        if otherStr1[i] == otherP2:
            pos = i
    ret[pos] = localP2
    return ret



def getstr(wordlist,intpos,pos,lim):
    len1 = len(wordlist)
    str1 = wordlist[intpos[pos]]

    ret = []
    if pos == 0:
        ret.append(str1)
        for i in range(0,lim,1):
            ret.append(wordlist[intpos[pos+i+1]])
    if pos == len(wordlist)-1:
        counter = pos - lim
        while constructSen()<= pos:
            ret.append(wordlist[intpos[counter]])
            counter=counter+1
    if pos>0 & pos < lim:
        for i in range(0,lim,1):
            ret.append(wordlist[intpos[i]])
        ret.append(wordlist[intpos[pos]])
        for i in range(lim+1,lim,1):
            ret.append(wordlist[intpos[i]])
    if pos< len(wordlist)-1 & pos > len(wordlist)-lim:
        for i in range(pos-lim,pos,1):
            ret.append(wordlist[intpos[i]])
        ret.append(wordlist[intpos[pos]])
        for i in range(pos+1,len(wordlist)-1,1):
            ret.append(wordlist[intpos[i]])
    if pos >= lim & pos <= len(wordlist)-lim:
        for i in range(pos-lim,pos,1):
            ret.append(wordlist[intpos[i]])
        ret.append(wordlist[intpos[pos]])
        for i in range(pos+1,pos+lim,1):
            ret.append(wordlist[intpos[i]])

    return ret




def getstr1(wordlist, intpos, pos):
    ret = []
    if pos==0:
        ret.append(wordlist[intpos[pos]])
        ret.append(wordlist[intpos[pos+1]])
        ret.append(wordlist[intpos[pos+2]])
    elif pos == len(wordlist)-1:
        ret.append(wordlist[intpos[pos-2]])
        ret.append(wordlist[intpos[pos-1]])
        ret.append(wordlist[intpos[pos]])
    else:
        ret.append(wordlist[intpos[pos-1]])
        ret.append(wordlist[intpos[pos]])
        ret.append(wordlist[intpos[pos+1]])
    return ret
