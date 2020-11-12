#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game

# SCORE= 1.7341850698306929
# LINE = -0.11697226951172592
# DIFF = -0.1445751048255119
# ADVLINE = -1.2911490430059458

SCORE= 0.2
LINE = -0.2
DIFF = 0.1
ADVLINE = -0.1

coefficients = [SCORE, LINE, DIFF, ADVLINE]

def changeParameter(position, val):
    global coefficients
    coefficients[position]+=val

def setParameters(param):
    global coefficients
    coefficients = param

Pmax = 3

nbNoeuds = 0
monJoueur = None

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    global monJoueur
    monJoueur = game.getJoueur(jeu)

    return decisionAB(jeu)


def decisionAB(jeu):
    alpha = float("-inf")
    beta = float("inf")
    valMax=None
    cpMax=None

    for cp in game.getCoupsValides(jeu):
        j = game.getCopieJeu(jeu)
        game.joueCoup(j, cp)

        val = estimationBetaMin(j, alpha, beta)
        global nbNoeuds
        nbNoeuds+=1
        if valMax is None or val>valMax:
            valMax=val
            cpMax=cp

        alpha = max(alpha, val)

    return cpMax



def estimationAlphaMax(jeu, alpha, beta, p=1):
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
        v = estimationBetaMin(j, alpha, beta, p+1)
        global nbNoeuds
        nbNoeuds+=1
        if Vmax<v :
            Vmax = v
        if Vmax >= beta:
            return Vmax
        alpha = max(alpha, Vmax)
    return Vmax

def estimationBetaMin(jeu, alpha, beta, p=1):
    if game.finJeu(jeu):
        g = game.getGagnant(jeu)
        if g == monJoueur:
            return 1000
        else:
            return -1000
    if p == Pmax:
        return evaluation(jeu)
    Vmin=float("inf")
    coups=game.getCoupsValides(jeu)
    for cp in coups:
        j = game.getCopieJeu(jeu)
        game.joueCoup(j, cp)
        v = estimationAlphaMax(j,alpha, beta, p+1)
        global nbNoeuds
        nbNoeuds+=1
        if Vmin>v :
            Vmin = v
        if Vmin <= alpha:
            return Vmin
        beta = min(beta, Vmin)
    return Vmin

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
    s=0
    if (len(evl) == len(coef)):
        for i in range(len(coef)):
            s+=coef[i]*evl[i]
    return s

def evaluation(jeu):
    return dot(jeu, coefficients)

def evaluationScore(jeu):
    """ jeu -> reel
        retourner le coup qui donne le meilleur resultat
    """
    return  game.getScore(jeu, monJoueur)-game.getScore(jeu, monJoueur%2+1)

def evaluationDifference(jeu):
    """
        retourner la difference des graines de ces cases
    """
    adv = monJoueur % 2 + 1
    if(monJoueur == 1):
        mesCases = jeu[0][0]
        advCases = jeu[0][1]
    else:
        mesCases = jeu[0][1]
        advCases = jeu[0][0]

    #print(100*((sum(mesCases)-sum(advCases))/48))
    #return 100*((sum(mesCases)-sum(advCases))/48)
    return sum(mesCases)-sum(advCases)

def evaluationLine(jeu):
    """
        N'avoir pas des cases avec des 1 et 2 graines dans notre cote
    """
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
    """
        Avoir des cases avec des 1 et 2 graines de cote d'adversaire
    """
    if(monJoueur == 1):
        advCases = jeu[0][1]
    else:
        advCases = jeu[0][0]
    cpt=0
    for i in advCases:
        if(i in [1,2]):
            cpt+=1

    return cpt
