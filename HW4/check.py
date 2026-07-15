# check.py
# Yuan Xie
#
# check the card number

# prompt the card number
card = input("Enter your 8-digit card number:")
even = int(card[1]) + int(card[3]) + int(card[6]) + int(card[8])
a1 = 2*int(card[7])//10
a2 = 2*int(card[7])%10
b1 = 2*int(card[5])//10
b2 = 2*int(card[5])%10
c1 = 2*int(card[2])//10
c2 = 2*int(card[2])%10
d1 = 2*int(card[0])//10
d2 = 2*int(card[0])%10
odd = a1+a2+b1+b2+c1+c2+d1+d2
# calculate the sum of different parts
total = even + odd
total = str(total)
if total[-1] == "0":
    print("Valid")
else:
    print("Invalid")
    even = (int(total)//10)*10-odd-(int(card[1]) + int(card[3]) + int(card[6]))
    if even > 0:
        print("Check digit should be",even)
    else:
        even = ((int(total)+10)//10)*10-odd-(int(card[1]) + int(card[3]) + int(card[6]))
        print("Check digit should be",even)
