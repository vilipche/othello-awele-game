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
import time

list_joueurs = [joueur_random, joueur_premier_coup]
game.joueur1 = joueur_random

def printJoueur(joueur):
    if(joueur == joueur_random):
        return "joueur_random"
    if(joueur == joueur_premier_coup):
        return "joueur_premier_coup"

for joueur2 in list_joueurs:
    game.joueur2 = joueur2
    J1 = printJoueur(game.joueur1)
    J2 = printJoueur(game.joueur2)
    j1_res = 0
    j2_res = 0

    print(J1," vs ", J2)
    parties = int(input("N des parties: "))
    n=0

    while(n<parties):
        jeu = game.game.initialiseJeu()
        it = 0   
        while(it < 100 and not game.finJeu(jeu)):
            if(jeu[1] == 1):
                coup = game.joueur1.saisieCoup(jeu)
            else:
                coup = game.joueur2.saisieCoup(jeu)
            game.joueCoup(jeu, coup)
            it=it+1
        if(game.getGagnant(jeu) == 1):
            j1_res=j1_res+1
        else:
            j2_res=j2_res+1
        n=n+1
    
    print("Apres ",n," parties:")
    print(J1,": ", j1_res)
    print(J2,": ", j2_res)
    print(J1+" gagne!" if j1_res>j2_res else J2+" gagne!")