# trycat.py
# Yuan Xie
#
# UNIX trycat

while True:
    # prompt the filename
    filename = input("Enter a file name to open:")
    #build the try-except block
    try:
        infile = open(filename,"r")
        for line in infile:
            line = line.strip()
            print(line)
        infile.close()
    except:
        print("Could not open","'"+str(filename)+"'")
        continue
    break
