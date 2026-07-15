# divide.py
# Yuan Xie
#
# calculate the quotient and remainder
a = input("Enter a number:")
a = int(a) #change the number into an integer
b = input("Enter a number to divide that by:")
b = int(b) #change the number into an integer
c = a // b #floor division
d = a % b #remainder
print(a, "divided by", b, "is", c, "with", d, "remaining")
