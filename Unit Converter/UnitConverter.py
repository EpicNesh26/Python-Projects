def length_converter(value, from_unit, to_unit):
    conversion_factors = {
        "meters": 1,
        "kilometers": 0.001,
        "centimeters": 100,
        "millimeters": 1000,
        "miles": 0.00062,
        "yards": 1.09361,
        "feet": 3.28084,
        "inches": 39.3701,
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]


def weight_converter(value, from_unit, to_unit):
    conversion_factors = {
        "gram": 1,
        "kilogram": 0.001,
        "miligram": 1000,
        "pound": 0.0022,
        "ounces": 0.0352
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]


def temperature_converter(value, from_unit, to_unit):
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return value * 9/5 + 32
        elif to_unit == 'kelvin':
            return value + 273.15
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return value - 32 * 5/9
        elif to_unit == 'kelvin':
            return value - 32 * 5/9 + 273.15
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return value - 273.15 * 1.8 + 32
    return value


def main():
    while True:
        print("Unit Converter")
        print('1. Length')
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")
        choice = input("Choose the type of conversion you want to perform: ")

        if choice == '1':
            value = float(input("Enter the value to convert: "))
            from_unit = input(
                "Enter the from unit(meters, kilometers, centimeters, millimeters, miles, yards, feet, inches): ")
            to_unit = input(
                "Enter your to unit(meters, kilometers, centimeters, millimeters, miles, yards, feet, inches): ")
            converted_value = length_converter(value, from_unit, to_unit)
            print(f"{value} {from_unit} is equal to {converted_value} {to_unit}")
        elif choice == '2':
            value = float(input("Enter the value to convert: "))
            from_unit = input(
                "Enter the from unit(gram, kilogram, miligram, pound, ounces): ")
            to_unit = input(
                "Enter the to unit(gram, kilogram, milligram, pound, ounces): ")
            converted_value = weight_converter(value, from_unit, to_unit)
            print(f"{value} {from_unit} is equal to {converted_value} {to_unit}")
        elif choice == '3':
            value = float(input("Enter the value to convert: "))
            from_unit = input(
                'Enter the from unit(celsius, fahrenheit, kelvin): ')
            to_unit = input("Enter your to unit(celsius, fahrenheit, kelvin): ")
            converted_value = temperature_converter(value, from_unit, to_unit)
            print(f"{value} {from_unit} is equal to {converted_value} {to_unit}")
        elif choice == '4':
            print("Exiting Unit Converter")
            break

        else:
            print("Invalid choice. Please select a valid option")


main()
