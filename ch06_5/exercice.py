#!/usr/bin/env python
# -*- coding: utf-8 -*-

def check_brackets(text, brackets):
	print(text)
	structure = []
	for caractere in text:
		if caractere in brackets:
			if brackets.index(caractere) % 2 == 0:
				structure.append(caractere)
			else:
				ouverture = structure.pop()
				if brackets.index(caractere) != brackets.index(ouverture) + 1:
					return False
	if len(structure) > 0:
		return False
	return True

def remove_comments(full_text, comment_start, comment_end):
	index_start = full_text.find(comment_start)
	index_end = full_text.find(comment_end)
	if index_start < 0 or index_end < 0 or index_end < index_start:
		return None
	return full_text[:index_start] + full_text[index_end + len(comment_end):]

def get_tag_prefix(text, opening_tags, closing_tags):
	for otag, ctag in zip(opening_tags, closing_tags):
		if text.startswith(otag):
			return (otag, None)
		if text.startswith(ctag):
			return (None, ctag)
	return (None, None)

def check_tags(full_text, tag_names, comment_tags):
	text_sans_commentaire = full_text
	while text_sans_commentaire is not None and (comment_tags[0] in text_sans_commentaire or comment_tags[1] in text_sans_commentaire):
		text_sans_commentaire = remove_comments(text_sans_commentaire, comment_tags[0], comment_tags[1])
	if text_sans_commentaire == None:
		return False

	# Balises ouvrantes vers fermantes
	balises_ouvrantes = {f'<{tag_name}>':f'</{tag_name}>' for tag_name in tag_names}
	# Balises fermantes vers ouvrantes
	balises_fermantes = dict((v, k) for k, v in balises_ouvrantes.items())

	tag_stack = []
	texte = text_sans_commentaire
	while len(texte) > 0:
		ouvrant, fermant = get_tag_prefix(texte, balises_ouvrantes.keys(), balises_fermantes.keys())
		if ouvrant is not None:
			tag_stack.append(ouvrant)
			texte = texte[len(ouvrant):]
		elif fermant is not None:
			if len(tag_stack) == 0 or tag_stack[-1] != balises_fermantes[fermant]:
				return False
			tag_stack.pop()
			texte = texte[len(fermant):]
		else:
			# On avance jusqu'à la prochaine balise.
			texte = texte[1:]

	return len(tag_stack) == 0


if __name__ == "__main__":
	brackets = ("(", ")", "{", "}", "[", "]")
	yeet = "(yeet){yeet}"
	yeeet = "({yeet})"
	yeeeet = "({yeet)}"
	yeeeeet = "(yeet"
	print(check_brackets(yeet, brackets))
	print(check_brackets(yeeet, brackets))
	print(check_brackets(yeeeet, brackets))
	print(check_brackets(yeeeeet, brackets))
	print()

	spam = "Hello, world!"
	eggs = "Hello, /* OOGAH BOOGAH world!"
	parrot = "Hello, OOGAH BOOGAH*/ world!"
	dead_parrot = "Hello, /*oh brave new */world!"
	print(remove_comments(spam, "/*", "*/"))
	print(remove_comments(eggs, "/*", "*/"))
	print(remove_comments(parrot, "/*", "*/"))
	print(remove_comments(dead_parrot, "/*", "*/"))
	print()

	otags = ("<head>", "<body>", "<h1>")
	ctags = ("</head>", "</body>", "</h1>")
	print(get_tag_prefix("<body><h1>Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("<h1>Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("</h1></body>", otags, ctags))
	print(get_tag_prefix("</body>", otags, ctags))
	print()

	spam = (
		"<html>"
		"  <head>"
		"    <title>"
		"      <!-- Ici j'ai écrit qqch -->"
		"      Example"
		"    </title>"
		"  </head>"
		"  <body>"
		"    <h1>Hello, world</h1>"
		"    <!-- Les tags vides sont ignorés -->"
		"    <br>"
		"    <h1/>"
		"  </body>"
		"</html>"
	)
	eggs = (
		"<html>"
		"  <head>"
		"    <title>"
		"      <!-- Ici j'ai écrit qqch -->"
		"      Example"
		"    <!-- Il manque un end tag"
		"    </title>-->"
		"  </head>"
		"</html>"
	)
	parrot = (
		"<html>"
		"  <head>"
		"    <title>"
		"      Commentaire mal formé -->"
		"      Example"
		"    </title>"
		"  </head>"
		"</html>"
	)
	tags = ("html", "head", "title", "body", "h1")
	comment_tags = ("<!--", "-->")
	print('premier', check_tags(spam, tags, comment_tags))
	print('deuxieme', check_tags(eggs, tags, comment_tags))
	print('troisieme', check_tags(parrot, tags, comment_tags))
	print()

