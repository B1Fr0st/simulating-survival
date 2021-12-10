class Survivor():
  def __init__(self,hunger,water,health,isSick):
    self.hunger = hunger
    self.water = water
    self.health = health
    self.isSick = isSick
    self.sickDays = 0
  def passDay():
    if self.isSick && self.sickDays < 3:
      self.health -=5
      self.hunger -=5
      self.water  -=5
      self.sickDays += 1
    elif !self.isSick:
      self.hunger --
      self.water --
    if self.sickDays > 2:
      self.sickDays = 0
      self.isSick = False
    if self.hunger < 25:
      self.health --
    if self.water < 10:
      self.
