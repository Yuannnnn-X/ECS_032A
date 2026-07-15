# pocket.py
# Yuan Xie
#
# calculate the total number of dollars

print("Compute your pocket change!")
# prompt the numbers of quarters, dimes, nickels and pennies
quarters = int(input("Quarters?"))
dimes = int(input("Dimes?"))
nickels = int(input("Nickels?"))
pennies = int(input("Pennies?"))
# calculate the money in dollars
dollars = 0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies
# print the total
print("The total is","${:.2f}".format(dollars))
               

