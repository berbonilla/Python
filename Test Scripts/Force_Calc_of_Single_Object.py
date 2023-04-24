import math

def forceCalc(a,b):
    return a*b

a,b = list(map(int,input("Input Mass and Acceleration: ").split()))

print(f"The Force of %d and %d is :%0.f N" % (a,b,forceCalc(a,b)))

