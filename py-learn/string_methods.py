# day = input("Enter what day it is: ")
phone_number = input("Enter your phone number: ")

# result = len(day)
# result = day.find("T") -- first occurrence
# result = day.rfind("T")  # last occurrence
# day = day.capitalize()
# day = day.upper()
# day = day.lower()
# result = day.isdigit()
# result = day.isalpha()
# result = phone_number.count("-")
result = phone_number.replace("-", " ")

print(result)
# print(day)
