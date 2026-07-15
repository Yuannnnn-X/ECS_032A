# paint.py
# Yuan Xie
#
# use a computer to calculate the number of cans of paint required
print("Paint coverage estimator")
length = input("Length of room in inches:")
width = input("Width of room in inches:")
Height = input("Average height of room in inches:")
#prompt length, width and height
length = float(length)/12
width = float(width)/12
Height = float(Height)/12
Area = 2*length*Height + 2*width*Height
#change them into floating point numbers
number = Area/100
number = int(number) + 1
#calculate the number of cans will be needed
print("You'll want", number, "cans.")
