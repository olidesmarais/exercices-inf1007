#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def format_bill_total(data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2

	sous_total = 0
	for item in data:
		sous_total += item[1] * item[2]
	taxe = sous_total * 0.15
	total = sous_total + taxe

	resultat = ''
	resultat += f"{'SOUS TOTAL':14} {sous_total:7.2f} $\n"
	resultat += f"{'TAXE':14} {taxe:7.2f} $\n"
	resultat += f"{'TOTAL':14} {total:7.2f} $\n"

	return resultat

def format_bill_items(data):
	resultat = ""

	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2

	longueur_max = 0
	for item in data:
		if longueur_max < len(item[0]):
			longueur_max = len(item[0])

	for item in data:
		resultat += f'{item[INDEX_NAME]:{longueur_max}}{item[1] * item[2]:10.2f} $\n'

	return resultat

def format_number(number, num_decimal_digits):
	negatif = number < 0
	positif = abs(number)

	entier = int(positif)
	entier_string = ''
	while entier > 1000:
		sous_entier = entier % 1000
		entier_string = f' {sous_entier:03}{entier_string}'
		entier //= 1000
	entier_string = f'{entier}{entier_string}'

	decimal = round(positif % 1, 2)
	decimal *= 10**num_decimal_digits
	decimal = int(decimal)

	return f"{'-' if negatif else ''}{entier_string}.{decimal:0{num_decimal_digits}}"

def get_triangle(num_rows):
	largeur_triangle = 1 + 2 * (num_rows - 1)
	resultat = ''
	resultat += f"{'+'* (largeur_triangle + 2)}\n"
	for idx in range(0, num_rows):
		resultat += f"+{'A' * (idx * 2 + 1): ^{largeur_triangle}}+\n"
	resultat += f"{'+'* (num_rows * 2 + 1)}\n"
	return resultat


if __name__ == "__main__":
	purchases = [
		("chaise ergonomique", 1, 399.99),
		("g-fuel", 69, 35.99),
		("blue screen", 2, 39.99)
	]
	print(format_bill_items(purchases).strip())
	print("- - - - - - - - - - - - - - - - - - -")
	print(format_bill_total(purchases).strip())

	print("\n------------------")

	print(format_number(-1420069.0678, 2))

	print("\n------------------")

	print(get_triangle(2))
	print(get_triangle(5))
