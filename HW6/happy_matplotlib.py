# happy_stubs.py,happy_matplotlib.py
# Yuan Xie
#
# Read the file, and plot a graph


import matplotlib.pyplot as plt

# Read the file and build the dictionary by using two for loops
happiness = {} # make the happiness dictionary
def make_happy_dict(): # the function is used to read the file and return the happiness index
    infile = open("happiness.csv","r") # open the file
    infile.readline() # read the first line
    for line in infile: # for every line in the file except the first line
        line = line.strip() # strip the space
        val = line.split(",") # split the commas
        Country = val[0] # the first colon is country
        HappinessIndex = val[2] #the third colon is happiness index
        # print(Country,HappinessIndex) # print the two colons
        happiness[Country] = HappinessIndex # add keys and values to the dictionary
    return happiness

def read_gdp_data(happy_dict): # the function is used to read the tsv file
    outfile = open("world_pop_gdp.tsv","r") # open the file 
    outfile.readline() # read the first line
    midfile = open("world_pop_gdp_happy.csv","w") # write the new file
    midfile.write("Country,Population in Millions,GDP per Capita,Happiness\n") # write
    for line in outfile: # write all the lines required 
        line = line.strip() # strip the space
        val2 = line.split("\t") # split the tabs
        country = val2[0] # the first colon is country
        PopulationInMillions = val2[1] # the second colon is the population
        PopulationInMillions = PopulationInMillions.replace(",","") # strip the commas
        GDPperCapita = val2[2] # the third colon is the GDP per capita
        GDPperCapita = GDPperCapita.replace(",","") # strip the commas
        GDPperCapita = GDPperCapita.strip("$") # omit the dollar sign
        if float(PopulationInMillions) >= 100: # if the population is greater or equal to 100 million
            if country not in happiness: # if the country is not in the csv file
                continue
            else: # if the country is in the csv file and >= 100 million
                midfile.write(str(country)+","+str(PopulationInMillions)+","+str(GDPperCapita)+","+str(happiness[country])+"\n")
        else:
            continue
    midfile.close()

# Function reads the happiness file 
def read_data_file():
    fname = "world_pop_gdp_happy.csv"
    infile = open(fname)

    pop_list = []
    happy_list = []
    gdp_list = []
    country_list = []

    infile.readline() # ignore column header
    
    # loop over the lines of the input file and 
    # extract the data into four lists
    for line in infile:
        line = line.strip()
        
        # The columns are Country\tGDP per Capita\tPopulation in Millions\tHappiness
        cols = line.split(",")
        
        country = cols[0]
        country_list.append(country)
        
        pop = float(cols[1])
        pop_list.append(pop)
        
        pc_gdp = float(cols[2])
        gdp_list.append(pc_gdp)
        
        happy = float(cols[3])
        happy_list.append(happy)
    
    return country_list,gdp_list,pop_list,happy_list
    
# Function creates a bubble plot of the data in the happiness file     
def plot_data(country_list,gdp_list,pop_list,happy_list):
    # New scatter plot
    # This sets the plot size
    plt.figure(figsize=(12,6))
    
    # The size of the points will bet determined by population
    plt.scatter(gdp_list,happy_list,s=pop_list,alpha=0.3)

    # Set labels
    plt.xlabel("Per Capita GDP")  # Label x axis
    plt.ylabel("Happiness Index") # Label y axis

    # This optional code adds labels
    # loop over the country names and add them to the plot
    # at the same coordinates as the bubble if the country
    # is larger than a minimum population
    if country_list != None:
        for i in range(len(country_list)):
            label = country_list[i]    # label point by country
            x = gdp_list[i]            # x-axis location of label
            y = happy_list[i]          # y-axis location of label
            plt.annotate(label, (x, y))# set label
    
    # This shows the plot
    plt.show()

# Main program
def main():
    # Build dictionary mapping countries to happiness index
    happy_dict = make_happy_dict()
    # Read file containing population and GDP data and add happiness data
    read_gdp_data(happy_dict)
    # read the happiness file 
    country_list,gdp_list,pop_list,happy_list = read_data_file()
    # plot the happiness data
    plot_data(country_list,gdp_list,pop_list,happy_list)

main()
