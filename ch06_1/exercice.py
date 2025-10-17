#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        values = []
        while len(values) < 10:
            values.append(input('Veuillez saisir une valeur supplémentaires : '))
    values.sort()
    return values


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        words = []
        while len(words) < 2:
            words.append(input("Veuillez saisir un mot : "))

    # Retourner False si les mots n'ont pas la même longueur
    if len(words[0]) != len(words[1]):
        return False
    
    # Vérifier si les mots sont des anagrammes
    lettres_mot2 = list(words[1])
    for lettre in words[0]:
        if lettre not in lettres_mot2:
            return False
        lettres_mot2.remove(lettre)

    return True


def contains_doubles(items: list) -> bool:
    ensemble = set(items)
    return len(items) != len(ensemble)


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    # Calcul de la moyenne
    meilleure_note = (None, 0)
    for etudiant, notes in student_grades.items():
        moyenne = sum(notes) / len(notes)
        if moyenne > meilleure_note[1]:
            meilleure_note = (etudiant, moyenne)
    return {
        meilleure_note[0]: meilleure_note[1]
    }


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    caracteres_distincts = set(sentence)
    frequence_lettres = {}
    for caractere in caracteres_distincts:
        frequence_lettres[caractere] = sentence.count(caractere)

    #       Retourner le tableau de lettres
    frequence_triee = dict(sorted(frequence_lettres.items(), key=lambda item: item[1], reverse=True))
    for lettre, frequence in frequence_triee.items():
        if frequence >= 5:
            print(f"Le caractère {lettre} revient {frequence} fois.")

    return frequence_lettres


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    nom = input('Saisir le nom de votre recette : ')
    ingredients = []
    ingredient_supplementaire = True
    while ingredient_supplementaire:
        ingredients.append(input('Ingrédient : '))
        ingredient_supplementaire = True if input('Ingrédient supplémetaire ? (y/n)') == 'y' else False
    return {
        nom: ingredients
    }
        


def print_recipe(recettes) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    nom_recette = input('Quelle recette désirez-vous consulter ?')
    ingredients = recettes.get(nom_recette, None)
    if ingredients:
        print(nom_recette.upper())
        for ingredient in ingredients:
            print(ingredient)



def main() -> None:
    # print(f"On essaie d'ordonner les valeurs...")
    # order()

    # print(f"On vérifie les anagrammes...")
    # print(anagrams())

    # my_list = [3, 3, 5, 6, 1, 1]
    # print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    # grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    # best_student = best_grades(grades)
    # print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    # sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    # frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
