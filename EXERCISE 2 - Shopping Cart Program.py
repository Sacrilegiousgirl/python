item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is ${total}")

price1 = int(input("Enter price: "))
txt = f"It is very {'Expensive' if price1>50 else 'Cheap'}"

print(txt)