#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import joueur_horizon
import joueur_alphabeta
import joueur_random
import random
import student
import oracle
sys.path.append("..")
import othello
#from main_permutation import jouerNparties
sys.path.append("..")
import game

#za test:
#statsot da ne bide za sekoja partija tuku za n broj partii pobedi.

#podobro da igra portiv player so ista dlabocina i nauceni koeficienti, otkolku protiv podlaboko.
#vakvi rezultati dobivame bidejki protivnikot e na pogolema dlabocina i e normalno

game.joueur1 = None
game.joueur2 = None

game.game=othello

def apprentissageSupervise():
    a = 0.1
    jeux=1
    while True:
        jeuInit = game.initialiseJeu()

        game.joueur1 = student
        game.joueur2 = joueur_alphabeta
        eleve = game.joueur1


        nbCoupsTourne1=0
        nbCoupsImite1=0

        turn=0

        while not game.finJeu(jeuInit):
            if game.getJoueur(jeuInit) == 1: #monJoueur == 1

                coups = game.getCoupsValides(jeuInit)
                prof_coups = []

                alpha=float("-inf")
                beta=float("inf")
                #on joue l'oracle
                for c in coups:
                    #print("FOR1")
                    j = game.getCopieJeu(jeuInit)
                    oracle.monJoueur = game.getJoueur(j)
                    game.joueCoup(j, c)
                    #liste des scores de oracle
                    val = oracle.estimationBetaMin(j, alpha, beta)
                    prof_coups.append(val)
                    alpha = max(val, alpha)

                opt_max_index = prof_coups.index(max(prof_coups)) #index de score maximal
                opt = coups[opt_max_index] #coup avec score maximal (meilleur coup)

                #потегот оракл што го направил, ние земаме и одлучуваме дека е најдобар и го играме
                copy_opt = game.getCopieJeu(jeuInit)
                eleve.monJoueur = game.getJoueur(copy_opt) #on change la variable globale dans le fichier eleve (utilise dans saisie coup)
                game.joueCoup(copy_opt, opt) #eleve joue meilleur coup d'oracle. On utilise copy_opt dans l'evaluation

                #trouver lest coups possibles tq o(c)<o(opt)
                coups_a_jouer = []
                for i in range(len(coups)):
                    #on cree la liste o(c) < o(opt)
                    #print("FOR2")
                    if prof_coups[i]<prof_coups[opt_max_index]:
                        coups_a_jouer.append(coups[i])



                for cp in coups_a_jouer:
                    #print('asdasd')
                    copie = game.getCopieJeu(jeuInit)
                    eleve.monJoueur = game.getJoueur(copie)
                    game.joueCoup(copie,cp)
                    o=eleve.evaluation(copy_opt) #evaluacija na eleve za najdobriot poteg na oracle
                    s=eleve.evaluation(copie) #evaluacijata na eleve za polosite potezi
                    changedParam = []
                    nbCoupsTourne1+=1
                    if (o-s) < 1:
                        for j in range(len(eleve.coefficients)):
                            scjo = eleve.scores(copy_opt)[j]
                            scjc = eleve.scores(copie)[j]
                            changedParam.append(eleve.coefficients[j] - a * (scjc - scjo))

                        eleve.setParameters(changedParam)
                    else:
                        nbCoupsImite1+=1 #tie coups sto ne se koregirani sto se dobri.

                #procent kolku coups ne se koregirani od oracle, sto znaci deka se imitirani

                #print(prof_coups)
                #print(coups_a_jouer)

                if(turn > 4):
                    coupJoueEleve = eleve.saisieCoup(jeuInit)
                else:
                    coupJoueEleve = joueur_random.saisieCoup(jeuInit)

                game.joueCoup(jeuInit, coupJoueEleve)

                turn+=1

            else:
                if(turn > 4):
                    game.joueCoup(jeuInit, game.joueur2.saisieCoup(jeuInit))
                else:
                    game.joueCoup(jeuInit, joueur_random.saisieCoup(jeuInit))


        #print("------",jeux,"------")
        #print("a=",a)
        #print(eleve.coefficients)
        #print("eleve vs alphabeta: ",game.getScores(jeuInit))
        #print("Coups imite ", nbCoupsImite1," NbTournes ", nbCoupsTourne1 ," % ", (nbCoupsImite1/nbCoupsTourne1)*100)
        a*=0.999
        #print()
        if(game.getGagnant(jeuInit) == 1):
            gagne = 1
        else:
            gagne = 0
        print(nbCoupsTourne1)
        print(jeux,";1;",(nbCoupsImite1/nbCoupsTourne1)*100,";",gagne,";",eleve.coefficients)
        ###################################################################################################
        jeuInit = game.initialiseJeu()
        game.joueur1 = joueur_alphabeta
        game.joueur2 = student
        eleve = game.joueur2


        nbCoupsTourne2=0
        nbCoupsImite2=0

        turn=0

        while not game.finJeu(jeuInit):
            if game.getJoueur(jeuInit) == 2: #monJoueur == 1

                coups = game.getCoupsValides(jeuInit)
                prof_coups = []

                alpha=float("-inf")
                beta=float("inf")
                #on joue l'oracle
                for c in coups:
                    #print("FOR1")
                    j = game.getCopieJeu(jeuInit)
                    oracle.monJoueur = game.getJoueur(j)
                    game.joueCoup(j, c)
                    #liste des scores de oracle
                    val = oracle.estimationBetaMin(j, alpha, beta)
                    prof_coups.append(val)
                    alpha = max(val, alpha)

                opt_max_index = prof_coups.index(max(prof_coups)) #index de score maximal
                opt = coups[opt_max_index] #coup avec score maximal (meilleur coup)

                #потегот оракл што го направил, ние земаме и одлучуваме дека е најдобар и го играме
                copy_opt = game.getCopieJeu(jeuInit)
                eleve.monJoueur = game.getJoueur(copy_opt) #on change la variable globale dans le fichier eleve (utilise dans saisie coup)
                game.joueCoup(copy_opt, opt) #eleve joue meilleur coup d'oracle. On utilise copy_opt dans l'evaluation

                #trouver lest coups possibles tq o(c)<o(opt)
                coups_a_jouer = []
                for i in range(len(coups)):
                    #on cree la liste o(c) < o(opt)
                    #print("FOR2")
                    if prof_coups[i]<prof_coups[opt_max_index]:
                        coups_a_jouer.append(coups[i])



                for cp in coups_a_jouer:
                    #print('asdasd')
                    copie = game.getCopieJeu(jeuInit)
                    eleve.monJoueur = game.getJoueur(copie)
                    game.joueCoup(copie,cp)
                    o=eleve.evaluation(copy_opt) #evaluacija na eleve za najdobriot poteg na oracle
                    s=eleve.evaluation(copie) #evaluacijata na eleve za polosite potezi
                    changedParam = []
                    nbCoupsTourne2+=1
                    if (o-s) < 1:
                        for j in range(len(eleve.coefficients)):
                            scjo = eleve.scores(copy_opt)[j]
                            scjc = eleve.scores(copie)[j]
                            changedParam.append(eleve.coefficients[j] - a * (scjc - scjo))

                        eleve.setParameters(changedParam)
                    else:
                        nbCoupsImite2+=1 #tie coups sto ne se koregirani sto se dobri.

                #procent kolku coups ne se koregirani od oracle, sto znaci deka se imitirani

                #print(prof_coups)
                #print(coups_a_jouer)

                if(turn > 4):
                    coupJoueEleve = eleve.saisieCoup(jeuInit)
                else:
                    coupJoueEleve = joueur_random.saisieCoup(jeuInit)

                game.joueCoup(jeuInit, coupJoueEleve)

                turn+=1

            else:
                if(turn > 4):
                    game.joueCoup(jeuInit, game.joueur2.saisieCoup(jeuInit))
                else:
                    game.joueCoup(jeuInit, joueur_random.saisieCoup(jeuInit))



        #print("------",jeux,"------")
        #print("a=",a)
        #print(eleve.coefficients)
        #print("alphabeta vs eleve",game.getScores(jeuInit))

        #print("Coups imite ", nbCoupsImite2," NbTournes ", nbCoupsTourne2 ," % ", (nbCoupsImite2/nbCoupsTourne2)*100)
        a*=0.999
        #print()
        if(game.getGagnant(jeuInit) == 1):
            gagne = 0
        else:
            gagne = 1
        print(jeux,";2;",(nbCoupsImite2/nbCoupsTourne2)*100,";",gagne,";",eleve.coefficients)
        jeux+=1

apprentissageSupervise()
