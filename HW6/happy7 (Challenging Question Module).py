# happy_stubs.py,happy7.py
# Yuan Xie
#
# Read the file, build the dictionary and query the dictionary


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
    read_gdp_data(happy_dict)


# Read the file and build the dictionary by using two for loops
happiness = {} # make the happiness dictionary
def make_happy_dict():
    infile = open("happiness.csv","r")
    infile.readline()
    for line in infile:        
        line = line.strip()
        val = line.split(",") # split the commas
        Country = val[0] # the first colon is country
        HappinessIndex = val[2] #the third colon is happiness index
        # print(Country,HappinessIndex) # print the two colons
        happiness[Country] = HappinessIndex # add keys and values to the dictionary
    return happiness  

def read_gdp_data(happy_dict):
    outfile = open("world_pop_gdp.tsv","r")
    outfile.readline()
    midfile = open("world_pop_gdp_happy.csv","w")
    midfile.write("Country,Population in Millions,GDP per Capita,Happiness\n")
    for line in outfile:
        line = line.strip()
        val2 = line.split("\t") # split the tabs
        country = val2[0] # the first colon is country
        PopulationInMillions = val2[1] # the second colon is the population
        PopulationInMillions = PopulationInMillions.replace(",","") 
        GDPperCapita = val2[2] # the third colon is the GDP per capita
        GDPperCapita = GDPperCapita.replace(",","") 
        GDPperCapita = GDPperCapita.strip("$") # omit the dollar sign
        if float(PopulationInMillions) >= 100: # if the population is greater or equal to 100 million
            if country not in happiness: # if the country is not in the csv file
                continue
            else:
                midfile.write(str(country)+","+str(PopulationInMillions)+","+str(GDPperCapita)+","+str(happiness[country])+"\n")
        else:
            continue
    midfile.close()

def lookup_happiness_by_country(happy_dict):
    while True:
        UserInput = input("Enter a country to lookup or 'done' to exit:")
        if UserInput == "done":
            break
        if UserInput in happiness:
            HappinessIndex = happiness[UserInput]
            print(HappinessIndex)
        else:
            print(UserInput,"not found")
            continue

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
