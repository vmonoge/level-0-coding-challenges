def maximum_number(first_number, second_number, third_number, fourth_number):
	if first_number >= second_number and first_number >= third_number and first_number >= fourth_number:
		return print(first_number)
	elif second_number >= first_number and second_number >= third_number and second_number >= fourth_number:
		return print(second_number)
	elif third_number >= first_number and third_number >= second_number and third_number >= fourth_number:
		return print(third_number)
	else:
		return print(fourth_number)

maximum_number(1, 2, 3, 4)
maximum_number(4, 3, 2, 1)
maximum_number(2, 4, 1, 3)
maximum_number(3, 1, 4, 2)

