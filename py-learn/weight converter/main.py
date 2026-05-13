weight = float(input("Enter your weight: "))
unit = input("Is that in (K)g or (L)bs? ")
if unit == "K":
    converted = round(weight * 2.20462,2)
    print(f"You are {converted} pounds.")
elif unit == "L":
    converted = round(weight / 2.20462,2)
    print(f"You are {converted} kilograms.")
else:
    print("Invalid unit.")