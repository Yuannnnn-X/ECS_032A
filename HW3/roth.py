# roth.py
# Yuan Xie
#
# double your money

# prompt the initial deposit
Initial = float(input("Enter an initial Roth IRA deposit amount:"))
deposit = Initial
# prompt the rate of return
rate = int(input("Enter an annual percent rate of return:"))
Return = rate / 100
year = 0
# bulid the while loop
while True:
    if deposit < 2 * Initial:
        year = year + 1
        deposit = deposit + (deposit * Return)
        print("Value after year",str(year)+":", "${:.2f}".format(deposit))
    else:
        break
print("It will take",year,"years to double your investment with a",\
      str(rate)+"%","APR.")
        

