# approx.py
# Yuan Xie
#
# judge whether the numbers are similar

# prompt numbers
a = float(input("Enter a number:"))
b = float(input("Enter a number:"))
# they are identical
if a == b:
    print("Those numbers are identical")
# be the same to more than 9 decimal places
elif round(a,10) == round(b,10):
    print("Those numbers are very nearly identical")
# be the same to 2-9 decimal places
elif round(a,9) == round(b,9):
    print("Those numbers are the same to 9 decimal places")
elif round(a,8) == round(b,8):
    print("Those numbers are the same to 8 decimal places")
elif round(a,7) == round(b,7):
    print("Those numbers are the same to 7 decimal places")
elif round(a,6) == round(b,6):
    print("Those numbers are the same to 6 decimal places")
elif round(a,5) == round(b,5):
    print("Those numbers are the same to 5 decimal places")
elif round(a,4) == round(b,4):
    print("Those numbers are the same to 4 decimal places")
elif round(a,3) == round(b,3):
    print("Those numbers are the same to 3 decimal places")
elif round(a,2) == round(b,2):
    print("Those numbers are the same to 2 decimal places")
# be the same to 1 or fewer decimal places
else:
    print("Those numbers are different")
