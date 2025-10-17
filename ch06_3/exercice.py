#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import copy
import itertools


def get_maximums(numbers):
	resultat = []
	for liste in numbers:
		resultat.append(max(liste))
	return resultat

def join_integers(numbers):
	return int(''.join([str(number) for number in numbers]))

def generate_prime_numbers(limit):
	# FONCTION Eratosthène(limite)
    # premiers = []
	premiers = []
    # nombres = liste des entiers de 2 à limite
	nombres = [nombre for nombre in range( 2, limit + 1)]
    # TANT QUE nombres est non vide FAIRE
	while len(nombres) > 0:
    #     Ajouter à premiers le premier entier de nombres
		premier = nombres.pop(0)
		premiers.append(premier)
    #     nombres = liste des entiers de nombres non multiples du premier
		nombres = [nombre for nombre in nombres if nombre % premier != 0]
    # RÉSULTAT premiers
	return premiers

def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
	resultat = []
	for idx in range( 1, num_combinations + 1):
		if excluded_multiples and idx % excluded_multiples == 0:
			continue
		for lettre in strings:
			resultat.append(f'{lettre}{idx}')
	return resultat


if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))
