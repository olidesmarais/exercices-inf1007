#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	nombre_lettres = 0
	for lettre in text:
		if lettre.isalnum():
			nombre_lettres += 1
	return nombre_lettres

def get_word_length_histogram(text):
	mots = text.split()

	max_lettre = 0
	# Identifier le mot le plus long
	for mot in mots:
		if get_num_letters(mot) > max_lettre:
			max_lettre = len(mot)

	# Créer le histogramme vide
	histogramme = []
	for idx in range( max_lettre):
		histogramme.append(0)

	# Compter le nombre de mot de chaque lettre
	for mot in mots:
		histogramme[ get_num_letters(mot) ] += 1

	return histogramme

def format_histogram(histogram):
	ROW_CHAR = "*"
	resultat = ''

	for idx, valeur in enumerate(histogram):
		if idx == 0:
			continue
		resultat += f"{idx: >2} {ROW_CHAR * valeur}\n"

	return resultat

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"

	resultat = ''

	# Ajouter l'axe
	for _ in enumerate(histogram):
		# if idx == 0:
		# 	continue
		resultat += LINE_CHAR

	for niveau in range(max(histogram)):
		ligne_courante = ''
		for idx, valeur in enumerate(histogram):
			if idx == 0:
				continue
			if valeur >= niveau + 1:
				ligne_courante += BLOCK_CHAR
			else:
				ligne_courante += ' '
		resultat = ligne_courante + '\n' + resultat

	return resultat


if __name__ == "__main__":
	word = "est?"
	print(f"The number of characters for '{word}' is: {get_num_letters(word)}")
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
