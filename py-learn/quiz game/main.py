questions = (
    "What is the capital of France? ",
    "What is the largest planet in our solar system? ",
    "What is the chemical symbol for gold? ",
    "How many continents are there on Earth? ",
    "What is the longest river in the world? ",
)

options = (("a) London", "b) Berlin", "c) Paris", "d) Madrid"), 
           ("a) Jupiter", "b) Saturn", "c) Mars", "d) Venus"), 
           ("a) Ag", "b) Au", "c) Al", "d) As"), 
           ("a) 5", "b) 6", "c) 7", "d) 8"), 
           ("a) The Nile", "b) The Amazon", "c) The Yangtze", "d) The Mississippi"))

answers = ("c", "a", "b", "b", "a")

guesses = []

score = 0

question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (a, b, c, or d): ")
    guess = guess.lower()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("WRONG!")
    question_num += 1

print("-------------------------")
print("Quiz completed!")
print(f"Your score is: {score}/{len(questions)}")