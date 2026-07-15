# cat.py
# Yuan Xie
#
# UNIX cat

# prompt the filename
filename = input("Enter a file name to open:")
infile = open(filename,"r")
for line in infile:
    line = line.strip()
    print(line)
infile.close()
