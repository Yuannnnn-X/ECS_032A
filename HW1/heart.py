# heart.py
# Yuan Xie
#
# use a computer to calculate maximum and target heart rate
Age = input("Enter your age:") #prompt age
Age = int(Age) #change the age into an integer
Maximum = 220 - Age
print("Your maximum heart rate is", Maximum, "bpm")
lower = Maximum * 0.5 #lower bound is 50% of Maximum
upper = Maximum * 0.85 #upper bound is 85% of Maximum
print("Your target heart rate is", lower,"-", upper, "bpm")
