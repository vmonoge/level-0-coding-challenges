def vowels(input_string):
	vowels = ["a", "e", "i", "o", "u"]
	found_vowels = ""
	input_string = input_string.lower()

	for letter in input_string:
		if letter in vowels and letter not in found_vowels:
			found_vowels += f"{letter}, "

	return print(f"Vowels: {found_vowels[0:-2]}.")

vowels("Umuzi")
vowels("Victor")
