
value = float(input("Enter the distance: "))
from_unit = input("Convert from (mile, feet, inch, meter, km): ").lower()
to_unit = input("Convert to (mile, feet, inch, meter, km): ").lower()


if from_unit == "mile":
    value_in_meters = value * 1609.344
elif from_unit == "feet":
    value_in_meters = value * 0.3048
elif from_unit == "inch":
    value_in_meters = value * 0.0254
elif from_unit == "meter":
    value_in_meters = value * 1
elif from_unit == "km":
    value_in_meters = value * 1000
else:
    print("Invalid from-unit!")
    exit()


if to_unit == "mile":
    result = value_in_meters / 1609.344
elif to_unit == "feet":
    result = value_in_meters / 0.3048
elif to_unit == "inch":
    result = value_in_meters / 0.0254
elif to_unit == "meter":
    result = value_in_meters / 1
elif to_unit == "km":
    result = value_in_meters / 1000
else:
    print("Invalid to-unit!")
    exit()


print(f"{value} {from_unit} is equal to {result} {to_unit}")
