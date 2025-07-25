capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

print(capitals.get("USA"))

if capitals.get("Japan"):
    print("That capital exitsts")
else:
    print("That capital doesnt exist")

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroi"})
capitals.pop("China")
capitals.popitem()

keys = capitals.keys()

for key in capitals.keys():
    print(key)

values = capitals.values()

for value in capitals.values():
    print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")

capitals.clear()