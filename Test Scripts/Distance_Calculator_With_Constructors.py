import math

class distance:
  def __init__(self, x1, y1,x2,y2):
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2
  def printcoords(self):
      print("Initial x:%f y:%.0f \nFinal x:%.0f y:%.0f" % (self.x1,self.y1,self.x2,self.y2))
    
def my_function(x1, y1,x2,y2):
    distancecal = float(math.sqrt(pow((x2-x1),2)+pow((y2-y1),2)))
    print("The distance is %f" % (distancecal))
    
try:
    x1,y1 = list(map(float, input("Input Initial Coordinates:").split()))
    x2,y2 = list(map(float, input("Input Final Coordinates:").split()))
    D = distance(x1, y1,x2,y2)
    D.printcoords()
    my_function(x1, y1,x2,y2)

except:
    print("Please input two(2) values separated with a white space")


    
