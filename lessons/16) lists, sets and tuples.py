# []: list, {}: set, (): tuple
# List: ordered and changeable. Duplicates OK
# Set: unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = ordered and unchangeable. Duplicates OK. FASTER


# LIST EXAMPLE
fruits = ["apple", "orange", "banana", "coconut"]

print(dir(fruits))
print(help(fruits))
print(len(fruits))
print(fruits[::-1])
print("apple" in fruits)
print("pineapple" in fruits)
fruits[0] = "pineapple"
fruits.append("pineapple")
fruits.remove("orange")
fruits.insert(2, "mango")
fruits.sort()       #sort in alphabetical order
fruits.reverse()    #reverse original list, NOT in alphabetical order
print(fruits.index("coconut"))
print(fruits.count("banana"))

for fruit in fruits:
    print(fruit)

fruits.clear()



# SET EXAMPLE
fruits = {"apple", "orange", "banana", "coconut"}
print(fruits) #print in random order each time
print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("pineapple" in fruits)
fruits.add("pineapple")
fruits.remove("apple")
fruits.pop()

fruits.clear()


#TUPLE EXAMPLE
fruits = ("apple", "orange", "banana", "coconut")
print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("pineapple" in fruits)
print(fruits.index("apple"))
print(fruits.count("coconut"))

for fruit in fruits:
    print(fruit)

