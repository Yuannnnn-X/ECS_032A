# temp_file_stats.py
# Yuan Xie
#
# find the maximum and minimum temperatures

# prompt the name of the file
infile = input("Temperature anomaly filename:")
# open the file
infile = open(infile,"r")
# maximum and minimum temperatures are temporarily none
min_Value = None
min_Year = None
max_Value = None
max_Year = None
# ignore the header
line = infile.readline()
for line in infile:
    # strip whitespace off ends
    line = line.strip()
    line = line.rstrip("0")
    # extract into variables
    Year, Value = line.split(",")
    Value = float(Value)
    # update the minimum temperature
    if min_Value == None or Value < min_Value:
        min_Value = Value
        min_Year = Year
    # update the maximum temperature
    if max_Value == None or Value > max_Value:
        max_Value = Value
        max_Year = Year
# output the results
print("Min temp:",min_Value,"in",min_Year)
print("Max temp:",max_Value,"in",max_Year)
