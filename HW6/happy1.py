# happy_stubs.py,happy1.py
# Yuan Xie
#
# Read the file and build the dictionary


def main():

    # Part 1
    # Build dictionary mapping countries to happiness index
    happy_dict = make_happy_dict()

    # Part 2
    # Print key value pairs sorted by key
    # Uncomment the function call below for part 2 only
    # print_sorted_dictionary(happy_dict)

    # Part 3
    # Uncomment the function call below for part 3 only
    # lookup happiness by country until the user enters done
    # lookup_happiness_by_country(happy_dict)

    # Parts 4-6
    # Uncomment the function call below for parts 4-6 
    # Read file containing population and GDP data and add happiness data
    #read_gdp_data(happy_dict)


# Read the file and build the dictionary by using two for loops
def make_happy_dict(): # the function is used to read the file and return the happiness index
    infile = open("happiness.csv","r") #open the file
    infile.readline() # read the first line
    for line in infile: # read every line in the file except the first line
        line = line.strip()
        val = line.split(",") # split the colons
        Country =  val[0] # the first colon is country
        HappinessIndex = val[2] # the third colon is happiness index
        print(Country,HappinessIndex) # print the two colons
        happiness = {} # make the dictionary
        happiness[Country] = HappinessIndex
    return happiness
    infile.close()

def read_gdp_data(happy_dict):
    return

def lookup_happiness_by_country(happy_dict):
    return

# Function prints all the values in a dictionary d sorted by key
def print_sorted_dictionary(D):
    if type(D) != type({}):
        print("Dictionary not found")
        return
    print("Contents of dictionary sorted by key.")
    print("Key","Value")
    for key in sorted(D.keys()):
        print(key, D[key])
        
main()
