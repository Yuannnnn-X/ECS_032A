# hybrid.py
# Yuan Xie
#
# help decide whether to buy a hybrid car
CarCost = input("Cost of car:") #prompt the cost of the car
CarCost = float(CarCost) #change it into a floating point number
MilesDrivenPerYear = input("Miles driven per year:") #prompt miles driven per year
MilesDrivenPerYear = float(MilesDrivenPerYear) #change it into a floating point number
GasCost = input("Cost of gas:") #prompt the cost of gas
GasCost = float(GasCost) #change it into a floating point number
FuelEfficiency = input("Fuel efficiency (mpg):") #prompt fuel efficiency
FuelEfficiency = float(FuelEfficiency) #change it into a floating point number
EstimatedResale = input("Estimated resale value after 5 years:") #prompt the resale value
EstimatedResale = float(EstimatedResale) #change it into a floating point number
GasCost5 = MilesDrivenPerYear*5*GasCost/FuelEfficiency #the formula to calculate five year gas cost
CarCost5 = CarCost - EstimatedResale #the formula to calculate five year car cost
TotalCost5 = GasCost5 + CarCost5 #the formula to calculate five year total cost
print("Five year gas cost: {:.1f}".format(GasCost5))
print("Five year car cost: {:.1f}".format(CarCost5))
print("Five year total cost: {:.1f}".format(TotalCost5))




