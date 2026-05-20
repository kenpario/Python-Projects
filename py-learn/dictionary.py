capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "USA": "Washington D.C.",
    "China": "Beijing",
}

print(capitals.get("France"))

capitals.update({"Spain": "Madrid"})
capitals.pop("Italy")
keys = capitals.keys()
print(capitals)
print(keys)

for key in capitals.keys():
    print(key)

values = capitals.values()
for value in capitals.values():
    print(value)

for key, value in capitals.items():
    print(f"{key}: {value}")
