#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game
import random


def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    """
    colonne = random.randint(0, len(game.getCoupsValides(jeu))-1)
    print(len(game.getCoupsValides(jeu))-1, colonne)
    """
    #print(game.getCoupsValides(jeu))
    return random.choice(game.getCoupsValides(jeu))
    