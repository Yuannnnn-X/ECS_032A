# car.py
# Yuan Xie
#
# guess the price of a car

# print the sentence
print("Guess the price and win the prize!")
guess = int(input("Enter your guess:"))
time = 0
# build the while loop
while True:
    if guess > 44500:
        print("Too high!")
        guess = int(input("Enter your guess:"))
        time = time + 1
    elif guess < 44500:
        print("Too low!")
        guess = int(input("Enter your guess:"))
        time = time + 1
    elif guess == 44500:
        time = time + 1
        break
print("It took",time,"guesses.")
if time <= 5:
    print("You won the car!")
else:
    print("Too many guesses!")
        
        
