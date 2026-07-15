# quiz_part3.py
# Yuan Xie
#
# the third part of a quiz


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


# print the total score
print("Your total score is",Score)









