# phone.py
# Yuan Xie
#
# phone number validity check

# prompt the phine number
phone = input("Enter number as ### ###-####:")
# the length validity check
valid = len(phone) == 12
pos = 0
# build the while loop
while valid and pos < 12:
    if pos == 3:
        valid = phone[pos] == " "
    elif pos == 7:
        valid = phone[pos] == "-"
    else:
        valid = phone[pos].isdigit()
    pos = pos + 1
if valid:
    print("Valid")
else:
    print("Invalid")
