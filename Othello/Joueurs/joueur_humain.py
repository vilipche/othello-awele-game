#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    print("Coups valides: ", game.getCoupsValides(jeu))

    ligne = int(input("Votre ligne: "))
    colonne = int(input("Votre colonne: "))

    while((ligne, colonne) not in game.getCoupsValides(jeu)):
        print("Coup invalid!")
        ligne = int(input("Votre ligne: "))
        colonne = int(input("Votre colonne: "))

    return (ligne, colonne)
    
