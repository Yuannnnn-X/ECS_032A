# cash2.py
# Yuan Xie
#
# count the items and calculate the total price

print("Automated cash register")
# promopt the filename
filename = input("Enter file of prices:")
# the initial count and sum should be zero
Count = 0
Sum = 0
#open the file
infile = open(filename)
for line in infile:
    try:
        line = line.strip("$")
        num = float(line)
        Count = Count + 1
        Sum = Sum + num
    except:
        continue
print("File contained",Count,"items totaling $"+str("{:.2f}".format(Sum)))
