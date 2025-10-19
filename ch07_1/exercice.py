#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
from math import pi as PI

from ch06_1.exercice import frequence
#  python -m ch07_1.exercice

from turtle import *


# TODO: Définissez vos fonction ici
def volume_masse_ellipsoide( a, b, c, masse_volumique):
    volume = 4/3 * PI * a * b * c
    masse = masse_volumique * volume 
    return (volume, masse)

def max_frequence(phrase):
    print(phrase)
    dictionnaire_frequence = frequence(phrase)
    print(f"plus fréquent : '{sorted(dictionnaire_frequence.items(), key= lambda item: item[1], reverse=True)[0][0]}'")

def dessiner_arbre():
    color('green')
    penup()
    setpos(0,-200)
    print(pos())
    pendown()
    left(90)
    size = 10
    longueur = 100
    position = pos()
    dessiner_branche( position, size, longueur, 'gauche')
    dessiner_branche( position, size, longueur, 'droite')
    # dessiner_branche()
    done()

def dessiner_branche( position, size, longueur, cote):
    penup()
    setpos(position)
    pendown()
    pensize(size)
    if cote == 'gauche':
        left(-25)
    else:
        left(50)
    forward(longueur)
    if size > 0 and longueur > 0:
        dessiner_branche( pos(), size - 1, longueur - 10, 'gauche')
        dessiner_branche( pos(), size - 1, longueur - 10, 'droite')

def valider_adn(chaine):
    collection = set(chaine)
    liste = list(collection)
    liste.sort()
    texte = ''.join(liste)
    print('texte', texte)
    if len(texte) == 0:
        return False
    for lettre in texte:
        if lettre not in 'acgt':
            False
    return True

def saisir_chaine():
    chaine = ''
    while not valider_adn(chaine):
        chaine = input("Veuillez saisir la séquence ADN : ")
    return chaine

def calculer_proportion( adn, reference ):
    if len(adn) == 0:
        return 0
    frequence = adn.count(reference)
    return frequence * len(reference) / len(adn) * 100

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    a = 3
    b = 5
    c = 5
    masse_volumique = 10
    volume, masse = volume_masse_ellipsoide( a, b, c, masse_volumique)
    print(f"Volume : {volume}, masse : {masse}")

    phrase = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    max_frequence(phrase)

    # dessiner_arbre()

    print(valider_adn('agcgagcgagacgagcttttagat'))
    ADN = saisir_chaine()
    print(ADN)
    reference = 'ca'
    proportion = calculer_proportion(ADN, reference)
    print(f"Proportion de {reference} dans {ADN} : {proportion} %")

