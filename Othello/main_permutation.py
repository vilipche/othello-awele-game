#!/usr/bin/env python
# -*- coding: utf-8 -*-
import othello
import sys
sys.path.append("..")
import game
game.game=othello
sys.path.append("./Joueurs")
import joueur_random
import joueur_humain
import joueur_premier_coup
import joueur_horizon
import joueur_alphabeta
import joueur_alphabeta_fix
import minimax
import joueur_minimax
import random
import time

game.joueur1 = joueur_minimax
game.joueur2 = joueur_alphabeta

def printJoueur(joueur):
    if(joueur == joueur_random):
        return "joueur_random"
    if(joueur == joueur_premier_coup):
        return "joueur_premier_coup"
    if(joueur == joueur_minimax):
        return "joueur_minimax"
    if(joueur == joueur_horizon):
        return "joueur_horizon"
    if(joueur == joueur_alphabeta):
        return "joueur_alphabeta"
    if(joueur == joueur_alphabeta_fix):
        return "joueur_alphabeta_fix"


def jouerNparties(nbparties, joueur1, joueur2, printRes=False):
    game.joueur1 = joueur1
    game.joueur2 = joueur2
    j1_res = 0
    j2_res = 0
    n=0
    turn = 0
    parties = nbparties
    j1_finalRes = 0
    j2_finalRes = 0

    while(n<parties):
        jeu = game.game.initialiseJeu()
        it = 0 
        
        while(it < 100 and not game.finJeu(jeu)):
            if(jeu[1] == 1):
                if it<4:
                    coup = random.choice(game.getCoupsValides(jeu))
                else:
                    coup = game.joueur1.saisieCoup(jeu)
            else:
                if it<4:
                    coup = random.choice(game.getCoupsValides(jeu))
                else:
                    coup = game.joueur2.saisieCoup(jeu)
            game.joueCoup(jeu, coup)
            it=it+1

        if(game.getGagnant(jeu) == 1):
            j1_res=j1_res+1
        else:
            j2_res=j2_res+1
        n=n+1

        if(turn < 2 and n == parties): #turn nombre de fois permute
            if(printRes==True):
                print("Apres ",n," parties:")
                print("Joueur 1")
                print("\t",printJoueur(game.joueur1),": ", j1_res)
                print("Joueur 2")
                print("\t",printJoueur(game.joueur2),": ", j2_res)
                print(printJoueur(game.joueur1)+" gagne!" if j1_res>j2_res else printJoueur(game.joueur2)+" gagne!")
                
            if(turn==0):
                j1_finalRes += j1_res*(100/nbparties)
                j2_finalRes += j2_res*(100/nbparties)
            if(turn==1):
                j1_finalRes += j2_res*(100/nbparties)
                j2_finalRes += j1_res*(100/nbparties)


            if(turn == 0):
                if(printRes==True):
                    print("\n+++Permutation des joueurs!+++\n")
            
                j1 = game.joueur1
                game.joueur1 = game.joueur2
                game.joueur2 = j1
            
                j1_res = 0
                j2_res = 0
                n = 0
            turn+=1
    
    return (j1_finalRes/2, j2_finalRes/2)