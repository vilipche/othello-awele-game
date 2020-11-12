#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
import game

def initialiseJeu():
    """ void -> jeu
        Initialise le jeu (nouveau plateau, liste des coups joues vide, liste des coups valides None, scores a 0 et joueur = 1)
    """
    #plateau = [[4 for i in range(6)] for i in range(2)]
    plateau = [[4,4,4,4,4,4],[4,4,4,4,4,4]]
    return [plateau , 1, None, [], [0,0]]

def advaffame(jeu):
    """ jeu -> bool
        checks if the opponent starves (his row is 0)
    """
    j = game.getJoueur(jeu)
    adv = j%2+1
    return sum(jeu[0][adv-1]) == 0

def nourrit(jeu, coup):
    """ jeu, coup -> bool
        checks if a coup reaches opponents row
    """
    j = game.getJoueur(jeu)
    if (j==1):
        return coup[1]<game.getCaseVal(jeu, coup[0], coup[1])
    return game.getCaseVal(jeu, coup[0], coup[1]) + coup[1] > 5

def getCoupsValides(jeu):
    if(jeu[2]==None):
        j = game.getJoueur(jeu)
        a = advaffame(jeu)
        jeu[2]  = [(j-1,i) for i in range(6) if game.getCaseVal(jeu,j-1,i) > 0 and ((not a) or nourrit(jeu,(j-1,i)))] 
    return jeu[2]

def nextCase(l, c, horaire = False):
    if horaire:
        if c == 5 and l == 0:
            return (1,c)
        if c == 0 and l == 1 :
            return (0,c)
        if l == 0:
            return (l, c+1)
        return (l,c-1)
    else:
        if c == 5 and l == 1:
            return (0,c)
        if c == 0 and l == 0 :
            return (1,c)
        if l == 0:
            return (l, c-1)
        return (l,c+1)
        
def distribue(jeu,case):
    v = game.getCaseVal(jeu, case[0], case[1])
    nc = case
    jeu[0][case[0]][case[1]] = 0
    while v > 0:
        nc = nextCase(nc[0], nc[1])
        if not nc == case:
            jeu[0][nc[0]][nc[1]] += 1
            v -= 1
    return nc

def joueCoup(jeu, coup):
    l,c = distribue(jeu, coup)
    save = game.getCopieJeu(jeu)
    j = game.getJoueur(jeu)
    v = game.getCaseVal(jeu,l, c)
  
    while(l == (j%2) and ((v == 2) or (v == 3))):
        #print("in")
        jeu[0][l][c] = 0
        #print(jeu[0][l][c])
        jeu[-1][j-1] += v
        #print(jeu[-1][j-1])
        l,c = nextCase(l,c,True)
        v = game.getCaseVal(jeu, l, c)

    if advaffame(jeu):
        jeu[0] = save[0]
        jeu[-1] = save[-1]

    game.changeJoueur(jeu)
    jeu[2] = None
    jeu[3].append(coup)

def finJeu(jeu):
    """ jeu -> bool
        When one player has captured 25 or more seeds.
        When one player has no move to avoid the opponent to starve
        When a given position occurs for the second time with the same player's turn.
    """

    if(jeu[4][0] >= 25 or jeu[4][1] >= 25):
        return True
    
    if(game.getCoupsValides(jeu) == []):
        return True
    
    if(len(game.getCoupsJoues(jeu))>=100):
        return True

    

    return False

def affiche(jeu):
    """ jeu->void
        Affiche l'etat du jeu de la maniere suivante :
                 Coup joue = <dernier coup>
                 Scores = <score 1>, <score 2>
                 Plateau :  

                         |       0     |     1       |      2     |      ...
                    ------------------------------------------------
                      0  | <Case 0,0>  | <Case 0,1>  | <Case 0,2> |      ...
                    ------------------------------------------------
                      1  | <Case 1,0>  | <Case 1,1>  | <Case 1,2> |      ...
                    ------------------------------------------------
                    ...       ...          ...            ...
                 Joueur <joueur>, a vous de jouer
                    
         Hypothese : le contenu de chaque case ne depasse pas 5 caracteres
    """

    if(jeu[3]== []):
        print("Coup joue = None")
    else:
        print("Coup joue = ", jeu[3][-1])
    print("Joueur: ", jeu[1])
    print("Scores = ", jeu[4][0]," , ", jeu[4][1])
    print("Plateau :")
    
    plateau = jeu[0]
    
    for x in range (len(plateau[0])):
        if(x == 0):
            print("%5s|" %(""), end=" ")
        print("%5s|" %(x), end=" ")
    print()
    print("--------------------------------------------------------------")

    for i in range(len(plateau)):
        print(" ",i," |", end=" ")
        for j in range(len(plateau[i])):
            if(plateau[i][j] == 0):
                print("%5s|" %(" "), end=" ")
            else:
                if(plateau[i][j] == 1):
                    print("%5s|" %(plateau[i][j]), end=" ")
                else:
                    print("%5s|" %(plateau[i][j]), end=" ")
        print()
        print("--------------------------------------------------------------")
