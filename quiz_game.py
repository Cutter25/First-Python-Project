print("Welcome to my Python coding quiz!")

start = input("Do you want to play? ")

if start.lower() != "yes":
    quit()

print("Awesome! Let's get started! :)")
score = 0

answer = input("What does JS stand for? ")
if answer.lower() == "javascript":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("What does SQL stand for? ")
if answer.lower() == "structured query language":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("What does HTML stand for? ")
if answer.lower() == "hypertext markup language":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("What is REACT? ")
if answer.lower() == "a javascript framework":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")  

answer = input("Who made REACT? ")
if answer.lower() == "facebook":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("What is Python? ")
if answer.lower() == "a programming language":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")  

answer = input("What does CSS stand for? ")
if answer.lower() == "cascading style sheets":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("What is NodeJS ? ")
if answer.lower() == "a javascript back-end runtime environment":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("In JavaScript, what does let declare? ")
if answer.lower() == "a variable that can be reassigned globally":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("In JavaScript, what does const declare? ")
if answer.lower() == "a variable that cannot be reassigned":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

print("You got " + str(score) + " questions correct.")
print("Your score is " + str((score / 10) * 100) + " %.")

if score > 6:
    print("Congratulations! You passed!")
else: 
    print("You failed! Try again!")




