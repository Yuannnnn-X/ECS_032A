# temp_list.py
# Yuan Xie
#
# make the temperature list

# prompt the name of the file
infile = input("Temperature anomaly filename:")
# open the file
infile = open(infile,"r")
# ignore the header
line = infile.readline()
# an empty list
temp = []
for line in infile:
    # strip whitespace off ends
    line = line.strip()
    line = line.rstrip("0")
    # extract into variables
    Year, Value = line.split(",")
    Value = float(Value)
    # append the values
    temp.append(Value)
# print the list
print(temp)
infile.close()
    
