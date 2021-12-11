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
  def __init__(self,hunger,water,health,isSick,survI):
    self.hunger = hunger
    self.water = water
    self.health = health
    self.isSick = isSick
    self.sickDays = 0
    self.survI = survI
  def checkDeath(self):
    if self.health <= 0:
      try:
        del survivors[self.survI]
      except Exception as e:
        errorlog.append("Error occured in GarbageCollection:"+e)
  def passDay(self):
    self.checkDeath()
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
  

survivors.append(Survivor(100,100,100,False,0))
print(survivors)
while True:
  for survi in survivors:
    print(survi.health)
    print(survivors)
    survi.passDay()
    print(survi.hunger)
