num = 5
a = 6
b = 7
age = 25
temperature = 30
user_role = "admin"

print("Positive" if num > 0 else "Negative")
result = "EVEN" if num % 2 == 0 else "ODD"
max_num = a if a > b else b
min_num = a if a < b else b
status = "Adult" if age >= 18 else "Minor"
weather = "HOT" if temperature > 20 else "COLD"
access_level = "Full Access" if user_role == "admin" else "Limited Access"


print(result)
print(max_num)
print(min_num)
print(status)
print(weather)
print(access_level)