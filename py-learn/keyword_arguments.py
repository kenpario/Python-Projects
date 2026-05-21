def hello(greeting, title, first_name, last_name):
    print(f"{greeting}, {title} {first_name} {last_name}")


hello(last_name="Smith", greeting="Hello", title="Mr.", first_name="John")

for x in range(1, 11):
    print(x,end=" ")
print()

def get_phone_number(country,area,first,last):
    return f"+{country} ({area}) {first}-{last}"

phone_num = get_phone_number(area="123", country="1", first="456", last="7890")
print(phone_num)
