import math

def momentumCalc(a,b):
    return a*b

a = int(input("Initial Mass: "))
b = int(input("Velocity    : "))

try:
    print("The Momentum is :%0.3f kg m/s" % (momentumCalc(a,b)))
except:
    print("Invalid Input!")
