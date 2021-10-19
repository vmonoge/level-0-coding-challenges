def common_letters(first_word, second_word):
	first_word = first_word.lower()
	second_word = second_word.lower()

	save_common_letters = "" 

	for letter in first_word:
		if letter in second_word and letter not in save_common_letters:
			save_common_letters += f"{letter}, "

	return print(f"Common letters: {save_common_letters[0:-2]}.")

common_letters("house", "computers")
