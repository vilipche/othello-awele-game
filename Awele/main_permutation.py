#!/usr/bin/env python
# -*- coding: utf-8 -*-
import awele
import sys
sys.path.append("..")
import game
game.game=awele
sys.path.append("./Joueurs")
import joueur_random
import joueur_humain
import joueur_premier_coup
import joueur_horizon
import joueur_alphabeta
import joueur_alphabeta_fix
import joueur_minimax
import minimax2
import student
import time
import random
import joueur_horizon_moy
import joueur_minimax_avg

game.joueur1 = None
game.joueur2 = None

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
    if(joueur == minimax2):
        return "minimax2"
    if(joueur == student):
        return "student"
    if(joueur == joueur_minimax_avg):
        return "joueur_minimax_avg"
        
    if(joueur == joueur_ab_avg):
        return "joueur_ab_avg"

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

    #Print nodes level
    # 2 ; 5
    #print(game.joueur1.Pmax,';',game.joueur2.Pmax)

    #Print in the begining:
    #joueur_alphabeta ; joueur_minimax
    #print(printJoueur(game.joueur1),";",printJoueur(game.joueur2))

    while(n<parties):
        start_time = time.time()
        jeu = game.game.initialiseJeu()
        it = 0
        while(not game.finJeu(jeu)):
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


        #pour test de nbNoeuds et temps
        #654 ; 18161 ; 0.1686
        """
        if(turn==0):
            print(game.joueur1.nbNoeuds,";",game.joueur2.nbNoeuds,";",time.time() - start_time)
        else:
            print(game.joueur2.nbNoeuds,";",game.joueur1.nbNoeuds,";",time.time() - start_time)
        """
        game.joueur1.nbNoeuds=0
        game.joueur2.nbNoeuds=0

        #Pour tester le temps
        #2 ; 0.133156
        # 2 ; 0.133156
        # if(turn==0):
        #     print('1',';',time.time() - start_time)
        # else:
        #     print('2',';',time.time() - start_time)



        if(turn < 2 and n == parties):
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
                #print(printJoueur(game.joueur1),";",printJoueur(game.joueur2))
                j1_res = 0
                j2_res = 0
                n = 0
            turn+=1

    return (j1_finalRes/2, j2_finalRes/2)

print(jouerNparties(500, joueur_random, joueur_horizon_moy, True))

#Pour faire des stats, ca donne des resultats pour un fichier .csv

"""
# Testing the execution time

print("Depth 1")
joueur_minimax.Pmax=1
joueur_alphabeta.Pmax=1
print(jouerNparties(10,joueur_alphabeta, joueur_premier_coup))
print(jouerNparties(10,joueur_minimax, joueur_premier_coup))

print("Depth 2")
joueur_minimax.Pmax=2
joueur_alphabeta.Pmax=2
print(jouerNparties(10,joueur_alphabeta, joueur_premier_coup))
print(jouerNparties(10,joueur_minimax, joueur_premier_coup))

print("Depth 3")
joueur_minimax.Pmax=3
joueur_alphabeta.Pmax=3
print(jouerNparties(10,joueur_alphabeta, joueur_premier_coup))
print(jouerNparties(10,joueur_minimax, joueur_premier_coup))

print("Depth 4")
joueur_minimax.Pmax=4
joueur_alphabeta.Pmax=4
print(jouerNparties(10,joueur_alphabeta, joueur_premier_coup))
print(jouerNparties(10,joueur_minimax, joueur_premier_coup))

print("Depth 5")
joueur_minimax.Pmax=5
joueur_alphabeta.Pmax=5
print(jouerNparties(10,joueur_alphabeta, joueur_premier_coup))
print(jouerNparties(10,joueur_minimax, joueur_premier_coup))
"""

"""
TEST678.csv
print("Depth 6")
joueur_minimax.Pmax=6
joueur_alphabeta.Pmax=6
print(jouerNparties(10,joueur_alphabeta, joueur_premier_coup))
print(jouerNparties(10,joueur_minimax, joueur_premier_coup))

print("Depth 7")
joueur_minimax.Pmax=7
joueur_alphabeta.Pmax=7
print(jouerNparties(10,joueur_alphabeta, joueur_premier_coup))
print(jouerNparties(10,joueur_minimax, joueur_premier_coup))

print("Depth 8")
joueur_minimax.Pmax=8
joueur_alphabeta.Pmax=8
#print(jouerNparties(10,joueur_alphabeta, joueur_premier_coup))
print(jouerNparties(10,joueur_minimax, joueur_premier_coup))
"""
"""

joueur_alphabeta_fix.Pmax=3
joueur_alphabeta.Pmax=1
print(jouerNparties(10,joueur_alphabeta_fix, joueur_alphabeta))

joueur_alphabeta_fix.Pmax=3
joueur_alphabeta.Pmax=2
print(jouerNparties(10,joueur_alphabeta_fix, joueur_alphabeta))

joueur_alphabeta_fix.Pmax=3
joueur_alphabeta.Pmax=3
print(jouerNparties(10,joueur_alphabeta_fix, joueur_alphabeta))

joueur_alphabeta_fix.Pmax=3
joueur_alphabeta.Pmax=4
print(jouerNparties(10,joueur_alphabeta_fix, joueur_alphabeta))

joueur_alphabeta_fix.Pmax=3
joueur_alphabeta.Pmax=5
print(jouerNparties(10,joueur_alphabeta_fix, joueur_alphabeta))

joueur_alphabeta_fix.Pmax=3
joueur_alphabeta.Pmax=6
print(jouerNparties(10,joueur_alphabeta_fix, joueur_alphabeta))

joueur_alphabeta_fix.Pmax=3
joueur_alphabeta.Pmax=7
print(jouerNparties(10,joueur_alphabeta_fix, joueur_alphabeta))

joueur_alphabeta_fix.Pmax=3
joueur_alphabeta.Pmax=8
print(jouerNparties(10,joueur_alphabeta_fix, joueur_alphabeta))

joueur_alphabeta_fix.Pmax=3
joueur_alphabeta.Pmax=9
print(jouerNparties(10,joueur_alphabeta_fix, joueur_alphabeta))

joueur_alphabeta_fix.Pmax=3
joueur_alphabeta.Pmax=10
print(jouerNparties(10,joueur_alphabeta_fix, joueur_alphabeta))

joueur_alphabeta_fix.Pmax=3
joueur_alphabeta.Pmax=11
print(jouerNparties(10,joueur_alphabeta_fix, joueur_alphabeta))

joueur_alphabeta_fix.Pmax=3
joueur_alphabeta.Pmax=12
print(jouerNparties(10,joueur_alphabeta_fix, joueur_alphabeta))

joueur_alphabeta_fix.Pmax=3
joueur_alphabeta.Pmax=13
print(jouerNparties(10,joueur_alphabeta_fix, joueur_alphabeta))

"""
"""
joueur_alphabeta_fix.Pmax=3
joueur_alphabeta.Pmax=14
print(jouerNparties(10,joueur_alphabeta_fix, joueur_alphabeta))

joueur_alphabeta_fix.Pmax=3
joueur_alphabeta.Pmax=15
print(jouerNparties(10,joueur_alphabeta_fix, joueur_alphabeta))
<<<<<<< HEAD
"""
"""
=======
'''
'''
>>>>>>> 8a8f268a4d875f3d5b5b064df001d5c4a0da043d
# Testing the explored nodes

joueur_minimax.Pmax=1
joueur_alphabeta.Pmax=1
print(jouerNparties(5,joueur_minimax, joueur_alphabeta))


joueur_minimax.Pmax=2
joueur_alphabeta.Pmax=2
print(jouerNparties(5,joueur_minimax, joueur_alphabeta))

joueur_minimax.Pmax=3
joueur_alphabeta.Pmax=3
print(jouerNparties(5,joueur_minimax, joueur_alphabeta))

joueur_minimax.Pmax=4
joueur_alphabeta.Pmax=4
print(jouerNparties(5,joueur_minimax, joueur_alphabeta))

joueur_minimax.Pmax=5
joueur_alphabeta.Pmax=5
print(jouerNparties(5,joueur_minimax, joueur_alphabeta))
"""
