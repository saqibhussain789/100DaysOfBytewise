# Temperature Converter
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return fahrenheit_to_celsius(f) + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

temp = float(input("Enter the temperature: "))
unit = input("Enter the unit (Celsius, Fahrenheit, Kelvin): ")

if unit.lower() == 'celsius':
    print(f"{temp} degrees Celsius is equal to {celsius_to_fahrenheit(temp)} degrees Fahrenheit and {celsius_to_kelvin(temp)} degrees Kelvin.")
elif unit.lower() == 'fahrenheit':
    print(f"{temp} degrees Fahrenheit is equal to {fahrenheit_to_celsius(temp)} degrees Celsius and {fahrenheit_to_kelvin(temp)} degrees Kelvin.")
elif unit.lower() == 'kelvin':
    print(f"{temp} degrees Kelvin is equal to {kelvin_to_celsius(temp)} degrees Celsius and {kelvin_to_fahrenheit(temp)} degrees Fahrenheit.")
else:
    print("Invalid unit.")
