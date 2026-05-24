# # word = "World of Python"

# # letter = input("Guess a letter in the word: ")

# # # if letter in word:
# # #     print("Congratulations! You guessed a letter in the word.")
# # # else:
# # #     print("Sorry, that letter is not in the word.")

# # if letter not in word:
# #     print("Try again! That letter is not in the word.")
# # else:
# #     print("Great job! You guessed a letter in the word.")

# students = {"Alice", "Patrick", "John", "Emily"}

# student = input("Enter a student's name: ")

# if student in students:
#     print(f"{student} is in the class.")
# else:
#     print(f"{student} is not in the class.")

# grades = {"Alice": 85, "Bob": 92, "Charlie": 78}

# student = input("Enter a student's name: ")

# if student in grades:
#     print(f"{student}'s grade is {grades[student]}.")
# else:
#     print(f"{student} is not in the class.")

email = input("Enter your email address: ")

if "@" in email and "." in email:
    print("Valid email address.")
else:
    print("Invalid email address.")