def vowels_in_a_word(given_word):
    vowel_list = ["a", "e", "i", "o", "u"]
    given_word = given_word.lower()
    found_vowels = ""

    for letter in given_word:
        if letter in vowel_list and letter not in found_vowels:
            found_vowels += f"{letter}, "

	return print(f"Vowels: {found_vowels[:-2]}.")

vowels_in_a_word("Umuzi")
vowels_in_a_word("Victor")
