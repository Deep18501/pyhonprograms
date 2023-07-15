import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self,**balls):
    self.contents=[]
    for key,value in balls.items():
        self.contents.extend([key] * value)

  def draw(self,num):
    drawn=[]
    if num>= len(self.contents):
      temp=self.contents.copy()
      self.contents.clear()
      return temp
    for i in range(num):
      drawn.append(self.contents.pop(random.randint(0, len(self.contents)-1)))
    return drawn
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  succ=0
  expected=[]
  # exlen=num_balls_drawn-len(expected)
  for k,v in expected_balls.items():
    expected.extend([k] * v)
  
  # print(expected)
  for i in range(num_experiments):
      hat1=copy.deepcopy(hat)
      drawn=hat1.draw(num_balls_drawn)
      # print(expected)
      # print(drawn)
      # for b in expected:
      #   try :
      #     drawn.remove(b)
      #   except:
      #     break
      # if len(drawn)==exlen:
      #   succ+=1
      if(all(x in drawn for x in expected)):
        succ+=1
      
      
  # print(succ)
  return round(succ/num_experiments,3)