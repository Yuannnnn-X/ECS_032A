# mileage.py
# Yuan Xie
#
# calculate mileage of a car

# print the sentence
print("Your Personal Fuel Economy")
# prompt the values
miles = input("Number of miles traveled (or enter to exit):")
gallons = input("Number of gallons needed:")
SumMiles = 0
SumGallons = 0
while True:
        miles = int(miles)
        gallons = int(gallons)
        SumMiles = SumMiles + miles
        SumGallons = SumGallons + gallons
        Mileage = miles / gallons
        print("Mileage this tank =","{:.1f}".format(Mileage))
        miles = input("Number of miles traveled (or enter to exit):")
        if miles == "":
            AverMileage = SumMiles  / SumGallons
            print("Average mileage =","{:.1f}".format(AverMileage))
            break
        gallons = input("Number of gallons needed:")
            

