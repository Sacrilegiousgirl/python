op = input("Enter operator: (+ - * /): ")
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if op == "+":
    print(round(a+b, 3))
elif op == "-":
    print(round(a-b, 3))
elif op == "*":
    print(round(a*b, 3))
elif op == "/":
    if (b == 0):
        print("You cant divide a number by 0")
    else:
        print(round(a/b, 3))
else:
    print(f"{op} is not a valid operator")