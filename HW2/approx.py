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
elif ("{:.10f}".format(a)) == ("{:.10f}".format(b)):
    print("Those numbers are very nearly identical")
# be the same to 2-9 decimal places
elif ("{:.9f}".format(a)) == ("{:.9f}".format(b)):
    print("Those numbers are the same to 9 decimal places")
elif ("{:.8f}".format(a)) == ("{:.8f}".format(b)):
    print("Those numbers are the same to 8 decimal places")
elif ("{:.7f}".format(a)) == ("{:.7f}".format(b)):
    print("Those numbers are the same to 7 decimal places")
elif ("{:.6f}".format(a)) == ("{:.6f}".format(b)):
    print("Those numbers are the same to 6 decimal places")
elif ("{:.5f}".format(a)) == ("{:.5f}".format(b)):
    print("Those numbers are the same to 5 decimal places")
elif ("{:.4f}".format(a)) == ("{:.4f}".format(b)):
    print("Those numbers are the same to 4 decimal places")
elif ("{:.3f}".format(a)) == ("{:.3f}".format(b)):
    print("Those numbers are the same to 3 decimal places")
elif ("{:.2f}".format(a)) == ("{:.2f}".format(b)):
    print("Those numbers are the same to 2 decimal places")
# be the same to 1 or fewer decimal places
else:
    print("Those numbers are different")
