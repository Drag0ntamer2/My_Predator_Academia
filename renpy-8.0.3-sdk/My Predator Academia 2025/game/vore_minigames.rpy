label digestion_start(prey_list, Pred, PredBars = [ True, True, True, True, True ], PreyBars = predBars = [ True, True, True, True, False ]):
label vore_start(prey_list, Pred, PredBars = [ True, True, True, True, True ], PreyBars = predBars = [ True, True, True, True, False]):
    # MINIGAME SETUP: store the participants and mark each prey as inside.
    # The action labels below mutate these participant objects.
    python:
        preyList = prey_list                                        # List of prey involved in the vore
        pred = Pred                                                 # Single pred participating in the vore
        predName = pred.name                                        # Store pred's name for display
        vore_active = True                                          # Flag to indicate vore is active

        predBars = PredBars
        preyBars = PreyBars

        for prey in preyList:
            prey.inStomach = True
    return



label prey_vore_action(prey, preyAction="rest", target = None):
    # PREY TURN: choose an action, pay its stamina cost, and resolve its effects.
    $ preyName = prey.name                                          # Get prey's name for display

    if prey.disOverload:
        $ preyAction = "rest"                                       # Force rest if disOverload is active

    "[preyName] used {b}[preyAction]{/b}"                           # reveal action used by prey

    python:
        diff = preferences.difficulty                               # Game Difficulty
        diffDamage = difficultyDamage()                             # Difficulty scaling for damage
        actionCost = 0                                              # Stores the cost, in stamina, of an action
        damage = 0                                                  # Stores damage to apply to pred's stomach
        prey.bracing = False                                        # stop bracing
        prey.disDecay()                                             # reduce disorientation

        if preyAction == "light struggle":
            # EQUATION: actionCost = 15 + (difficulty * 4)
            # damageCalc(actionCost, 2) converts the cost into stomach damage.
            actionCost = 15 + diff * 4
            damage = damageCalc(actionCost, 2)                      # Calculate Struggle Damage

        elif preyAction == "moderate struggle":
            # EQUATION: actionCost = 25 + (difficulty * 4)
            # damageCalc(actionCost, 3) converts the cost into stomach damage.
            actionCost = 25 + diff * 4
            damage = damageCalc(actionCost, 3)                      # Calculate Struggle Damage

        elif preyAction == "aggressive struggle":
            # EQUATION: actionCost = 35 + (difficulty * 4)
            # damageCalc(actionCost, 4) converts the cost into stomach damage.
            actionCost = 35 + diff * 4
            damage = damageCalc(actionCost, 4)                      # Calculate Struggle Damage

        elif preyAction == "rest":
            # EQUATION: stamina restored = (5 * prey constitution) - (difficulty * 4)
            prey.addStam(5 * prey.con - diff * 4)                   # Restore Stamina

        elif preyAction == "massage":
            # EQUATION: actionCost = 15 + (difficulty * 4)
            actionCost = 15 + diff * 4
            if prey.stam >= actionCost:
                pred.loseComp(prey.dex)                             # Reduce Stomach Compression
                if (prey.lewdness >= 3) or (type == "pleasure"):
                    # EQUATION: arousal increase = dexterity * lewdness * 0.1
                    pred.addArousal(prey.dex * pred.lewdness * 0.1) # Increase pred Arousal
                    prey.addArousal(prey.dex * prey.lewdness * 0.1) # Increase prey Arousal

        elif preyAction == "Pleasure Self":
            # EQUATION: actionCost = 5 + difficulty
            actionCost = 5 + diff
            if prey.stam >= actionCost:
                # EQUATION: prey arousal increase = lewdness * dexterity * 0.1
                prey.addArousal(prey.lewdness * prey.dex * 0.1)     # Increase prey Arousal
                if pred.lewdness >= 4:
                    # EQUATION: predator arousal increase = prey dexterity * predator lewdness * 0.1
                    pred.addArousal(prey.dex * pred.lewdness * 0.1) # Increase pred Arousal

        elif preyAction == "Try to pleasure pred":
            # EQUATION: actionCost = 10 + (difficulty * 2)
            actionCost = 10 + diff * 2
            if prey.stam >= actionCost:
                # EQUATION: predator arousal increase = prey dexterity * predator lewdness * 0.1
                pred.addArousal(prey.dex * pred.lewdness * 0.1)     # Increase pred Arousal
                if prey.lewdness >= 4:
                    # EQUATION: prey arousal increase = prey dexterity * prey lewdness * 0.1
                    prey.addArousal(prey.dex * prey.lewdness * 0.1) # Increase prey Arousal

        elif preyAction == "Pleasure Fellow Prey":
            # EQUATION: actionCost = 5 + difficulty
            actionCost = 5 + diff
            if prey.stam >= actionCost:
                # EQUATION: target arousal increase = target lewdness * prey dexterity * 0.1
                target.addArousal(target.lewdness * prey.dex * 0.1)     # Increase pred Arousal

        elif preyAction == "brace":
            # EQUATION: actionCost = 15 + (difficulty * 4)
            actionCost = 15 + diff * 4
            if prey.stam >= actionCost:
                prey.bracing = True




        ##### End of Turn Calculations #####
        # EQUATION: overflow = max((action cost - remaining stamina) * 0.1, 0)
        prey.loseStam(actionCost)                                   # apply stamina cost
        overflow = max((actionCost - prey.stam) * 0.1, 0)           # calculate stamina overflow
        # EQUATION: prey disorientation increase = (overflow + predator compression) / prey constitution
        prey.addDis((overflow + pred.comp) / prey.con)              # apply disOverflow

    if damage > pred.shp:
        # Damage greater than current stomach health causes escape.
        $ prey.inStomach = False
        "[preyName] has escaped!"
        python:
            newPreyList = []
            for prey in preyList:
                if prey.inStomach:
                    newPreyList.append(prey)
            preyList = newPreyList
    else:
        # DELEGATED EQUATION: applyDis(prey.dis, damage) adjusts damage using
        # prey disorientation before stomach health is reduced.
        $ pred.loseShp(applyDis(prey.dis, damage))                    # apply stomach damage

    # Acid damage is resolved after the prey action and may digest the prey.
    call acidDamage(prey)
    if not prey.alive:
        "[preyName] has been digested!"
        python:
            newPreyList = []
            for Prey in preyList:
                if Prey.alive:
                    newPreyList.append(Prey)
            preyList = newPreyList

    if len(preyList) == 0:
        $ vore_active = False                                     # Flag to indicate vore is no longer active
    return preyAction



label pred_vore_action(predAction, type="digest", target=None):
    # PREDATOR TURN: choose an action, pay stamina, then update compression,
    # disorientation, acid, and direct effects on the prey.

    if pred.disOverload:
        $ predAction = "rest"                                       # Force rest if disOverload is active

    "[predName] used {b}[predAction]{/b}"                           # Reveal the action used by the pred

    python:
        # Variables for calculations
        compMultiplier = 1                                          # Multiplier for balancing compression
        diff = preferences.difficulty                               # Game Difficulty
        diffDamage = difficultyDamage()                             # Increases inversely from difficulty
        actionCost = 0                                              # Stamina cost of the pred's action
        nausea = 0                                                  # Nausea to apply to pred
        comp = 0                                                    # Compression of pred's stomach
        prey.disDecay()


        if predAction == "squeeze":
            # EQUATION: actionCost = 15 + (difficulty damage modifier * 2)
            # compress(actionCost, compMultiplier) converts cost to compression.
            actionCost = 15 + diffDamage * 2
            comp = compress(actionCost, compMultiplier)             # Calculate compression

        elif predAction == "crush":
            # EQUATION: actionCost = 30 + (difficulty damage modifier * 2)
            # compress(actionCost, compMultiplier) converts cost to compression.
            actionCost = 30 + diffDamage * 2
            comp = compress(actionCost, compMultiplier)             # Calculate compression

        elif predAction == "rest":
            # EQUATION: stamina restored = (5 * predator constitution) - (difficulty damage modifier * 4)
            pred.addStam(5 * pred.con - diffDamage * 4)             # Recover stamina for the pred

        elif predAction == "pleasure self":
            # EQUATION: actionCost = 5 + difficulty damage modifier
            actionCost = 5 + diffDamage
            # EQUATION: predator arousal increase = lewdness * dexterity * 0.1
            pred.addArousal(pred.lewdness * pred.dex * 0.1)         # Pred increases their own arousal


        elif predAction == "massage":
            # EQUATION: actionCost = 15 + (difficulty damage modifier * 2)
            actionCost = 15 + diffDamage * 2
            pred.addShp(5 + diff)                                   # Recover stomach health
            for prey in preyList:
                prey.addArousal(pred.dex * prey.lewdness * 0.1)     # Increase prey arousal


        elif predAction == "shake":
            # EQUATION: actionCost = 40 + (difficulty damage modifier * 3)
            actionCost = 40 + diffDamage * 3
            # EQUATION: nausea = 2 + arousal level - (predator constitution * 0.1)
            nausea = 2 + pred.aLev - (pred.con * 0.1)               # Calculate nausea recoil
            # EQUATION: base prey disorientation = 2.5 - (prey constitution * 0.1)
            dis = 2.5 - (prey.con * 0.1)                            # Base disorientation for prey
            for prey in preyList:
                # DELEGATED EQUATION: applyDis(pred.dis, dis) adjusts the
                # base disorientation using predator disorientation.
                Dis = applyDis(pred.dis, dis)
                prey.addDis(Dis)                                    # Apply disorientation to prey
                if renpy.random.randint(1, 5) == 1:                 # 20% chance to apply damage
                    # EQUATION: prey damage = predator strength + difficulty - prey constitution
                    damage = pred.stren + diff - prey.con           # Calculate prey damage
                    prey.loseHp(max(0, damage))                     # Apply damage to prey

        elif predAction == "try to pleasure prey":
            # EQUATION: actionCost = 10 + (difficulty damage modifier * 2)
            actionCost = 10 + diffDamage * 2
            if target:
                # EQUATION: target arousal increase = (predator dexterity * 0.5) * target lewdness
                dex = pred.dex * 0.5
                target.addArousal(dex * target.lewdness)            # Increase specific prey arousal
            else:
                # EQUATION: each prey arousal increase = (predator dexterity * 0.1) * prey lewdness
                dex = pred.dex * 0.1
                for prey in preyList:
                    prey.addArousal(dex * prey.lewdness)            # Increase arousal for all prey

        # End-of-action calculations for pred
    # EQUATION: overflow = max((action cost - remaining stamina) * 0.1, 0)
        pred.loseStam(actionCost)                                   # Apply stamina cost to pred
        overflow = max((actionCost - pred.stam) * 0.1, 0)           # calculate stamina overflow
    # EQUATION: predator disorientation increase = overflow / predator constitution
        pred.addDis(overflow / pred.con)                            # apply disOverflow
        renpy.say("debug", f"{overflow}")
        # DELEGATED EQUATION: applyDis(pred.dis, comp) adjusts compression
        # using predator disorientation before adding it to current compression.
        pred.addComp(applyDis(pred.dis, comp))                      # Apply Compression
        pred.acidRise()                                             # Increase stomach acid level


    return predAction

