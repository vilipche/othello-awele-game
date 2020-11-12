#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game
import random

SCORE= 1
LINE = 0
DIFF = 0
ADVLINE = 0

monJoueur = None


Pmax = 2
def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    global monJoueur 
    monJoueur = game.getJoueur(jeu)

    return decisionMINIMAX(jeu)

def decisionMINIMAX(jeu):
    cpMax=None
    valMax=None

    for cp in game.getCoupsValides(jeu):
        j = game.getCopieJeu(jeu)
        game.joueCoup(j, cp)   

        val = estimationMIN(j)
        if valMax is None or val>valMax:
            valMax=val
            cpMax=cp

    return cpMax 

    
def estimationMAX(jeu, p=1):
    Vmax=float("-inf")

    if game.finJeu(jeu):
        g = game.getGagnant(jeu)
        if g == monJoueur:
            return 1000
        else:
            return -1000
    if p == Pmax:
        #print("VMAX:",Vmax)
        return evaluation(jeu)
    #game.changeJoueur(jeu)
    coups=game.getCoupsValides(jeu)

    for cp in coups:
        j = game.getCopieJeu(jeu)
        game.joueCoup(j, cp) 
        
        v = estimationMIN(j,p+1)
        #print(cp," ",v," ", p)
        if Vmax<v :
            Vmax = v
   # print("VMAX:",Vmax)
    return Vmax

def estimationMIN(jeu, p=1):
    Vmin=float("inf")
    if game.finJeu(jeu):
        g = game.getGagnant(jeu)
        if g == monJoueur:
            return 1000
        else:
            return -1000
    if p == Pmax:
        #print("VMIN:",Vmin)
        return evaluation(jeu)
    
    #game.changeJoueur(jeu)
    coups=game.getCoupsValides(jeu)


    for cp in coups:
        j = game.getCopieJeu(jeu)
        game.joueCoup(j, cp) 
       
        v = estimationMAX(j,p+1)
        #print(cp," ",v," ", p)

        if Vmin>v :
            Vmin = v
   # print("VMIN:",Vmin)

    return Vmin


def evaluation(jeu):
    a = SCORE * evaluationScore(jeu) + LINE * evaluationLine(jeu) \
        + DIFF * evaluationDifference(jeu) + ADVLINE * evalutationLineAdv(jeu)
    #print(a)
    return a
          
def evaluationScore(jeu):
    """ jeu -> reel
        retourner le coup qui donne le meilleur resultat
    """
    #print(((game.getScore(jeu,monJoueur-48))/48)*100)
    return  game.getScore(jeu, monJoueur)-game.getScore(jeu, monJoueur%2+1)

def evaluationDifference(jeu):
    adv = monJoueur % 2 + 1
    if(monJoueur == 1):
        mesCases = jeu[0][0]
        advCases = jeu[0][1]
    else:
        mesCases = jeu[0][1]
        advCases = jeu[0][0]

    #print(100*((sum(mesCases)-sum(advCases))/48))
    return 100*((sum(mesCases)-sum(advCases))/48)


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
    
    