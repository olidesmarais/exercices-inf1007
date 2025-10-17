#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List


def convert_to_absolute(number: float) -> float:
    return -number if number < 0 else number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    resultat = []
    for prefixe in prefixes:
        resultat.append(prefixe + suffixe)
    return resultat


def prime_integer_summation() -> int:
    nombre_premier = [2, 3, 5]
    nombre = 6
    while len(nombre_premier) < 100:
        est_premier = True
        for diviseur in range(2, nombre // 2):
            if nombre % diviseur == 0:
                est_premier = False
                break
        if est_premier:
            nombre_premier.append(nombre)
        nombre += 1
    return sum(nombre_premier)


def factorial(number: int) -> int:
    resultat = 1
    index = 1
    while index < number:
        resultat *= index
        index += 1
    return resultat


def use_continue() -> None:
    for index in range( 1, 11):
        if index == 5:
            continue
        else:
            print(index)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    resultat = []
    for groupe in groups:
        # - Critère de taille: Si le groupe possède plus que 10 membres ou 3 membres et moins, il n'est pas acceptable
        if not 3 < len(groupe) <= 10:
            resultat.append(False)
            continue
        # - Critère d'âge: Si au moins un membre du groupe à exactement 25 ans, alors le groupe est acceptable peut-importe les autres critères d'âges
        if 25 in groupe:
            resultat.append(True)
            continue
        mineur = False
        plus_70 = False
        # - Critère d'âge: Si au moins un membre du groupe est mineur, le groupe n'est pas acceptable
        # - Critère d'âge: Si un membre du groupe est plus vieux que 70 ans et qu'un autre membre du groupe à exactement 50 ans, 
        #   le groupe n'est pas acceptable
        if (min(groupe) < 18) or (50 in groupe and max(groupe) > 70):
            resultat.append(False)

        resultat.append(True)
    return resultat


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
