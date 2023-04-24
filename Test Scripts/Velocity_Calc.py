import math

def velocityCalc(a,b):
    return a/b

a,b = list(map(int,input("Input Displacement and Time: ").split()))

print(f"The Velocity of %d and %d is :%0.4f m/s" % (a,b,velocityCalc(a,b)))

