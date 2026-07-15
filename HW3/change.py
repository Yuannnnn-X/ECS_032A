# change.py
# Yuan Xie
#
# calculate the numbers of quarters, dimes, nickels and pennies

# prompt the number of cents
Cents = int(input("Enter cents:"))
# calculate the number of quarters and its remaining
quarters = Cents // 25
quarters_remained = Cents % 25
# calculate the number of dimes and its remaining
dimes = quarters_remained // 10
dimes_remained = quarters_remained % 10
# calculate the number of nickels and its remaining
nickels = dimes_remained // 5
nickels_remained = dimes_remained % 5
# calculate the number of pennies
pennies = nickels_remained
# print
print("The minimum coins for",Cents,"cents are:")
print(quarters,"Quarters")
print(dimes,"Dimes")
print(nickels,"Nickels")
print(pennies,"Pennies")
