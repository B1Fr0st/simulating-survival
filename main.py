survivors = []
class Survivor():
  def __init__(self,hunger,water,health,isSick,survI):
    self.hunger = hunger
    self.water = water
    self.health = health
    self.isSick = isSick
    self.sickDays = 0
  def checkDeath(self):
    if self.health == 0:
      del survivors[self.survI]
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
      if self.health < 100:
        self.health += 1
      

    if self.sickDays > 2:
      self.sickDays = 0
      self.isSick = False
    if self.hunger < 25:
      self.health -= 1
    if self.water < 10:
      self.health -= 5
  

survivors.append(Survivor(100,100,0,False,0))
survi = survivors[0]
while True:
  print(survi.health)
  survi.passDay()
  print(survi.hunger)

