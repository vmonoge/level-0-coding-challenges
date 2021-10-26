def maximum_number(*args):
    number_storage = args[0]
    
    for number in args:

        if number >= number_storage :
            number_storage = number
    return number_storage

print(maximum_number(-1, -2, -3))
print(maximum_number(3, 2, 1))
print(maximum_number(2, 1, 3))
print(maximum_number(3, 1, 2))
