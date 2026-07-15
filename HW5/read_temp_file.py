# read_temp_file.py
# Yuan Xie
#
# read the temperatures from the files

# prompt the name of the file
infile = input("Temperature anomaly filename:")
# open the file
infile = open(infile,"r")
# ignore the header
line = infile.readline()
for line in infile:
    # strip whitespace off ends
    line = line.strip()
    line = line.rstrip("0")
    # extract into variables
    Year, Value = line.split(",")
    Value = float(Value)
    print(Year,Value)
infile.close()
