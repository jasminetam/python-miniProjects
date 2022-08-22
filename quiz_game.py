print("Welcome to the quiz game")

playing =input("Type start to start a game: ")

if playing.lower() != "start":
    quit()

print("Okay! Let's start playing")
score = 0

answer = input("What is SSR stand for? ")
if answer.lower() == "server side rendering":
    print('Well done!')
    score += 1
else: print("Incorrect.")

answer = input("What is JWT stand for? ")
if answer.lower() == "json web token":
    print('Well done!')
    score += 1
else: print("Incorrect.")

answer = input("What is API stand for? ")
if answer.lower() == "application programming interface":
    print('Well done!')
    score += 1
else: print("Incorrect.")

answer = input("What is HTTP stand for? ")
if answer.lower() == "hypertext transfer protocol":
    print('Well done!')
    score += 1
else: print("Incorrect.")

print("You got " + str(score) + " questions correct.")
print("You got " + str((score/4) * 100) + "%.")