init -9998 python:
    intvert = True
    outvert = False
    socialStance = intvert
    class Char:
        def __init__(self, name, heroName = "", abrev = "", altName = "", color = "#ffffff", health=15, stam=10, strength=1, stomachHealth=15, acidStrength=1, stomachSize=0, size=1, acidResistance=1, acidFillRate=0.1, dexterity=1, constitution=1):
# Name fields ----------------------------------------------------------------------------------------------------------
            if name == "EMPTY CHAR":
                self.name = name
                self.NameHold = name
                self.sex = sex
                return
            self.name = name[0]
            self.abrev = abrev
            self.spritenam = name[0].lower()
            self.NameHold = name[0]
            self.heroName = heroName
            if len(name) == 1:
                self.fullName = name[0]
            elif len(name) == 2:
                self.fullName = name[0] + " " + name[1]
            elif len(name) == 3:
                self.fullName = name[0] + " " + name[1] + " " + name[2]
# Misc fields ----------------------------------------------------------------------------------------------------------
            self.boobs = 0
            self.belly = 0
            self.color = color
            self.c = Character(self.name, who_color = color, what_color = color)
            self.exampts = 0
# Stat Fields ----------------------------------------------------------------------------------------------------------
            self.maxHp = health
            self.maxStam = stam
            self.maxShp = stomachHealth
            self.hp = health
            self.stam = stam
            self.stren = strength
            self.size = size
            self.aRes = acidResistance
            self.shp = stomachHealth
            self.sSize = stomachSize
            self.aStren = acidStrength
            self.aFill = acidFillRate
            self.dex = dexterity
            self.con = constitution
            self.arousal = 0
            self.aLev = 0       # acid level
            self.sComp = 0      # stomach compression
            self.dis = 0        # disorientation
            self.inStomach = False
            self.alive = True
            return

