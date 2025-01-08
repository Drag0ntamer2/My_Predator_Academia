label digestion_start(Prey, Pred):
    python:
        prey = Prey
        pred = Pred
        preyName = prey.name
        predName = pred.name
        minigame_active = True
        digestion_active = True
    return
label prey_vore_action(preyAction="rest", type="digest"):

    if prey.disOverload:
        $ preyAction = "rest"  # Force rest if disOverload is active

    "[preyName] used {b}[preyAction]{/b}"
    python:
        damage = 0
        difficulty = preferences.difficulty
        if preyAction == "light struggle":
            # Check stamina and calculate damage
            actionCost = 15 + difficulty * 4
            if prey.stam >= actionCost:
                damage = max(0, (difficultyDamage(difficulty) * prey.stren) - (pred.con * pred.sComp))
                if damage == 0:
                    prey.addDis(disOverflow(difficulty, pred.sComp, prey.con))
            else:
                prey.addDis(disOverflow(actionCost * 0.1 - prey.stam, pred.sComp, prey.con))
            prey.stam = max(prey.stam - actionCost, 0)

        elif preyAction == "moderate struggle":
            # Check stamina and calculate damage
            actionCost = 25 + difficulty * 4
            if prey.stam >= actionCost:
                damage = max(0, (difficultyDamage(difficulty) * 2 * prey.stren) - (pred.con * pred.sComp))
                if damage == 0:
                    prey.addDis(disOverflow(difficulty, pred.sComp, prey.con))
            else:
                prey.addDis(disOverflow(actionCost * 0.1 - prey.stam, pred.sComp, prey.con))
            prey.stam = max(prey.stam - actionCost, 0)

        elif preyAction == "aggressive struggle":
            # Check stamina and calculate damage
            actionCost = 35 + difficulty * 4
            if prey.stam >= actionCost:
                damage = max(0, (difficultyDamage(difficulty) * 4 * prey.stren) - (pred.con * pred.sComp))
                if damage == 0:
                    prey.addDis(disOverflow(difficulty, pred.sComp, prey.con))
            else:
                prey.addDis(disOverflow(actionCost * 0.1 - prey.stam, pred.sComp, prey.con))
            prey.stam = max(prey.stam - actionCost, 0)

        elif preyAction == "rest":
            # Recover stamina only if no recent disorientation increase
            if not prey.recDis:
                prey.stam += 5 * prey.con - difficulty * 4
                prey.stam = min(prey.maxStam, prey.stam)

        elif preyAction == "massage":
            # Reduce compression and increase predator arousal
            actionCost = 15 + difficulty * 4
            if prey.stam >= actionCost:
                pred.sComp = max(0.01, pred.sComp - prey.dex)
                pred.arousal += prey.dex * pred.lewdness * 0.1
            else:
                prey.addDis(disOverflow(actionCost * 0.1 - prey.stam, pred.sComp, prey.con))
            prey.stam = max(prey.stam - actionCost, 0)

        ##### Apply Prey Disorientation #####
        pred.shp -= applyDis(prey.dis, damage)

        ##### End of Round Conditions #####
        prey.disDecay(prey.con * 0.1)
        if prey.hp <= 0:
            prey.alive = False
        if pred.shp <= 0:
            prey.inStomach = False

    return preyAction



label pred_vore_action(predAction="auto", type="digest"):
    python:
        compMultiplier = 1
        # Local variables for effects
        disorientation = 0
        compression = 0
        damage = 0
        nausea = 0
        pred.disDecay(pred.con * 0.1)
        difficulty = preferences.difficulty

    if pred.disOverload:
        $ predAction = "rest"  # Force rest if disOverload is active

    "[predName] used {b}[predAction]{/b}"
    python:
        if predAction == "squeeze":
            actionCost = 15 + difficultyDamage(difficulty) * 2
            if pred.stam >= actionCost:
                compression = max(0, (difficulty * pred.stren * compMultiplier) / (prey.con * prey.stren))
                if compression == 0:
                    pred.addDis(disOverflow(actionCost * 0.1, prey.stren, pred.con))
            else:
                pred.addDis(disOverflow(actionCost * 0.1 - pred.stam, prey.stren, pred.con))
            pred.stam = max(pred.stam - actionCost, 0)

        elif predAction == "crush":
            actionCost = 30 + difficultyDamage(difficulty) * 2
            if pred.stam >= difficultyDamage(difficulty) * 4:
                compression = max(0, (difficulty * pred.stren * compMultiplier) / (prey.con * prey.stren))
                if compression == 0:
                    pred.addDis(disOverflow(difficultyDamage(difficulty), prey.stren, pred.con))
            else:
                pred.addDis(disOverflow(actionCost * 0.1 - pred.stam, prey.stren, pred.con))
            pred.stam = max(pred.stam - actionCost, 0)

        elif predAction == "massage":
            actionCost = 15 + difficultyDamage(difficulty) * 2
            if pred.stam >= actionCost:
                compression = min(0, (-1 * pred.con) * 1.5)
                prey.arousal += pred.dex * prey.lewdness * 0.1
                pred.arousal += pred.dex * pred.lewdness * 0.1
                pred.shp = min(pred.maxShp, pred.shp + 5)
            else:
                pred.addDis(disOverflow(actionCost * 0.1 - pred.stam, prey.stren, pred.con))
            pred.stam = max(pred.stam - actionCost, 0)

        elif predAction == "rest":
            if not pred.recDis:
                pred.stam += difficulty * pred.con
                pred.stam = min(pred.maxStam, pred.stam)

        elif predAction == "shake":
            actionCost = 40 + difficultyDamage(difficulty) * 3
            if pred.stam >= actionCost:
                # Prey effects
                disorientation = 2.5 - (prey.con * 0.1)  # Base disorientation for prey
                if renpy.random.randint(1, 5) == 1:  # 1/5 chance for minor damage
                    damage = max(0, difficulty - prey.con)

                # Recoil effects
                nausea = 2 + pred.aLev - (pred.con * 0.1)# Disorientation recoil
                pred.shp -= pred.aLev
            else:
                pred.addDis(disOverflow((actionCost - pred.stam) * 0.1, prey.stren, pred.con))
            pred.stam = max(pred.stam - actionCost, 0)

        ##### Apply Predator Disorientation #####
        prey.hp = max(prey.hp - applyDis(pred.dis, damage), 0)  # Apply disoriented damage
        pred.sComp = max(0.01, min(50, pred.sComp + applyDis(pred.dis, compression)))  # Apply disoriented compression
        prey.addDis(applyDis(pred.dis, disorientation))  # Apply disoriented disorientation

        ##### Acid Damage ##### (passive, and separate from dealt damage)
        if (pred.aStren * pred.aLev >= prey.aRes * 2) & (type != "contain"):
            damage = (pred.aStren / prey.aRes) * pred.aLev
            if type == "digest":
                prey.hp -= max(damage, 0)
            else:
                if pred.arousal <= 25:
                    prey.hp -= max(damage, 0) / 2
                else:
                    prey.hp -= max(damage, 0) + (0.1 * pred.arousal)



        ##### Acid Level Adjustments #####
        pred.aLev += pred.aFill
        pred.aLev = min(pred.aLev, 1)

        ##### Nausea & Decay #####
        pred.addDis(nausea)

        ##### End of Round Conditions #####
        if prey.hp <= 0:
            prey.alive = False

    return predAction










####################################################################################################
# - the pred is attempting only to contain her prey.
# - The pred doesn't have a set win condition, but rather, only needs to contain the prey until
#     she decides she no longer wants to do so.
# - the prey wins if they escape before that happens.
####################################################################################################
#label containment_round():



####################################################################################################
# - the pred may or may not be attempting to digest the prey
# - the prey's objective is to pleasure the pred as much as possible
# - the pred may or may not reciprocate
####################################################################################################
#label pleasure_round():


