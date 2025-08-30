def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15


print("Temperature Converter")
print("1. Celsius to Kelvin")
print("2. Kelvin to Celsius")
print("3. Celsius to Fahrenheit")
print("4. Fahrenheit to Celsius")
print("5. Kelvin to Fahrenheit")
print("6. Fahrenheit to Kelvin")

choice = int(input("Enter your choice (1-6): "))
temp = float(input("Enter the temperature to convert: "))

if choice == 1:
    print("Result:", celsius_to_kelvin(temp), "K")
elif choice == 2:
    print("Result:", kelvin_to_celsius(temp), "°C")
elif choice == 3:
    print("Result:", celsius_to_fahrenheit(temp), "°F")
elif choice == 4:
    print("Result:", fahrenheit_to_celsius(temp), "°C")
elif choice == 5:
    print("Result:", kelvin_to_fahrenheit(temp), "°F")
elif choice == 6:
    print("Result:", fahrenheit_to_kelvin(temp), "K")
else:
    print("Invalid choice.")
