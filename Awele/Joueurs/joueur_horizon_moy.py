#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../..")
import game

SCORE= 1
LINE = 0
DIFF = 0
ADVLINE = 0

coefficients = [SCORE, LINE, DIFF, ADVLINE]

monJoueur = None

Pmax = 2

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
    listvaleurs=[]
    for cp in game.getCoupsValides(jeu):
        j = game.getCopieJeu(jeu)
        game.joueCoup(j, cp)
        listvaleurs.append(estimation(j,p+1))

    avgValue = sum(listvaleurs)/len(listvaleurs)

    closestValue = min(listvaleurs, key=lambda x:abs(x-avgValue))
    return closestValue
    
"""
def decision(jeu):
    
       # Returns the move with the closest value to average from all moves.
      
    listcoups = []
    listvaleurs = []

    for cp in game.getCoupsValides(jeu):
        j = game.getCopieJeu(jeu)
        game.joueCoup(j, cp) 

        listvaleurs.append(estimation(j))
        listcoups.append(cp)

    avgValue = sum(listvaleurs)/len(listvaleurs)

    closestValue = min(listvaleurs, key=lambda x:abs(x-avgValue))

    return listcoups[listvaleurs.index(closestValue)]


def estimation(jeu, p=1):
    if game.finJeu(jeu):
        g = game.getGagnant(jeu)
        if g == monJoueur:
            return 1000
        else:
            return -1000

    if p == Pmax:
        return evaluation(jeu)
"""
    

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
    """ jeu -> reel
        retourner le coup qui donne le meilleur resultat
    """

    return game.getScore(jeu, monJoueur)

def evaluationDifference(jeu):
    adv = monJoueur % 2 +1
    return game.getScore(jeu, monJoueur) - game.getScore(jeu, adv)

def evaluationLine(jeu):
        
    if(monJoueur == 1):
        mesCases = jeu[0][0]
    else:
        mesCases = jeu[0][1]
    
    cpt=6
    for i in mesCases:
        if(i in [1,2]):
            cpt-=1
    
    return cpt
      


def evalutationLineAdv(jeu):
    if(monJoueur == 1):
        advCases = jeu[0][1]
    else:
        advCases = jeu[0][0]
    cpt=0
    for i in advCases:
        if(i in [1,2]):
            cpt+=1
    
    return cpt
    
