name = input("Enter your fulll name: ")
phone_number = input("Enter your phone #: ")

result = len(name)
result = name.find("n") #first occurence
result = name.rfind("n") #last occurence
result = name.capitalize()
result = name.upper()
result = name.lower()
result = name.isdigit()
result = name.isalpha()
result = phone_number.count("-")
result = phone_number.replace("-", "")

print(result)

# make a username that cannot exceed 12 characters, cant contain spaces or numbers
username = input("Enter your username: ")

if len(username) > 12:
    print("Your username cant exceed 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")