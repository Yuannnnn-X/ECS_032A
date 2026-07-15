# pi.py
# Yuan Xie
#
# pi approximation

# prompt the number of terms
num = int(input("Number of terms:"))
n = 1
pai = 0
# build the while loop
while n <= num:
    term = (((-1)**(n-1))*4)/(2*n-1)
    pai = pai + term
    n = n + 1
print("Estimate of pi:","{:.9f}".format(pai))
import math
# calculate the error
error = math.pi - pai
print("Error:","{:.9f}".format(error))
    
    
    
    
