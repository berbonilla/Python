import math

def hypotenuse(a,b):
    return math.sqrt((math.pow(a,2)+(math.pow(b,2))))

a,b = list(map(int,input("Input A & B:").split()))
print(f"The hypotenuse of side a and b is: %0.2f" % (hypotenuse(a,b)))

