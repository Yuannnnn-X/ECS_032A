# digits.py
# Yuan Xie
#
# phone number with only the digits

# prompt the phone number
number = input("Enter phone number:")
# replace the signs
number = number.replace(' ','')
number = number.replace('(','')
number = number.replace(')','')
number = number.replace('-','')
print("Digit string:",number)
