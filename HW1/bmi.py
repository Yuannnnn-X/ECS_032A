# bmi.py
# Yuan Xie
#
# use a computer to calculate bmi value
Height = float(input("Enter height in inches:")) #prompt height
Weight = float(input("Enter weight in pounds:")) #prompt weight
bmi = (Weight/(Height**2))*703 #calculate bmi with the formula
print("BMI:",bmi)
