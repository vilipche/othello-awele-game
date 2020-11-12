#!/usr/bin/env python
# -*- coding: utf-8 -*-
import awele
import sys
sys.path.append("..")
import game
game.game=awele
sys.path.append("./Joueurs")
import joueur_humain
import joueur_random
import joueur_premier_coup
import joueur_horizon
import joueur_minimax
import joueur_alphabeta
import time

game.joueur1=joueur_humain
game.joueur2=joueur_alphabeta
#parties = int(input("N des parties: "))
n=0
parties=1

j1 = 0
j2 = 0
while(n<parties):
    
    jeu = game.game.initialiseJeu()
    it = 0
    game.affiche(jeu)
    
    while(it < 100 and not game.finJeu(jeu)):
        a=input()
        print("Joueur ", game.getJoueur(jeu)," a jouer!")
        if(jeu[1] == 1):
            coup = game.joueur1.saisieCoup(jeu)
        else:
            coup = game.joueur2.saisieCoup(jeu)
        game.joueCoup(jeu, coup)
        game.affiche(jeu)
        it=it+1
        #time.sleep(0.05)

    print("Gagnant de partie = ",n,", joueur = ", game.getGagnant(jeu))
    if(game.getGagnant(jeu) == 1):
        j1=j1+1
    else:
        j2=j2+1
    n=n+1
      

print("Fin des parties!")
print("Joueur1: ", j1)
print("Joueur2: ", j2)

print("Joueur 1" if j1>j2 else "Joueur 2")


