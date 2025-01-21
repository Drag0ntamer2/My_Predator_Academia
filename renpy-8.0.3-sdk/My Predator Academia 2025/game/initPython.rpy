init -9998 python:
    def difficultyDamage():
        damage_values = {1: 4, 2: 3, 3: 2}  # Easy, Medium, Hard
        return damage_values.get(preferences.difficulty, 2)  # Default to Medium if difficulty is invalid

    def disOverflow(overflow, compression, constitution):
        return (overflow + compression) / constitution


    def applyDis(dis, damage):
        if dis <= 0:
            return damage                                                   # No disorientation, no adjustment
        roll = renpy.random.randint(1, 20)

        # Special cases for extreme disorientation or critical rolls
        if dis > 3:
            if roll == 1:
                return 0                                                    # Complete failure due to high disorientation
            elif roll == 20:
                return damage                                               # Full effectiveness on a critical success

        # Calculate damage reduction based on disorientation
        reduction_factor = dis / 5                                          # Scale disorientation to a 0-1 factor
        roll_modifier = (20 - roll) / 20                                    # Higher rolls mean less reduction
        adjustment = reduction_factor * roll_modifier                       # Combine factors

        # Adjust damage based on calculated reduction
        adjusted_damage = damage * (1 - adjustment)
        if prey.bracing:
            adjusted_damage /= prey.stren


        return max(0, adjusted_damage)                                      # Ensure damage is not negative


    def damageCalc(actionCost, amt):
        if prey.stam >= actionCost:
            diffDamage = difficultyDamage()
            compFactor = pred.con * pred.comp
            return max(0, (diffDamage * amt * prey.stren) - compFactor)
        else:
            return -1

    def compress(actionCost, compMultiplier):
        if pred.stam < actionCost:
            return 0
        preyCon = 1
        preyStren = 1
        for prey in preyList:
            preyCon += prey.con
            preyStren += prey.stren
        resFactor = preyCon * preyStren
        strenFactor = diff * pred.stren
        return (strenFactor * compMultiplier) / resFactor


    def GameCheck():                            #checks if the minigame should remain active
        for prey in preyList:
            if prey.inStomach & prey.alive:
                return True
        return False

    
    def splitList(List):
        left = False
        L = []
        R = []
        for char in List:
            if left:
                L.append(char)
            else:
                R.append(char)
            left = not left
        return [L, R]




label acidDamage(prey):
    $ damage = pred.aStren * pred.aLev
    if (damage >= prey.aRes * 2):
        if pred.arousal <= (pred.con / 2):
            $ prey.loseHp(damage)
        else:
            $ prey.loseHp(damage + (0.1 * pred.arousal))

    return


