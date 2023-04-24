import math

def accelerationCalc(a,b,c):
    return (b-a)/c

a = int(input("Initial Velocity: "))
b = int(input("Final Velocity  : "))
c = int(input("Time            : "))
try:
    print("The Acceleration is :%0.3f m/s^2" % (accelerationCalc(a,b,c)))
except:
    print("Invalid Input!")
