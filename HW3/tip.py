# tip.py
# Yuan Xie
#
# offering tipping options

# prompt total
Total = float(input("Enter total:"))
pct = 14
# build the loop
while pct < 25:
    pct = pct + 1
    Tip = Total * pct / 100
    print("A",str(pct)+"%","tip is","${:.2f}".format(Tip))

    

              

