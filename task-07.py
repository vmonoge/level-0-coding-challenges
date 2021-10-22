def celsius_to_fahrenheit(celsius_temperature):
    fahrenheit_temperature = celsius_temperature * (9/5) + 32

    return print(f"{celsius_temperature} degrees Celsius: {fahrenheit_temperature} degrees Fahrenheit")

celsius_to_fahrenheit(23)


def fahrenheit_to_celcius(fahrenheit_temperature):
    celcius_temperature = (fahrenheit_temperature - 32) * (5/9)

    return print(f"{fahrenheit_temperature} degrees Fahrenheit: {celcius_temperature} degrees Celcius")

fahrenheit_to_celcius(23)
