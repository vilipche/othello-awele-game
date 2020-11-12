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
    ligneJoueur = game.getJoueur(jeu) - 1
    colonne = int(input("Votre colonne:"))

    while((ligneJoueur, colonne) not in game.getCoupsValides(jeu)):
        colonne = int(input("Coup invalid ! Votre colonne:"))

    return (ligneJoueur, colonne)