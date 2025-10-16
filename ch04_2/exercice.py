#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def get_first_part_of_name(name):
	index = name.find('-')
	return name[:index].title()

def get_random_sentence(animals, adjectives, fruits):
	chance = random.randint(0, 2)
	animal = animals[chance]
	chance = random.randint(0, 2)
	adjectif = adjectives[chance]
	chance = random.randint(0, 2)
	fruit = fruits[chance]
	return f'Dans un univers parallèles, un {animal} est {adjectif} et chasse les {fruit}'

def format_date(year, month, day, hours, minutes, seconds):
	return f'{day:02}/{month:02}/{year:04} {hours:02}:{minutes:02}:{seconds:02.3f}'

def encrypt(text, shift):
	text = text.upper()
	resultat = ""
	for lettre in text:
		if lettre.isalpha():
			index = ord(lettre) - ord('A')
			encrypted_index = (index + shift) % 26
			resultat += chr(ord('A') + encrypted_index)
		else:
			resultat += lettre
	return resultat

def decrypt(encrypted_text, shift):
	return encrypt(encrypted_text, -shift)

# def decrypt(encrypted_text, shift):
# 	resultat = ''
# 	for lettre in encrypted_text:
# 		if lettre.isalpha():
# 			index = ord(lettre) - ord('A')
# 			decrypted_index = (index - shift) % 26
# 			resultat += chr(ord('A') + decrypted_index)
# 		else:
# 			resultat += lettre
# 	return resultat


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))

	print(format_date(1970, 1, 12, 12, 3, 45.6789))

	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
