import math

class distance:
  def __init__(self, x1, y1,z1,x2,y2,z2):
    self.x1 = x1
    self.y1 = y1
    self.z1 = z1
    self.x2 = x2
    self.y2 = y2
    self.z2 = z2
  def printcoords(self):
    print("Initial x:%.0f y:%.0f z:%.0f\nFinal x:%.0f y:%.0f z:%.0f" %
          (self.x1, self.y1, self.z1, self.x2, self.y2, self.z2))
    
def coordForm(x1,y1,z1,x2,y2,z2):
    distancecal = float(math.sqrt(pow((x2-x1),2)+pow((y2-y1),2)+pow((z2-z1),2)))
    print("The distance is %.2f" % (distancecal))

try:    
    x1,y1,z1 = list(map(float, input("Point 1(x1 y1 z1):").split()))
    x2,y2,z2 = list(map(float, input("Point 2(x2 y2 z2):").split()))

    D = distance(x1,y1,z1,x2,y2,z2)
    D.printcoords()
    coordForm(x1,y1,z1,x2,y2,z2)
except:
   print("Invalid Character Input!")



    
