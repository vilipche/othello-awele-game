#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game

SCORE   = 1
CORNER  = 0
MID     = 0
XC      = 0
POS     = 0

coefficients = [SCORE, CORNER, MID, XC, POS]

Pmax = 1
monJoueur = None

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    global monJoueur 
    monJoueur = game.getJoueur(jeu)

    return decision(jeu)

def decision(jeu):
    valMax=None
    cpMax=None

    for cp in game.getCoupsValides(jeu):
        j = game.getCopieJeu(jeu)
        game.joueCoup(j, cp) 

        val = estimation(j)
        if valMax is None or val>valMax:
            valMax=val
            cpMax=cp

    return cpMax

def estimation(jeu, p=1):
    if game.finJeu(jeu):
        g = game.getGagnant(jeu)
        if g == monJoueur:
            return 1000
        else:
            return -1000

    if p == Pmax:
        return evaluation(jeu)

    Vmax=float("-inf")
    coups=game.getCoupsValides(jeu)
    for cp in coups:
        j = game.getCopieJeu(jeu)
        game.joueCoup(j, cp) 
        
        v = estimation(j,p+1)
        if Vmax<v :
            Vmax = v
    return Vmax
    
def scores(jeu):
    """ jeu -> list
        retourne une liste des scores d'evaluation
    """
    return [evaluationScore(jeu), evaluationLine(jeu), evaluationDifference(jeu), evalutationLineAdv(jeu)]

def dot(jeu, coef):
    """ jeu, coef(list) -> float
        produit scalaire de liste des evaluations et coefficients
    """
    evl = scores(jeu)
    if (len(evl) == len(coef)):
        s=0
        for i in range(len(coef)):
            s+=coef[i]*evl[i]
    return s

def evaluation(jeu):
    return dot(jeu, coefficients)


def evaluationScore(jeu):
    return  game.getScore(jeu, monJoueur)-game.getScore(jeu, monJoueur%2+1)
    

def evalutaionCorner(jeu):
    cpt=0
    for i in 0,7:
        for j in 0,7:
            if(jeu[0][i][j] == monJoueur):
                cpt+=1
    return cpt

def evaulationXC(jeu):
    cpt=0
    for i in 0,1,6,7:
        for j in 0,1,6,7:
            if((i,j) != (0,0) and (i,j) != (7,7) and (i,j) != (0,7) and (i,j) != (7,0)):
                if(jeu[0][i][j] == monJoueur):
                    cpt+=1
    return -cpt
        
def evaluationMiddleSquare(jeu):
    mid=0
    for i in 3,4:
        for j in 3,4:
            if(jeu[0][i][j] == monJoueur):
                mid+=1
    return -mid

positional =   [[ 99, -8,  8,  6,  6,  8, -8, 99],
                [ -8,-24, -4, -3, -3, -4,-24, -8],
                [  8, -4,  7,  4,  4,  7, -4,  8],
                [  6, -3,  4,  0,  0,  4, -3,  6],
                [  6, -3,  4,  0,  0,  4, -3,  6],
                [  8, -4,  7,  4,  4,  7, -4,  8],
                [ -8,-24, -4, -3, -3, -4,-24, -8],
                [ 99, -8,  8,  6,  6,  8, -8, 99]]

def evaluationPositional(jeu):
    plateau=game.getPlateau(jeu)
    s=0
    for i in range(plateau):
        for j in range(plateau[0]):
            if(plateau[i][j]==monJoueur):
                s+=positional[i][j]
    return s
        