weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounts? (K or L): ")

if unit.upper() == "K":
    weight *= 2.205
    unit = "Lbs."
    print(f"Your weight is {round(weight, 1)} {unit}")
elif unit.upper() == "L":
    weight /= 2.205
    unit = "Kgs."
    print(f"Your weight is {round(weight, 1)} {unit}")
else:
    print(f"{unit} was not valid")



