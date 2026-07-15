# circle.py
# Yuan Xie
#
# calculate the diameter, circumference and area of a circle
Radius = input("Enter radius:")
Radius = float(Radius) #change the radius into a floating point number
diameter = 2 * Radius
circumference = 3.14159 * diameter
area = 3.14159 * (Radius**2)
print("Diameter", diameter)
print("Circumference", circumference)
print("Area", area)
