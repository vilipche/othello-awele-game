#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    """
    colonne = random.randint(0, len(game.getCoupsValides(jeu))-1)
    print(len(game.getCoupsValides(jeu))-1, colonne)
    """
    return game.getCoupsValides(jeu)[0]