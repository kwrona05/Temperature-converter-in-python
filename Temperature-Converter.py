def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def celsius_to_kelvin(celsius):
    return celsius + 273.15
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def temperature_converter():
    print('Choose an option: ')
    print('1. Celsius -> Fahrenheit')
    print('2. Fahrenheit -> Celsius')
    print('3. Celsius -> Kelvin')
    print('4. Kelvin -> Celsius')

    choice = int(input('Enter option number: (1/2/3/4): '))
    temperature = float(input('Enter temperature: '))

    if choice == 1:
        result = celsius_to_fahrenheit(temperature)
        print(f'{temperature}°C is {result}°F')
    elif choice == 2:
        result = fahrenheit_to_celsius(temperature)
        print(f'{temperature}°F is {result}°C')
    elif choice == 3:
        result = celsius_to_kelvin(temperature)
        print(f'{temperature}°C is {result}K')
    elif choice == 4:
        result = kelvin_to_celsius(temperature)
        print(f'{temperature}K is {result}°C')
    else:
        print('Incorrect option number')

temperature_converter()