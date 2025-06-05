# A script that converts temperature from celsius to fahrenheit and vice versa

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32 ) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    temperature = float(input("Enter the temperature to convert: "))
    unit = str(input("Is this temperature in Celsius or Fahrenheit? (C/F):")).strip().lower()

    if unit == "c":
        new_temperature = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {new_temperature}°F")
    elif unit == "f":
        new_temperature = convert_to_celsius(temperature)
        print(f"{temperature}°F is {new_temperature}°C")
    else:
        print("Invalid unit")

main()