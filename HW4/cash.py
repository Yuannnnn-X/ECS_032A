# cash.py
# Yuan Xie
#
# count the items and calculate the total price

print("Automated cash register")
# prompt the filename
filename = input("Enter file of prices:")
# the initial count and sum should be zero
Count = 0
Sum = 0
infile = open(filename)
for line in infile:
    line = line.strip()
    num = float(line)
    Count = Count + 1
    Sum = Sum + num
print("File contained",Count,"items totaling","${:.2f}".format(Sum))
