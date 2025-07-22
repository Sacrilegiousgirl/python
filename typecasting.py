name = "Annie"
age = 18
is_student = True

print(type(is_student))
print(float(age))

name1 = input("Babe whats your name?: ")
if bool(name1) == True:
    print("Hello", name1)
else:
    print("You forgot to type your name!")