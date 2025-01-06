label digestion_round(Prey, Pred, preyAction="auto", predAction="auto"):
    python:
        # Reference objects
        prey = Prey
        pred = Pred

        ##### Predator Actions #####
        if predAction == "squeeze":
            pred.sComp = min(1, pred.sComp + pred.stren * 0.5)  # Increase compression, cap at 1
            pred.stam -= 3
        elif predAction == "crush":
            pred.sComp = min(1, pred.sComp + pred.stren)  # Stronger compression increase
            pred.stam -= 6
        elif predAction == "massage":
            pred.stam -= 1
            pred.shp += 1
            pred.shp = min(pred.shp, pred.maxShp)  # Cap at max stomach health
        elif predAction == "rest":
            pred.stam += 1
            pred.stam = min(pred.stam, pred.maxStam)
        elif predAction == "shake":
            # Risky move: increases prey disorientation, reduces predator SHP
            recoil_damage = max(1, 5 - pred.con * 0.5)  # Recoil damage based on predator constitution
            pred.shp -= recoil_damage
            disorientation_increase = (pred.stren - prey.con * 0.5) * 0.2
            prey.dis += max(0, disorientation_increase)  # Ensure non-negative increase

        ##### Disorientation Decay #####
        disorientation_decay = prey.con * 0.1
        prey.dis = max(0, prey.dis - disorientation_decay)  # Gradually reduce disorientation

        ##### Prey Actions #####
        effectiveness = 0  # Initialize effectiveness for calculations
        if preyAction == "light":
            if prey.stam >= 1:
                prey.stam -= 1
                effectiveness = prey.stren * 0.3 * (1 - pred.sComp)
        elif preyAction == "moderate":
            if prey.stam >= 3:
                prey.stam -= 3
                effectiveness = prey.stren * 0.6 * (1 - pred.sComp)
        elif preyAction == "aggressive":
            if prey.stam >= 5:
                prey.stam -= 5
                effectiveness = prey.stren * (1 - pred.sComp)
        elif preyAction == "rest":
            prey.stam += 1
            prey.stam = min(prey.stam, prey.maxStam)  # Cap at max stamina
            effectiveness = 0  # No damage on resting
        elif preyAction == "massage":
            if prey.stam >= 2:
                prey.stam -= 2
                pred.sComp = max(0, pred.sComp - prey.dex * 0.05)  # Reduction scales with prey dexterity
                effectiveness = 0  # No direct damage on massage

        ##### Disorientation Roll #####
        if prey.dis > 0:
            roll = renpy.random.randint(1, 20)  # d20 roll
            if roll <= prey.dis * 10:  # Higher disorientation increases chance of nullification
                # Nullify or reduce effectiveness based on disorientation level
                if prey.dis >= 0.5:  # High disorientation, possible nullification
                    effectiveness *= renpy.random.uniform(0, 0.5)  # Reduce effectiveness significantly
                else:  # Low disorientation, partial reduction only
                    effectiveness *= renpy.random.uniform(0.5, 0.9)

        # Apply effectiveness to predator stomach health
        if preyAction in ["light", "moderate", "aggressive"]:
            pred.shp -= effectiveness
            if pred.shp <= 0:
                prey.inStomach = False

        ##### Acid Damage #####
        if pred.aStren * pred.aLev * 2 >= prey.aRes:
            damage = (pred.aStren * pred.aLev) - prey.aRes
            prey.hp -= max(damage, 0)  # Ensure no negative damage

        ##### Acid Level Adjustments #####
        pred.aLev += pred.aFill
        pred.aLev = min(pred.aLev, 1)  # Cap acid level at 1

        ##### End of Round Conditions #####
        if prey.hp <= 0:
            prey.alive = False
        if pred.shp <= 0:
            prey.inStomach = False

    # Return updated objects
    return prey, pred












####################################################################################################
# - the pred is attempting only to contain her prey.
# - The pred doesn't have a set win condition, but rather, only needs to contain the prey until
#     she decides she no longer wants to do so.
# - the prey wins if they escape before that happens.
####################################################################################################
label containment_round()



####################################################################################################
# - the pred may or may not be attempting to digest the prey
# - the prey's objective is to pleasure the pred as much as possible
# - the pred may or may not reciprocate
####################################################################################################