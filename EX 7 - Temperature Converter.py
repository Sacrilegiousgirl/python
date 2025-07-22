unit = input("Is this temperature in Celcius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit.upper() == "C":
    temp = temp * 1.8 + 32
    unit = "F"
    print(f"The temperature in Fahrenheit is {round(temp, 1)}°{unit}")
elif unit.upper() == "F":
    temp = (temp - 32) / 1.8
    unit = "C"
    print(f"The temperature in Celcius is {round(temp, 1)}°{unit}")
else:
    print(f"{unit} is not a valid temperature scale")