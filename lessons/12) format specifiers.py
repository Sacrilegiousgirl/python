price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

print(f"Price 1 is ${price1:.2f}")
print(f"Price 2 is ${price2:10}") #have 10 spaces
print(f"Price 3 is ${price3:010}") #same as above but added 0s to the spaces

print(f"Price 1 is ${price1:<10}") #align to left
print(f"Price 2 is ${price2:>10}") #alight to right/default
print(f"Price 3 is ${price3:^10}") #center-aligned

print(f"Price 1 is ${price1:+,.2f}") # add + to positive numbers, add , to big numbers, round to 2 decimal places
print(f"Price 2 is ${price2:+,.2f}") 
print(f"Price 3 is ${price3:+,.2f}")