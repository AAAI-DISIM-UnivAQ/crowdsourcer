__author__ = 'subhasis'

from CrowdManager import *
from igraph import *
import random
from pylinkgrammar.linkgrammar import Parser
from igraph import *
import matplotlib.pyplot as plt

str1 = 'Italian explorers such as Polo, Columbus, and Verrazzano discovered new routes to the Far East and the New World, helping to usher in the European Age of Discovery.'

wordList = str1.split(' ')

print(len(wordList))


agentIds = []

len1 = len(wordList)

for i in range(0,len1,1):
    agentIds.append(i)



# random allocation of puzzle pieces
intPos = random.sample(agentIds,len1)
intPos1 = intPos
agents  = []
# first bipartite graph
for i in range(0,len1,1):
    local1 = agent(wordList[i],0)
    if i<=len1/2:
        local1.setGroup("L")
    else:
        local1.setGroup("R")
    agents.append(local1)







counter1 = 0
lim = 6
wtstore = []
intposstore = []

storescore = []

storeedges = []

parser2 = Parser()


totalscore = []

while counter1 < 1000:
    g = Graph()
    g.add_vertices(len1)
    for i in range(0,len1,1):
        g.vs["name"] = i


    parser1 = Parser()

    wts = []
    changed = []
    for i in range(0, len(agents), 1):
        localpos = findPos(intPos, i)
 
        str1 = getstr1(wordList,intPos,localpos)
        str11 = []
        str11.append(str1[0])
        str11.append(str1[1])
        str22 = []
        str22.append(str1[1])
        str22.append(str1[2])

        localsen1 = constructSen(str1)
        localsen2 = constructSen(str11)
        localsen3 = constructSen(str22)


        print(localsen1)
        print(localsen2)
        print(localsen3)


        score1 = len(parser1.parse_sent(localsen1))
        score2 = len(parser1.parse_sent(localsen2))
        score3 = len(parser1.parse_sent(localsen3))


        ownwt1 = max(score1,score2,score3)
        agents[i].setScore(ownwt1)
        agents[i].setStr(str1)

    totalwt1 = 0
    for i in range(0,len(agents),1):
        wts.append(agents[i].score)
        totalwt1 = totalwt1 + agents[i].score

    totalscore.append(totalwt1)
    wtstore.append(con1(wts))
    intposstore.append(con2(intPos))
    storeedges.append(con1(g.get_edgelist()))

    for i in range(0,len(agents),1):
        localpos = findPos(intPos, i)
        localscore = agents[i].score
        localP2 = agents[i].p2
        ownStr1 = agents[i].str1
        for j in range(0,len(agents),1):
            if agents[i].group != agents[j].group:
                otherscore = agents[j].score
                otherP2 = agents[j].p2
                otherStr1 = agents[j].str1
                newstr1 = replaceStr(otherStr1,localP2,otherP2)
                newstr2 = replaceStr(ownStr1,otherP2,localP2)

                str11 = []
                str11.append(newstr1[0])
                str11.append(newstr1[1])
                str22 = []
                str22.append(newstr1[1])
                str22.append(newstr1[2])

                localsen1 = constructSen(newstr1)
                localsen2 = constructSen(str11)
                localsen3 = constructSen(str22)


                score1 = len(parser1.parse_sent(localsen1))
                score2 = len(parser1.parse_sent(localsen2))
                score3 = len(parser1.parse_sent(localsen3))
                newscore1 = max(score1,score2,score3)

                str11 = []
                str11.append(newstr2[0])
                str11.append(newstr2[1])
                str22 = []
                str22.append(newstr2[1])
                str22.append(newstr2[2])

                localsen1 = constructSen(newstr2)
                localsen2 = constructSen(str11)
                localsen3 = constructSen(str22)


                score1 = len(parser1.parse_sent(localsen1))
                score2 = len(parser1.parse_sent(localsen2))
                score3 = len(parser1.parse_sent(localsen3))
                newscore2 = max(score1,score2,score3)


                nei1 = 100
                nei2 = 100

                nei3 = 100
                nei4 = 100

                old1left1 = 0
                old1left2 = 0
                old1right1 = 0
                old1right2 = 0


                lstr1 = " "
                lstr2 = " "
                rstr1 = " "
                rstr2 = " "

                lstr11 = " "
                lstr21 = " "
                rstr11 = " "
                rstr21 = " "

                if localpos > 1:
                    lstr1 = agents[intPos[localpos-2]].p2 + " " + agents[intPos[localpos-1]].p2 + " " + agents[intPos[localpos]].p2
                if localpos < len(agents)-3:
                    rstr1 = agents[intPos[localpos]].p2 + " " + agents[intPos[localpos+1]].p2 + " " + agents[intPos[localpos+2]].p2



                localpos1 = findPos(intPos,j)
                if localpos1 > 1:
                    lstr2 = agents[intPos[localpos1-2]].p2 + " " + agents[intPos[localpos1-1]].p2 + " " + agents[intPos[localpos1]].p2
                if localpos1 < len(agents)-3:
                    rstr2 = agents[intPos[localpos1]].p2 + " " + agents[intPos[localpos1+1]].p2 + " " + agents[intPos[localpos1+2]].p2



                if localpos > 1:
                    lstr11 = agents[intPos[localpos-2]].p2 + " " + agents[intPos[localpos-1]].p2 + " " + agents[intPos[localpos1]].p2
                if localpos < len(agents)-3:
                    rstr11 = agents[intPos[localpos1]].p2 + " " + agents[intPos[localpos+1]].p2 + " " + agents[intPos[localpos+2]].p2

                if localpos1 > 1:
                    lstr21 = agents[intPos[localpos1-2]].p2 + " " + agents[intPos[localpos1-1]].p2 + " " + agents[intPos[localpos]].p2
                if localpos1 < len(agents)-3:
                    rstr21 = agents[intPos[localpos]].p2 + " " + agents[intPos[localpos1+1]].p2 + " " + agents[intPos[localpos1+2]].p2



                old1left1 = len(parser1.parse_sent(lstr1))
                old1left2 = len(parser1.parse_sent(lstr2))
                old1right1 = len(parser1.parse_sent(rstr1))
                old1right2 = len(parser1.parse_sent(rstr2))

                old1left11 = len(parser1.parse_sent(lstr11))
                old1left21 = len(parser1.parse_sent(lstr21))
                old1right11 = len(parser1.parse_sent(rstr11))
                old1right21 = len(parser1.parse_sent(rstr21))

# edge weight


                edgewt1 = newscore1 + newscore2 - localscore - otherscore - old1left1 - old1left2 - old1right1 - old1right2 + old1left11 + old1left21 + old1right11 + old1right21


                g.add_edges([(i,j)])
                id1 = g.get_eid(i,j)
                g.es[id1]["weight"] = edgewt1

# matching

    match1 =  g._maximum_bipartite_matching(g.vs["name"],g.es["weight"])

    for i in range(0,len(match1),1):
        mat = match1[i]
        if mat >= 0 :
            if  contains(changed,i)*contains(changed,mat) == 0 :
                id2 = g.get_eid(i,mat)
                edgewt2 = g.es[id2]["weight"]
                if edgewt2 > 0:
                    pos1 = findPos(intPos,i)
                    pos2 = findPos(intPos,mat)
                    intPos[pos1] = mat
                    intPos[pos2] = i
                    changed.append(i)
                    changed.append(mat)

    left = []
    right = []
    for i in range(0,len(agents),1):
        if contains(changed,i)== 0:
            if agents[i].group == "L":
                left.append(i)
            else:
                right.append(i)

    l1 = int(round(len(left)/2))
    r1 = int(round(len(right)/2))

# changing the bipartite graph

    sampleL = random.sample(left,l1)
    sampleR = random.sample(right,r1)

    for i in range(0,l1,1):
        l11 = sampleL[i]
        agents[l11].setGroup("R")



    for i in range(0,r1,1):
        r11 = sampleR[i]
        agents[r11].setGroup("L")

    groupstr1 = ""
    groupstr2 = ""
    for i in range(0,len(agents),1):
        if agents[i].group == "L":
            groupstr1 = groupstr1 + "~" + str(i)
        if agents[i].group == "R":
            groupstr2 = groupstr2 + "~" + str(i)

    counter1 = counter1 + 1


for i in range(0,len(wtstore),1):
    print(wtstore[i])


print(intPos1)
for i in range(0,len(intposstore),1):
    print(intposstore[i])
print(intPos)


for i in range(0,len(storeedges),1):
    print(storeedges[i])


plt.xlabel("Rounds")
plt.ylabel("Score")
plt.plot(totalscore)
plt.show()
