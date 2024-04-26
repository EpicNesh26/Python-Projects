print("Idea: Ask the user bunch of questions and if they give the right answer we add 1 point to their score and at the end of the program we give total points")
print()

print("Welcome to my Anime Quiz")
print()

playing=input("Do you want to play ??")
if playing != "yes":
    quit()
print()

print("Okay lets Play ")
score=0
print()

answer=input("Which is the longest anime??")
if answer.lower() =="one piece":
    print("Correct")
    score +=1 
else:
    print("Incorrect")
print()

answer=input("What is the no 1 anime in 2023??")
if answer.lower() =="demon slayer":
    print("Correct")
    score += 1
else:
    print("Incorrect")
print()

answer=input("What is the name of volleyball anime??")
if answer.lower() =="haikyuu":
    print("Correct")
    score += 1
else:
    print("Incorrect")
print()

answer=input("What is the name of the football anime")
if answer.lower() =="blue lock":
    print("Correct")
    score += 1
else:
    print("Incorrect")
print()
print("You got " + str(score) + "Questions Correct")
print("You got " + str((score/4)*100) + "%")

print("Thank You for playing")
