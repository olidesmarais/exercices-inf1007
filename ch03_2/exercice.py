#!/usr/bin/env python

import math


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	puissance = voltage**2 / resistance
	return puissance

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	# v1[0] et v2[0] pour accéder au X
	# v1[1] et v2[1] pour accéder au Y
	produit = v1[0] * v2[0] + v1[1] * v2[1]
	return produit == 0

def point_in_circle(point, circle_center, circle_radius):
	# TODO: Retourner vrai si le point est à l'intérieur du cercle, faux sinon.
	# point[0] et circle_center[0] pour accéder au X
	# point[1] et circle_center[1] pour accéder au Y
	distance = math.sqrt((circle_center[0] - point[0])**2 + (circle_center[1] - point[1])**2)
	return distance <= circle_radius

def cash(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$, 25¢, 10¢ et 5¢ à remettre pour représenter la valeur. Il faut arrondir à la pièce de 5¢ près. Il faut remplir les variables twenties, tens, fives, ones, quarters, dimes et nickels avec le quantité de chaque dénomination.
	twenties = value // 20
	value -= twenties * 20
	tens = value // 10
	value -= tens * 10
	fives = value // 5
	value -= fives * 5
	ones = value // 1
	value -= ones * 1
	quarters = value // 0.25
	value -= quarters * 0.25
	dimes = value // 10
	value -= dimes * 0.10
	nickels = value // 0.05
	value -= nickels * 0.05
	print(value)
	return twenties, tens, fives, ones, quarters, dimes, nickels

def format_base(value, base, digit_letters):
	# Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres.
	# `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
	result = ""
	abs_value = abs(value)
	while abs_value != 0:
		digit_value = abs_value % base
		result += digit_letters[digit_value]
		abs_value //= base
	if value < 0:
		# TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
		result = '-' + result
	return result


if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(point_in_circle([-1, 1], [1, -1], 2))
	print(cash(137.38))
	print(format_base(-420, 16, "0123456789ABCDEF"))
