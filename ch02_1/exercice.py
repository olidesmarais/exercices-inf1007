#!/usr/bin/env python
# -*- coding: utf-8 -*-

ecart_majuscule_minuscule = ord('a') - ord('A')

def majuscule(mot):
    # TODO completer la fonction ici
    resultat = ''
    for lettre in mot:
        # Si la lettre est une lettre minuscule
        if ord('a') <= ord(lettre) <= ord('z'):
            resultat += chr(ord(lettre) - ecart_majuscule_minuscule)
        else:
            resultat += lettre
    return resultat


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
