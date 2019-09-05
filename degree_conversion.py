# Prompt the user for a number in degrees Celsius, and convert the value to degrees in Fahrenheit and display it to the user.

celsius = int(input("Temperature in C?"))


def celsius_to_fahrenheit(celsius):

    fahrenheit = celsius * 1.8 + 32
    return str(fahrenheit) + " F"


fahrenheit_conversion = celsius_to_fahrenheit(celsius)
print(fahrenheit_conversion)
