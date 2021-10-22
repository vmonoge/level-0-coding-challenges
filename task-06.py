def maximum_number(*args):
    number_storage = 0
    
    for number in args:
        if number >= number_storage:
            number_storage = number
    return print(number_storage)

maximum_number(1, 2, 3)
maximum_number(3, 2, 1)
maximum_number(2, 1, 3)
maximum_number(3, 1, 2)
