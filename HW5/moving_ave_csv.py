# moving_ave_csv.py
# Yuan Xie
#
# calculate the average temperature in an interval and write a csv

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
    Year = int(Year)
    # append the values
    temp.append(Value)
infile.close()
outfile = open("MovingAve.csv","w")
outfile.write("Year,Value\n")
# prompt the index
k = int(input("Enter window size:"))
for index in range(k,len(temp)-k):
    Year = 1880 + index
    ave = sum(temp[index-k:index+k+1]) / (2*k+1)
    outfile.write(str(Year)+","+"{:.4f}".format(ave)+"\n")
outfile.close()

    
