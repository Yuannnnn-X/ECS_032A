# cash_register.py
# Yuan Xie
#
# calculate price

# print the first sentence
print("Cash register (press enter to exit)")
item = 0
cost = 0
total = 0
item_cost = input("Enter item cost:")
# build the while loop
while True:
    if item_cost == "":
        print("You entered",item,"items totaling","${:.2f}".format(total))
        break
    elif item_cost != "":
        item_cost = float(item_cost)
        item = item + 1
        total = total + item_cost
        item_cost = input("Enter item cost:")
        if item_cost == "":
            print("You entered",item,"items totaling","${:.2f}".format(total))
            break
           
            
    


        
    
