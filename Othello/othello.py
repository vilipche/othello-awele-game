#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import reduce

import sys
sys.path.append("..")
import game

def initialiseJeu():
    """ void -> jeu
        Initialise le jeu (nouveau plateau, liste des coups joues vide, liste des coups valides None, scores a 0 et joueur = 1)
    """
    plateau = [[0 for i in range(8)] for i in range(8)]

    plateau[3][3] = 1
    plateau[4][4] = 1
    plateau[4][3] = 2
    plateau[3][4] = 2
    
   
    

    return [plateau , 1, None, [], [2,2]]


def coups(jeu):
    """jeu->list
        les cases vide autour les cases d'adversaire
    """
    adv = jeu[1]%2 + 1
    s = [entourageVide(jeu, l, c) for l in range(8) for c in range(8) if jeu[0][l][c]==adv]
    s = reduce(lambda a,b:a|b,s)
    return s

def entourageVide(jeu, l, c):
    """ jeu, l, c, -> set
        retourne tous les cases vides autour la case l,c
    """
    return {(l+i, c+j) for i in [-1,0,1] for j in [-1,0,1] if (c+j <= 7) and (c+j>=0) \
    and (l+i<=7) and (l+i>=0) and jeu[0][l+i][c+j] == 0}

def getCoupsValides(jeu):
    """ jeu -> list
        retourne les coups valides a jouer
    """
    if(jeu[2]==None):
        coup = coups(jeu)
        jeu[2] = [x for x in coup if len(getEncadrements(jeu, x , False)) > 0]
    return jeu[2]

def getEncadrements(jeu, c, all = True):
    """ jeu -> list
        retourne la liste des directions
        all: if true, retourne tous les directions possibles de coup c
            if false, retourne un seul. (si il existe)
    """
    ret = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if(i==0 and j ==0):
                continue
            if checkEncadrementDirection(jeu, c, i, j):
                ret.append((i,j))
                if not all:
                    break
    return ret

def checkEncadrementDirection(jeu, cp , i ,j):
    """
    """
    ok = False
    l, c = cp
    while True:
        l+=i
        c+=j
        if(l>7 or l<0 or c>7 or c<0):
            return False
        if(jeu[0][l][c] == 0):
            return False
        if(jeu[0][l][c] == jeu[1]):
            return ok
        ok = True

def joueCoup(jeu, cp):
    jeu[0][cp[0]][cp[1]] = jeu[1]
    jeu[4][game.getJoueur(jeu)-1] += 1
    d = getEncadrements(jeu, cp)
    for x in d:
        returnPions(jeu, cp, x)
    jeu[3].append(cp)
    jeu[2] = None
    jeu[1] = jeu[1]%2 +1



def returnPions(jeu, cp, x):
    """ jeu->void
        retourne les pions dans la direction x
    """
    joueur = game.getJoueur(jeu)
   

  
    while(jeu[0][cp[0]+x[0]][cp[1]+x[1]] == joueur % 2 + 1):
        jeu[0][cp[0]+x[0]][cp[1]+x[1]] = joueur

        jeu[4][joueur-1]+=1
        jeu[4][joueur%2]-=1

        cp = cp[0]+x[0],cp[1]+x[1]
  
        
def finJeu(jeu):
    """
        
    """
    if(jeu[4][0] == 0 or jeu[4][1] == 0):
        return True
    if(jeu[4][0]+jeu[4][1] == 64):
        return True

    if(game.getCoupsValides(jeu) == []):
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
                    print("\x1b[0;30;43m%5s\x1b[0m|" %(plateau[i][j]), end=" ")
                else:
                    print("\x1b[0;30;41m%5s\x1b[0m|" %(plateau[i][j]), end=" ")
        print()
        print("--------------------------------------------------------------")
