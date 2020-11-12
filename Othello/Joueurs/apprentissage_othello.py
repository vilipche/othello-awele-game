#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import joueur_horizon
import joueur_alphabeta
import joueur_alphabeta_fix
import joueur_minimax
sys.path.append("..")
from main_permutation import jouerNparties
import random



def apprentissageFaible(e, parties, elevePar, masterPar, nbEssai):
    eleve = elevePar
    master = masterPar 
    eleve.setParameters([0.2,0.1,0.1,0])
    master.setParameters([0.2,0.1,0.1,0])
    #print(eleve.coefficients)
    cpt=1
    appris=False
    while True and cpt<=nbEssai:
        print(eleve.coefficients)
        j = random.randint(0,3) #choisir un parametre
        x = random.random() #savoir si on va - ou +
        dep = None
        if (x<0.5):
            dep = -e
        else:
            dep = e

        #print("\nEssai ", cpt,"| position=",j,", e=",dep)
        before=eleve.coefficients
        v1 = jouerNparties(parties, eleve, master) 
        #print("Avant changement")
        #print(eleve.coefficients," vs ", master.coefficients,"\n",v1)
        
        #changer les parametres et rejouer
        eleve.changeParameter(j, dep)
        v2 = jouerNparties(parties, eleve, master)
        #print("Apres changement")
        #print(eleve.coefficients," vs ", master.coefficients,"\n",v2)
        print(cpt,";",before,";",eleve.coefficients,";",v1[0],";",v2[0])
        if(v1[0]<v2[0]):
            print("eleve apris!")
        #    print("Parameters changed, new parameters:", eleve.coefficients)

        else:
        #    print("De nouveau")
            eleve.changeParameter(j, -dep)



        cpt=cpt+1
    
    return eleve.coefficients

def apprentissageFaibleSansRepetition(e, parties, elevePar, masterPar, nbEssai):
    eleve = elevePar
    master = masterPar
    eleve.setParameters([0.3, -0.1, 0.1, 0.2])
    masterPar.setParameters([0.3, -0.1, 0.1, 0.2])
    
    cpt=1
    repet=False
    while True and cpt<=nbEssai:
        j = random.randint(0,3) #choisir un parametre
        x = random.random() #savoir si on va - ou +
        dep = None
        if (x<0.5):
            dep = -e
        else:
            dep = e


        print("\nEssai ", cpt,"| position=",j,", e=",dep)

        if(repet==False):
            v1 = jouerNparties(parties, eleve, master) 
            print("Avant changement")
            print(eleve.coefficients," vs ", master.coefficients,"\n",v1)
        else:
            print("Sans repetition")
            print(eleve.coefficients," vs ", master.coefficients,"\n",v1)
        #changer les parametres et rejouer
        eleve.changeParameter(j, dep)
        v2 = jouerNparties(parties, eleve, master)
        
        print("Apres changement")
        print(eleve.coefficients," vs ", master.coefficients,"\n",v2)

        if(v1[0]<v2[0]):
            print("eleve apris!")
            print("Parameters changed, new parameters:", eleve.coefficients)
            repet=False
        else:
            print("De nouveau")
            eleve.changeParameter(j, -dep)
            repet=True
        cpt=cpt+1
    
    return eleve.coefficients

a=apprentissageFaible(0.1, 5, joueur_alphabeta, joueur_alphabeta_fix, 5)
print(a)