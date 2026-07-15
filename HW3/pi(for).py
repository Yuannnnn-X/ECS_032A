# pi.py
# Yuan Xie
#
# pi approximation

import math
pai = 0
NumTerms = int(input("Number of terms:"))
for i in range(1,NumTerms):
    pai = pai + (((-1)**(i-1))*4)/(2*i-1)
print("Estimate of pi:","{:.9f}".format(pai))
error = math.pi - pai
print("Error:","{:.9f}".format(error))

    

    

