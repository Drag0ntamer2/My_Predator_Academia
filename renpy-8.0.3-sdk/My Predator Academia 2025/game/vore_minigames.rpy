label digestion_start(prey_list, Pred, PredBars = [ True, True, True, True, True ], PreyBars = predBars = [ True, True, True, True ]):
label minigame_start(prey_list, Pred, PredBars = [ True, True, True, True, True ], PreyBars = predBars = [ True, True, True, True ]):
    python:
        preyList = prey_list                                        # List of prey involved in the minigame
        pred = Pred                                                 # Single pred participating in the minigame
        predName = pred.name                                        # Store pred's name for display
        minigame_active = True                                      # Flag to indicate minigame is active

        predBars = PredBars
        preyBars = PreyBars

        for prey in preyList:
            prey.inStomach = True
    return



label prey_vore_action(prey, preyAction="rest", target = None):
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
            actionCost = 15 + diff * 4
            damage = damageCalc(actionCost, 2)                      # Calculate Struggle Damage

        elif preyAction == "moderate struggle":
            actionCost = 25 + diff * 4
            damage = damageCalc(actionCost, 3)                      # Calculate Struggle Damage

        elif preyAction == "aggressive struggle":
            actionCost = 35 + diff * 4
            damage = damageCalc(actionCost, 4)                      # Calculate Struggle Damage

        elif preyAction == "rest":
            prey.addStam(5 * prey.con - diff * 4)                   # Restore Stamina

        elif preyAction == "massage":
            actionCost = 15 + diff * 4
            if prey.stam >= actionCost:
                pred.loseComp(prey.dex)                             # Reduce Stomach Compression
                if (prey.lewdness >= 3) or (type == "pleasure"):
                    pred.addArousal(prey.dex * pred.lewdness * 0.1) # Increase pred Arousal
                    prey.addArousal(prey.dex * prey.lewdness * 0.1) # Increase prey Arousal

        elif preyAction == "Pleasure Self":
            actionCost = 5 + diff
            if prey.stam >= actionCost:
                prey.addArousal(prey.lewdness * prey.dex * 0.1)     # Increase pred Arousal

        elif preyAction == "Try to pleasure pred":
            actionCost = 10 + diff * 2
            if prey.stam >= actionCost:
                pred.addArousal(prey.dex * pred.lewdness * 0.1)     # Increase pred Arousal

        elif preyAction == "Pleasure Fellow Prey":
            actionCost = 5 + diff
            if prey.stam >= actionCost:
                target.addArousal(target.lewdness * prey.dex * 0.1)     # Increase pred Arousal

        elif preyAction == "brace":
            actionCost = 15 + diff * 4
            if prey.stam >= actionCost:
                prey.bracing = True




        ##### End of Turn Calculations #####
        prey.loseStam(actionCost)                                   # apply stamina cost
        overflow = max((actionCost - prey.stam) * 0.1, 0)           # calculate stamina overflow
        prey.addDis((overflow + pred.comp) / prey.con)              # apply disOverflow

    if damage > pred.shp:
        $ prey.inStomach = False
        "[preyName] has escaped!"
        python:
            newPreyList = []
            for prey in preyList:
                if prey.inStomach:
                    newPreyList.append(prey)
            preyList = newPreyList
    else:
        $ pred.loseShp(applyDis(prey.dis, damage))                    # apply stomach damage

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
        $ minigame_active = False                                     # Flag to indicate minigame is no longer active
    return preyAction



label pred_vore_action(predAction, type="digest", target=None):

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
            actionCost = 15 + diffDamage * 2
            comp = compress(actionCost, compMultiplier)             # Calculate compression

        elif predAction == "crush":
            actionCost = 30 + diffDamage * 2
            comp = compress(actionCost, compMultiplier)             # Calculate compression

        elif predAction == "rest":
            pred.addStam(5 * pred.con - diffDamage * 4)             # Recover stamina for the pred

        elif predAction == "pleasure self":
            actionCost = 5 + diffDamage
            pred.addArousal(pred.lewdness * pred.dex * 0.1)         # Pred increases their own arousal


        elif predAction == "massage":
            actionCost = 15 + diffDamage * 2
            pred.addShp(5 + diff)                                   # Recover stomach health
            for prey in preyList:
                prey.addArousal(pred.dex * prey.lewdness * 0.1)     # Increase prey arousal


        elif predAction == "shake":
            actionCost = 40 + diffDamage * 3
            nausea = 2 + pred.aLev - (pred.con * 0.1)               # Calculate nausea recoil
            dis = 2.5 - (prey.con * 0.1)                            # Base disorientation for prey
            for prey in preyList:
                Dis = applyDis(pred.dis, dis)
                prey.addDis(Dis)                                    # Apply disorientation to prey
                if renpy.random.randint(1, 5) == 1:                 # 20% chance to apply damage
                    damage = pred.stren + diff - prey.con           # Calculate prey damage
                    prey.loseHp(max(0, damage))                     # Apply damage to prey

        elif predAction == "try to pleasure prey":
            actionCost = 10 + diffDamage * 2
            if target:
                dex = pred.dex * 0.5
                target.addArousal(dex * target.lewdness)            # Increase specific prey arousal
            else:
                dex = pred.dex * 0.1
                for prey in preyList:
                    prey.addArousal(dex * prey.lewdness)            # Increase arousal for all prey

        # End-of-action calculations for pred
        pred.loseStam(actionCost)                                   # Apply stamina cost to pred
        overflow = max((actionCost - pred.stam) * 0.1, 0)           # calculate stamina overflow
        pred.addDis(overflow / pred.con)                            # apply disOverflow
        renpy.say("debug", f"{overflow}")
        pred.addComp(applyDis(pred.dis, comp))                      # Apply Compression
        pred.acidRise()                                             # Increase stomach acid level


    return predAction

