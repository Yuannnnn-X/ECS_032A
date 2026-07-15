# quiz_part5.py
# Yuan Xie
#
# the fifth part of a quiz


Score = 0
# print the three options of ART category
print("ART: Who painted 'The Persistance of Memory'?\
\na. Dali\
\nb. Munch\
\nc. Picasso")
# prompt your choice
Choice = input("Enter your choice:")
# your answer is a, which is correct
if Choice == "a":
    print("Correct!")
    Score = Score + 1
# your answer is not a
else:
    print("The correct answer was a")


# print the three options of ENTERTAINMET category
print("ENTERTAINMENT: How many oscars did Hitchcock win?\
\na. None\
\nb. One\
\nc. Two")
# prompt your choice
Choice = input("Enter your choice:")
# your answer is a, which is correct
if Choice == "a":
    print("Correct!")
    Score = Score + 1
# your answer is not a
else:
    print("The correct answer was a")


# print the three options of SCIENCE category
print("SCIENCE: Which dinosaur is most closely related to the pelican?\
\na. Velociraptor\
\nb. Stegosaurus\
\nc. Pterodactyl")
# prompt your choice
Choice = input("Enter your choice:")
# your answer is a, which is correct
if Choice == "a":
    print("Correct!")
    Score = Score + 1
# your answer is not a
else:
    print("The correct answer was a")


# print the three options of HISTORY category
print("HISTORY: Which of the following was not invented in Baja California?\
\na. Margaritas\
\nb. Chocolate\
\nc. Caesar Salad")
# prompt your choice
Choice = input("Enter your choice:")
# your answer is b, which is correct
if Choice == "b":
    print("Correct!")
    Score = Score + 1
# your answer is not b
else:
    print("The correct answer was b")


# print the three options of SCIENCE AND NATURE category
print("SCIENCE AND NATURE: Can pigs swim?\
\na. Yes\
\nb. No\
\nc. Only in salt water")
# prompt your choice
Choice = input("Enter your choice:")
# your answer is a, which is correct
if Choice == "a":
    print("Correct!")
    Score = Score + 1
# your answer is not a
else:
    print("The correct answer was a")


# print the three options of SPORT AND LEISURE category
print("SPORT AND LEISURE: What color is the middle Olympic ring?\
\na. Red\
\nb. Blue\
\nc. Black")
# prompt your choice
Choice = input("Enter your choice:")
# your answer is c, which is correct
if Choice == "c":
    print("Correct!")
    Score = Score + 1
# your answer is not c
else:
    print("The correct answer was c")


# add the new GENIUS question
print("GENIUS: In ancient Rome, what is L divided by X?")
# prompt your answer
Answer = input("Enter your answer:")
# your answer is 5 or V, which are correct
if Answer == "5" or Answer == "V":
    print("Correct!")
    Score = Score + 1
else:
    print("Correct answers were 5 or V")


# print the final score
print("Your final score is",Score)


# add a message
# if the total is from 0 through 2
if 0 <= Score <= 2:
    print("You were unlucky!")
# if the total is from 3 through 4
elif 3 <= Score <= 4:
    print("At least you did better than chance!")
# if the total is from 5 through 6
elif 5 <= Score <= 6:
    print("Excellent!")
# if the total is 7
elif Score == 7:
    print("Genius!")


    









