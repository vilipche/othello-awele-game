import matplotlib
import matplotlib.pyplot as plt
"""
#NODES
minimax_nodes=[99.9, 888.9, 2749.8, 18250, 54021.5]
alphabeta_nodes=[96.7, 644.6, 1703.8, 6711.4, 13349.7]
depth=[1,2,3,4,5]


plt.title('Explored nodes comparison')
plt.plot(depth,minimax_nodes)
plt.plot(depth, alphabeta_nodes,'r')
plt.legend(['Minimax','Alphabeta'], loc='upper left')
plt.xlabel('Depth')
plt.ylabel('Nodes explored')
plt.xticks(range(1,6))
plt.show()


"""
"""
#TIME
ab1 = [0.052579998970032, 0.099211859703064, 0.220445942878723, 0.695571422576904, 1.64126579761505, 4.05254559516907, 8.72490339279174]
ab2 = [0.052260231971741, 0.094255971908569, 0.277983999252319, 0.763116383552551, 2.01056332588196, 4.43745520114899, 14.6561724901199]

minimax1 = [0.052768182754517, 0.135119032859802, 0.730922961235046, 1.79874286651611, 9.42508714199066, 45.2309153079987, 213.716837501526]
minimax2 = [0.048141241073608, 0.192449188232422, 0.828680872917175, 2.68981437683105, 14.6000562429428, 54.0086671829223, 233.147355175018]

abavg = [0.052420115470887, 0.096733915805817, 0.249214971065521, 0.729343903064728, 1.8259145617485, 4.24500039815903, 11.6905379414558]
minimaxavg = [0.050454711914063, 0.163784110546112, 0.779801917076111, 2.24427862167358, 12.0125716924667, 49.6197912454605, 223.432096338272]

depth=[1,2,3,4,5,6,7]

plt.title('Execution time of one party')

plt.plot(depth,ab1)
plt.plot(depth,ab2)
plt.plot(depth,minimax1)
plt.plot(depth,minimax2)

# plt.plot(depth, minimaxavg)
# plt.plot(depth, abavg)
plt.legend(['AlphaBeta Player1','Alphabeta Player2','Minimax Player1', 'Minimax Player2'], loc='upper left')
plt.xlabel('Depth')
plt.ylabel('Time (s)')
plt.xticks(range(1,8))
plt.show()
"""
"""
#WIN DEPTH fixed 3

wins = [0,45,55,70,80,80,100,100,80,100]
depth=[1,2,3,4,5,6,7,8,9,10]


plt.title('Win % vs AlphaBeta depth 3')
plt.plot(depth,wins,'o')

plt.legend(['Alpha Beta win %'],loc='upper left')
plt.xlabel('Depth')
plt.ylabel('Win %')
plt.xticks(range(1,11))
plt.show()

"""
"""
#APPRENTISSAGE PLOTS VS 0 local1
plt.title("Local Learning, against [0,0,0,0], a=0.1")
plt.xlabel("Coefficients before change")
plt.ylabel("Win %")

paramBefore=["[0, 0, 0, 0]","[0, 0.0, 0, 0]","[0, 0.0, 0, 0.1]","[0, 0.0, 0, 0.1]","[0, 0.0, 0, 0.1]","[0.1, 0.0, 0, 0.1]","[0.1, 0.0, 0, 0.1]","[0.1, 0.0, 0, 0.1]","[0.1, 0.0, 0.0, 0.1]","[0.1, 0.0, 0.0, 0.1]"]
paramAfter = [[0, 0.1, 0, 0] , [0, 0.0, 0, 0.1] , [0, 0.1, 0, 0.1] , [0, 0.1, 0, 0.1] , [0.1, 0.0, 0, 0.1] , [0.1, 0.0, 0, 0.0] , [0.0, 0.0, 0, 0.1] , [0.1, 0.0, -0.1, 0.1] , [0.1, 0.0, 0.0, 0.0] , [0.2, 0.0, 0.0, 0.1] ]

jeux = [1,2,3,4,5,6,7,8,9,10]

scoreBefore=[65,45,85,80,85,100,100,90,100,100]
scoreAfter = [45,90,85,70,100,100,85,55,100,95]


plt.tick_params(axis='x', rotation=70)
plt.xticks(jeux, (paramBefore))

plt.plot(jeux,scoreBefore)
plt.plot(jeux,scoreAfter,'o-')

for i, txt in enumerate(paramAfter):
    plt.annotate(txt, xy=(jeux[i],scoreAfter[i]),xytext=(jeux[i]-0.2,scoreAfter[i]+1))

plt.legend(['Win % Before','Win % After'], loc='upper left')

plt.show()
"""
"""
#APPRENTISSAGE PLOTS VS 0 local2

plt.title("Local Learning, against [0.1,0,0,0.1], a=0.1")
plt.xlabel("Coefficients before change")
plt.ylabel("Win %")

paramBefore=["[0.1, 0.0, 0, 0.1]","[0.1, -0.1, 0, 0.1]","[0.1, 0.0, 0, 0.1]","[0.1, 0.0, 0.0, 0.1]","[0.1, 0.0, 0.0, 0.1]","[0.2, 0.0, 0.0, 0.1]","[0.2, 0.1, 0.0, 0.1]","[0.2, 0.1, 0.0, 0.0]","[0.2, 0.1, 0.1, 0.0]","[0.2, 0.1, 0.1, 0.0]","[0.2, 0.1, 0.1, 0.0]","[0.2, 0.1, 0.1, 0.0]","[0.2, 0.1, 0.1, 0.0]","[0.2, 0.1, 0.1, 0.0]","[0.2, 0.1, 0.1, 0.0]","[0.2, 0.1, 0.1, 0.0]","[0.2, 0.1, 0.1, 0.0]","[0.2, 0.1, 0.1, 0.0]","[0.2, 0.1, 0.1, 0.0]","[0.3, 0.1, 0.1, 0.0]","[0.3, 0.1, 0.1, 0.0]","[0.2, 0.1, 0.1, 0.0]","[0.2, 0.1, 0.1, 0.0]","[0.2, 0.2, 0.1, 0.0]","[0.2, 0.2, 0.1, 0.0]"]
paramAfter = [[0.1, -0.1, 0, 0.1] , [0.1, 0.0, 0, 0.1] , [0.1, 0.0, -0.1, 0.1] , [0.0, 0.0, 0.0, 0.1] , [0.2, 0.0, 0.0, 0.1] , [0.2, 0.1, 0.0, 0.1] , [0.2, 0.1, 0.0, 0.0] , [0.2, 0.1, 0.1, 0.0] , [0.2, 0.1, 0.2, 0.0] , [0.2, 0.1, 0.0, 0.0] , [0.2, 0.2, 0.1, 0.0] , [0.2, 0.2, 0.1, 0.0] , [0.2, 0.2, 0.1, 0.0] , [0.2, 0.2, 0.1, 0.0] , [0.2, 0.1, 0.0, 0.0] , [0.2, 0.1, 0.2, 0.0] , [0.1, 0.1, 0.1, 0.0] , [0.2, 0.1, 0.0, 0.0] , [0.3, 0.1, 0.1, 0.0] , [0.3, 0.1, 0.1, 0.1] , [0.2, 0.1, 0.1, 0.0] , [0.1, 0.1, 0.1, 0.0] , [0.2, 0.2, 0.1, 0.0] , [0.1, 0.2, 0.1, 0.0] , [0.2, 0.1, 0.1, 0.0] ]
jeux = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

scoreBefore=[40,50,45,60,65,45,25,55,45,60,70,70,70,70,70,70,65,65,60,80,65,80,30,50,40]
scoreAfter = [50,60,0,0,70,55,35,70,45,55,65,45,65,70,60,35,40,50,65,60,70,30,40,25,50]


plt.tick_params(axis='x', rotation=70)
plt.xticks(jeux, (paramBefore))

plt.plot(jeux,scoreBefore)
plt.plot(jeux,scoreAfter,'o-')

for i, txt in enumerate(paramAfter):
    plt.annotate(txt, xy=(jeux[i],scoreAfter[i]),xytext=(jeux[i]-1,scoreAfter[i]+1))

plt.legend(['Win % Before','Win % After'], loc='upper left')

plt.show()
"""
"""
#APPRENTISSAGE PLOTS VS 0 local3

plt.title("Local Learning, against [0.2, 0.1, 0.1, 0], a=0.05")
plt.xlabel("Coefficients before change")
plt.ylabel("Win %")

paramBefore=["[0.2, 0.1, 0.1, 0]","[0.2, 0.15, 0.1, 0]","[0.2, 0.15, 0.1, 0.05]","[0.2, 0.15, 0.1, 0.05]","[0.2, 0.15, 0.1, 0.05]","[0.2, 0.15, 0.15, 0.05]","[0.2, 0.15, 0.15, 0.05]","[0.2, 0.15, 0.15, 0.05]","[0.2, 0.15, 0.2, 0.05]","[0.2, 0.15, 0.2, 0.1]"]
paramAfter = [[0.2, 0.15, 0.1, 0],[0.2, 0.15, 0.1, 0.05], [0.2, 0.15, 0.05, 0.05] , [0.2, 0.15, 0.1, 0.0] , [0.2, 0.15, 0.15, 0.05] , [0.2, 0.2, 0.15, 0.05] , [0.2, 0.15, 0.2, 0.05] , [0.2, 0.15, 0.2, 0.05] , [0.2, 0.15, 0.2, 0.1] , [0.2, 0.2, 0.2, 0.1]]
jeux = [1,2,3,4,5,6,7,8,9,10]

scoreBefore=[55,35,50,45,45,35,45,35,35,25]
scoreAfter = [65,60,50,40,70,30,35,45,45,30]


plt.tick_params(axis='x', rotation=70)
plt.xticks(jeux, (paramBefore))

plt.plot(jeux,scoreBefore)
plt.plot(jeux,scoreAfter,'o-')

for i, txt in enumerate(paramAfter):
    plt.annotate(txt, xy=(jeux[i],scoreAfter[i]),xytext=(jeux[i]-1,scoreAfter[i]+1))

plt.legend(['Win % Before','Win % After'], loc='upper left')

plt.show()
"""
"""
#APPRENTISSAGE PLOTS VS PLAYER local5

plt.title("Local Learning, against [0.35, -0.15, 0.05, 0.15] a=0.1")
plt.xlabel("Coefficients before change")
plt.ylabel("Win %")

paramBefore=["[0.2, 0.0, 0.1, 0.0]","[0.2, 0.0, 0.1, 0.0]","[0.2, 0.0, 0.1, 0.0]","[0.2, 0.0, 0.1, 0.0]","[0.2, 0.0, 0.1, 0.0]","[0.2, -0.1, 0.1, 0.0]","[0.2, -0.1, 0.1, -0.1]","[0.2, -0.1, 0.1, -0.1]","[0.2, -0.1, 0.1, -0.1]","[0.2, -0.1, 0.1, -0.1]","[0.2, -0.1, 0.1, -0.1]","[0.2, -0.1, 0.1, -0.1]","[0.2, -0.1, 0.1, -0.1]","[0.2, -0.1, 0.1, -0.1]","[0.2, -0.1, 0.1, -0.1]","[0.2, -0.1, 0.1, -0.1]","[0.2, -0.1, 0.1, -0.1]","[0.2, -0.1, 0.1, -0.1]","[0.2, -0.1, 0.1, -0.1]","[0.2, -0.1, 0.1, -0.1]","[0.2, -0.1, 0.1, -0.1]","[0.2, -0.2, 0.1, -0.1]","[0.2, -0.2, 0.1, -0.1]","[0.2, -0.2, 0.1, -0.1]","[0.2, -0.2, 0.1, -0.1]"]
paramAfter = [[0.2, 0.0, 0.2, 0.0] , [0.2, 0.1, 0.1, 0.0] , [0.1, 0.0, 0.1, 0.0] , [0.1, 0.0, 0.1, 0.0] , [0.2, -0.1, 0.1, 0.0] , [0.2, -0.1, 0.1, -0.1] , [0.2, -0.1, 0.0, -0.1] , [0.2, -0.2, 0.1, -0.1] , [0.2, -0.1, 0.1, -0.2] , [0.3, -0.1, 0.1, -0.1] , [0.2, -0.1, 0.1, -0.2] , [0.2, -0.1, 0.1, 0.0] , [0.2, 0.0, 0.1, -0.1] , [0.2, -0.1, 0.1, 0.0] , [0.2, -0.1, 0.2, -0.1] , [0.1, -0.1, 0.1, -0.1] , [0.2, -0.1, 0.2, -0.1] , [0.2, -0.1, 0.0, -0.1] , [0.2, -0.1, 0.2, -0.1] , [0.2, -0.1, 0.2, -0.1] , [0.2, -0.2, 0.1, -0.1] , [0.2, -0.1, 0.1, -0.1] , [0.1, -0.2, 0.1, -0.1] , [0.2, -0.2, 0.2, -0.1] , [0.2, -0.2, 0.0, -0.1] ]
jeux = [26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]

scoreBefore=[65,50,55,40,40,30,45,40,50,60,75,65,50,65,45,60,40,55,35,60,45,55,45,45,60]
scoreAfter = [15,35,25,25,55,50,35,30,45,60,55,60,45,45,25,30,25,50,30,55,60,35,40,30,35]


plt.tick_params(axis='x', rotation=70)
plt.xticks(jeux, (paramBefore))

plt.plot(jeux,scoreBefore)
plt.plot(jeux,scoreAfter,'o-')

for i, txt in enumerate(paramAfter):
    plt.annotate(txt, xy=(jeux[i],scoreAfter[i]),xytext=(jeux[i]-1,scoreAfter[i]+1))

plt.legend(['Win % Before','Win % After'], loc='upper left')

plt.show()
"""

"""
#APPRENTISSAGE PLOTS SUPERVISE

#oracle avec coeff [0.35,-0.15, 0.05,0.15]

nbGames=[10,50,100,150,200,250,300,350,400,450,500]
xNotation = ["10","50","100","150","200","250","300","350","400","450","500"]

nodesImite1 = [ 52.51421565, 57.14893451, 54.82274025,54.74177554, 54.05672509,53.40216788,
52.96436357, 52.6876482, 52.36146302,52.01348215, 51.64705]
nodesImite2 = [55.85345, 54.88114, 55.45816, 56.53413, 56.52538, 56.05179, 55.50861, 55.22355,
54.88843, 54.35768, 54.4149]

gamesWon1 = ["60%","72%","72%","73.33333333%","73.5%","73.6%","73.33333333%","73.14285714%","73.25%","73.55555556%","72.6%"]
gamesWon2 = ["60%","52%","45%","53.33333%","53.5%","52%","51%","52.57143%","50.5%","48.44444%","49.2%"]

plt.plot(nbGames,nodesImite1)
plt.plot(nbGames,nodesImite2)

for i, txt in enumerate(gamesWon1):
    plt.annotate(txt, xy=(nbGames[i],nodesImite1[i]),xytext=(nbGames[i],nodesImite1[i]))
for i, txt in enumerate(gamesWon2):
    plt.annotate(txt, xy=(nbGames[i],nodesImite2[i]),xytext=(nbGames[i],nodesImite2[i]))

plt.legend(['As Player 1','As Player 2'], loc='upper left')
plt.title("Supervised Learning, Student Pmax=3 against AlphaBeta Pmax=3")
plt.xlabel("nb Games")
plt.ylabel("Nodes imitated")
plt.xticks(nbGames, (xNotation))

plt.show()



#oracle avec coeff [0.2,-0.25, 0.1,-0.1]

nbGames=[10,50,100,150,200,250,300,350,400,450,500]
xNotation = ["10","50","100","150","200","250","300","350","400","450","500"]

nodesImite1 = [59.36273,62.29485,62.12883,61.68201,61.7261,61.86091,61.83444,61.31272,61.19063,61.30876,61.12961]
nodesImite2 = [60.57403,59.25625,58.80775,58.74806,58.36722,58.21336,57.82651,57.31346,57.44113,57.36423,57.13254]

gamesWon1 = ["40%","66%","64%","67.33333%","65.5%","67.2%","67.33333%","67.71429%","67.5%","67.77778%","67.8%",]
gamesWon2 = ["60%","58%","50%","52%","52.5%","50.8%","51.66667%","51.71429%","50.75%","49.55556%","47.8%",]

plt.plot(nbGames,nodesImite1)
plt.plot(nbGames,nodesImite2)

for i, txt in enumerate(gamesWon1):
   plt.annotate(txt, xy=(nbGames[i],nodesImite1[i]),xytext=(nbGames[i],nodesImite1[i]))
for i, txt in enumerate(gamesWon2):
   plt.annotate(txt, xy=(nbGames[i],nodesImite2[i]),xytext=(nbGames[i],nodesImite2[i]))

plt.legend(['As Player 1','As Player 2'], loc='upper left')
plt.title("Supervised Learning, Student Pmax=3 against AlphaBeta Pmax=3")
plt.xlabel("nb Games")
plt.ylabel("Nodes imitated")
plt.xticks(nbGames, (xNotation))

plt.show()
"""


#with oracle i alphabeta coeff:
#SCORE= 0.2
#LINE = -0.2
#DIFF = 0.1
#ADVLINE = -0.1

nbGames=[10,50,100,150,200,250,300,350,400,450,500]
xNotation = ["10","50","100","150","200","250","300","350","400","450","500"]

nodesImite1 = [62.76811,59.56057,60.2546,59.93172,59.9672,59.55538,58.95636,58.846,58.38386,58.10994,57.99429]
nodesImite2 = [65.71733,57.59925,58.51975,58.97584,58.60959,58.04427,57.73381,57.71012,57.50022,57.46645,57.17719]

gamesWon1 = ["60%","44%","40%","39.33333%","42.5%","43.2%","44.33333%","44.57143%","45.25%","45.77778%","46%"]
gamesWon2 = ["30%","52%","54%","58.66667%","55.5%","54%","55%","54.57143%","53.75%","51.77778%","51%"]

plt.plot(nbGames,nodesImite1)
plt.plot(nbGames,nodesImite2)

for i, txt in enumerate(gamesWon1):
   plt.annotate(txt, xy=(nbGames[i],nodesImite1[i]),xytext=(nbGames[i],nodesImite1[i]))
for i, txt in enumerate(gamesWon2):
   plt.annotate(txt, xy=(nbGames[i],nodesImite2[i]),xytext=(nbGames[i],nodesImite2[i]))

plt.legend(['As Player 1','As Player 2'], loc='upper left')
plt.title("Supervised Learning, Student Pmax=3 against AlphaBeta Pmax=3 \
            Oracle coeff: [0.2,-0.2,0.1.-0.1] AlphaBeta coeff: [0.2,-0.2,0.1.-0.1]")
plt.xlabel("nb Games")
plt.ylabel("\"Coups\" imitated")
plt.xticks(nbGames, (xNotation))

plt.show()


'''
#with oracle i alphabeta coeff:
#for alphabeta:
#SCORE= 5
#LINE = 1
#DIFF = 3
#ADVLINE = 4
#for oracle:
#SCORE= 0.2
#LINE = -0.2
#DIFF = 0.1
#ADVLINE = -0.1



nbGames=[10,50,100,150,200,250,300,350,400,450,500]
xNotation = ["10","50","100","150","200","250","300","350","400","450","500"]

nodesImite1 = [61.60437,62.18491,62.23044,62.06572,61.72168,61.84409,61.4731,61.07702,60.89685,60.8471,60.85401]
nodesImite2 = [61.35557,58.64818,59.89349,59.50801,58.64927,58.43239,58.57242,58.43136,58.33624,58.17989,57.84216]

gamesWon1 = ["80%","72%","73%","74%","73.5%","73.2%","72%","70%","70.25%","69.77778%","68.4%"]
gamesWon2 = ["70%","56%","55%","51.33333%","52.5%","53.2%","54%","52.85714%","52%","51.33333%","51.4%"]

plt.plot(nbGames,nodesImite1)
plt.plot(nbGames,nodesImite2)

for i, txt in enumerate(gamesWon1):
   plt.annotate(txt, xy=(nbGames[i],nodesImite1[i]),xytext=(nbGames[i],nodesImite1[i]))
for i, txt in enumerate(gamesWon2):
   plt.annotate(txt, xy=(nbGames[i],nodesImite2[i]),xytext=(nbGames[i],nodesImite2[i]))

plt.legend(['As Player 1','As Player 2'], loc='upper left')
plt.title("Supervised Learning, Student Pmax=3 against AlphaBeta Pmax=3 \
            Oracle coeff: [0.2,-0.2,0.1.-0.1] AlphaBeta coeff: [5,1,3,4]")
plt.xlabel("nb Games")
plt.ylabel("\"Coups\" imitated")
plt.xticks(nbGames, (xNotation))

plt.show()
'''
