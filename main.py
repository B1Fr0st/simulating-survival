import random

survivors = []
errorlog = []
def constrain(value,min,max):
  if value >= max:
    val = max
  elif value <= min:
    val = min
  else:
    val = value
  return val
class Survivor():
  def __init__(self,hunger,water,health,isSick,survI,waterProb,hungerProb):
    self.hunger = hunger
    self.water = water
    self.health = health
    self.isSick = isSick
    self.sickDays = 0
    self.survI = survI
    self.waterProb = waterProb
    self.hungerProb = hungerProb
  def checkDeath(self):
    if self.health <= 0:
      try:
        del survivors[self.survI]
      except Exception as e:
        errorlog.append("Error occured in GarbageCollection:"+e)
  def passDay(self):
    self.checkDeath()
    if random.randint(0,100) < self.waterProb:
      self.water += 15
    if random.randint(0,100) < self.hungerProb:
      self.hunger += 25
    
    if self.isSick:
      if self.sickDays < 3:
        self.health -=5
        self.hunger -=5
        self.water  -=5
        self.sickDays += 1

    elif self.isSick == False:
      self.hunger -= 1
      self.water -= 1
      self.health += 1
      

    if self.sickDays > 2:
      self.sickDays = 0
      self.isSick = False
    if self.hunger < 25:
      self.health -= 1
    if self.water < 10:
      self.health -= 5;
    self.water = constrain(self.water,0,100)
    self.hunger = constrain(self.hunger,0,100)
    self.health = constrain(self.health,0,100)
  


def processAvg(data):
    sumTotal = 0
    for point in data:
        sumTotal += point
    return sumTotal/len(data)
def processMax(data):
    curMax = 0
    for point in data:
        if point > curMax:
            curMax = point
    return curMax
def processMin(data):
    curMin = processMax(data)
    for point in data:
        if point < curMin:
            curMin = point
    return curMin
healthdata = []
waterdata = []
hungerdata = []
survivors.append(Survivor(100,100,100,False,0,5,5))#10 points, dedicated to either water (1) or hunger (2)


while len(survivors) > 0:
  for survi in survivors:
    survi.passDay()
    healthdata.append([survi.health,survi.waterProb,survi.hungerProb,survi.survI])
    waterdata.append([survi.water,survi.waterProb,survi.hungerProb,survi.survI])
    hungerdata.append([survi.hunger,survi.waterProb,survi.hungerProb,survi.survI])
    print("\n\nCurrent Hunger:%i\nCurrent Water:%i\nCurrent Health:%i" % (survi.hunger,survi.water,survi.health))


