init -9998 python:
    intvert = True
    outvert = False
    socialStance = intvert
    class Char:
        def __init__(self, name, heroName="", abrev="", altName="", color="#ffffff", health=15, stam=10, strength=1,stomachHealth=0, acidStrength=0, stomachSize=0, size=1, acidResistance=1, acidFillRate=0,dexterity=1, constitution=1, oxygen=50, lewdness=1):
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
            self.dex = dexterity
            self.con = constitution
            self.arousal = 0                # how horny the character is
            self.lewdness = lewdness        # how easy it is to get the character horny
            self.size = size                # the physical size of this character
            self.aRes = acidResistance      # the character's resistence to stomach acid
            self.shp = stomachHealth        # the character's ability to keep prey from escaping their stomach
            self.sSize = stomachSize        # the physical size of the character's stomach at max stretch
            self.aStren = acidStrength      # the potency of the character's stomach acid
            self.aFill = acidFillRate       # how quickly the character's stomach fills with acid
            self.aLev = 0                   # how much the stomach has filled with acid
            self.sComp = 0.01               # how much the stomach, and by extension its contents are being squished. (minimum 0.01)
            self.dis = 0                    # disorientation / nausea
            self.disOverload = False        # disorientation / nausea overload
            self.recDis = False             # was disorientation increased last round
            self.inStomach = False          # is this character currently in a stomach
            self.alive = True               # is this character currently alive
            self.oxy = oxygen               # how much oxygen does this character currently have
            self.oxyMax = oxygen            # how much oxygen can this character hold
            return

        def addDis(self, amt):
            self.dis += amt
            if amt > 0:
                self.recDis = True
            if self.dis >= 4:
                self.disOverload = True
            return

        def disDecay(self, amt):
            if self.recDis:
                self.recDis = False
                return
            self.dis = max(0, self.dis - amt)

            if self.disOverload & (self.dis <= 2.5):
                self.disOverload = False
            return