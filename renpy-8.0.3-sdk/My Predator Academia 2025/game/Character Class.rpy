init -9998 python:
    intvert = True
    outvert = False
    socialStance = intvert
    class Char:
        def __init__(self, name, sex, abrev="", altName="", color="#ffffff", health=15, stam=10, strength=1,stomachHealth=0,
            acidStrength=0, stomachSize=0, size=1, acidResistance=1, acidFillRate=0,dexterity=1, constitution=1, lewdness=1,
            arousalMax = 50, choiceWeights = 0, face = "images/faces/Name_thumb.png", profile = None):
# Name fields ----------------------------------------------------------------------------------------------------------
            if name == "EMPTY CHAR":
                self.name = name
                self.NameHold = name
                self.sex = sex
                return
            self.sex = sex
            Name = name.split(' ')
            self.name = Name[0]
            self.abrev = abrev
            self.NameHold = Name[0]
            characters[abrev] = self
            if len(Name) == 1:
                self.fullName = Name[0]
            elif len(Name) == 2:
                self.fullName = Name[0] + " " + Name[1]
            elif len(Name) == 3:
                self.fullName = Name[0] + " " + Name[1] + " " + Name[2]
# Misc fields ----------------------------------------------------------------------------------------------------------
            self.c = Character(self.name, who_color = color, what_color = color, image = self.name.lower())
            self.color = color
            self.exampts = 0
            self.face = face
            if self.face == "images/faces/Name_thumb.png":
                self.hover = "images/faces/Name_thumb.png"
            else:
                self.hover = f"images/faces/{self.name} face hover.png"

            self.profile = profile
            self.boobs = 0
            self.belly = 0
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
            self.arousalMax = arousalMax    # how long the character can keep going before climax
            self.lewdness = lewdness        # how easy it is to get the character horny
            self.vornyness = 0              # lewd interest in vore specifically
            self.size = size                # the physical size of this character
            self.aRes = acidResistance      # the character's resistence to stomach acid
            self.shp = stomachHealth        # the character's ability to keep prey from escaping their stomach
            self.sSize = stomachSize        # the physical size of the character's stomach at max stretch
            self.aStren = acidStrength      # the potency of the character's stomach acid
            self.aFill = acidFillRate       # how quickly the character's stomach fills with acid
            self.aLev = 0                   # how much the stomach has filled with acid
            self.comp = 0.01                # how much the stomach, and by extension its contents are being squished. (minimum 0.01)
            self.dis = 0                    # disorientation / nausea
            self.disOverload = False        # disorientation / nausea overload
            self.recDis = False             # was disorientation increased last round
            self.inStomach = False          # is this character currently in a stomach
            self.alive = True               # is this character currently alive
            self.bracing = False            # is this character currently bracing
            return

        def addDis(self, amt):
            if amt == 0:
                return
            self.dis += amt
            self.recDis = True
            if self.dis >= self.con: # constitution serves as the max disorientation a character can handle
                self.disOverload = True
            return

        def disDecay(self, amt = -1):
            if self.recDis:
                self.recDis = False
                return
            if amt == -1:
                amt = self.con * 0.1
            if self.dis > self.con:
                self.dis = self.con
            renpy.say("Debug", f"Disorientation = {self.dis} {self.name}")
            self.dis = max(0, self.dis - amt)

            if self.disOverload & (self.dis <= 2.5):
                self.disOverload = False
            return

        def addArousal(self, amt):
            self.arousal += amt + (0.1 * self.arousal)
            if self.arousal >= self.arousalMax:
                #self.arousal = 0
                return True     # reached climax
            return False        # did not reach climax

        def arousalDecay(self, amt):
            self.arousal = max(0, self.arousal - amt)
            return

        def addHp(self, amt):
            self.hp = min(self.maxHp, self.hp + amt)
            return

        def loseHp(self, amt):
            self.hp = max(0, self.hp - amt)
            if self.hp == 0:
                self.alive = False
            return

        def addShp(self, amt):
            self.shp = min(self.maxShp, self.shp + amt)
            return

        def loseShp(self, amt):
            self.shp = max(0, self.shp - amt)
            return

        def addStam(self, amt):
            self.stam = min(self.maxStam, self.stam + amt)
            return

        def loseStam(self, amt):
            self.stam = max(0, self.stam - amt)
            return
            
        def addComp(self, amt):
            self.comp = min(maxComp, self.comp + amt)
            return

        def loseComp(self, amt):
            self.comp = max(0.01, self.comp - amt)
            return
            
        def acidRise(self):
            self.aLev = min(self.aLev + self.aFill, 1)
            return

        def reset(self):
            self.hp = self.maxHp
            self.stam = self.maxStam
            self.arousal = 0                # how horny the character is
            self.shp = self.maxShp          # the character's ability to keep prey from escaping their stomach
            self.aLev = 0                   # how much the stomach has filled with acid
            self.comp = 0.01                # how much the stomach, and by extension its contents are being squished. (minimum 0.01)
            self.dis = 0                    # disorientation / nausea
            self.disOverload = False        # disorientation / nausea overload
            self.recDis = False             # was disorientation increased last round
            self.inStomach = False          # is this character currently in a stomach
            self.alive = True               # is this character currently alive
            self.bracing = False            # is this character currently bracing


        def chooseAction(self):

            num = renpy.random.randint(0,100)
            if num < 50:
                actionCost = 40 + diffDamage * 3
                if self.stam < actionCost:
                    return "rest"
                else:
                    return "shake"
            elif num < 70:
                actionCost = 30 + diffDamage * 3
                if self.stam < actionCost:
                    actionCost = 15 + diffDamage * 3
                    if self.stam < actionCost:
                        return "rest"
                    else:
                        return "squeeze"
                else:
                    return "crush"
            elif num < 95:
                actionCost = 15 + diffDamage * 2
                if self.stam < actionCost:
                    return "rest"
                else:
                    return "massage"
            else:
                actionCost = 10 + diffDamage * 2
                if self.stam < actionCost:
                    return "rest"
                else:
                    return "try to pleasure prey"
