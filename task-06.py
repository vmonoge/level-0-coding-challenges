def maximum_number(first_number, second_number, third_number):
    if first_number >= second_number and first_number >= third_number :
        return print(first_number)
    elif second_number >= first_number and second_number >= third_number:
        return print(second_number)
    else:
        return print(third_number)

maximum_number(1, 2, 3)
maximum_number(3, 2, 1)
maximum_number(2, 1, 3)
maximum_number(3, 1, 2)
