# converter.py
# Yuan Xie
#
# calculate the decimal and binary representations of that character
Character = input("Enter a character:") #prompt a character
Character = str(Character)
Number = ord(Character) #get the order of the character
Binary = bin(Number) #change it into a binary number
print(Character, "corresponds to the integer", Number, "which is", Binary, "in binary.")
