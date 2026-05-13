temp = 31
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is ongoing")

is_sunny = False

if temp >= 30 and is_sunny:
    print("It's a sunny day")
elif temp >= 30 and not is_sunny:
    print("It's a hot day but not sunny")
else:
    print("It's not a sunny day")
