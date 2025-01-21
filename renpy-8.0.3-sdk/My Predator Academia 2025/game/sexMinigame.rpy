label sex_start(participant_list, Player = Jes, statBars = [ False, True, False, True, False ], objective = 'pleasure'):
    python:
        sexParticipants = participant_list                          # List of actor involved in the minigame
        player = player                                             # Single pred participating in the minigame
        playerName = player.name                                    # Store pred's name for display
        sex_active = True                                           # Flag to indicate minigame is active
        sexBars = statBars
        sexObjective = objective
        if not objective == 'pleasure':
            sexBars[0] = True
    return



label sex_action(actor, zone="lips", action="rest", target=None, sucChance = 5):
    $ name = actor.name                                          # Get actor's name for display

    "[name] used {b}[action]{/b}"                                       # reveal action used by actor

    python:
        diff = preferences.difficulty                                   # Game Difficulty
        actionCost = 0                                                  # Stores the cost, in stamina, of an action
        arousal = 0                                                     # Stores arousal to apply to pred's stomach
        actor.bracing = False                                           # stop bracing
        if not target: 
            target = actor
            selfAct = True
        else:
            selfAct = False


        success = renpy.random.randint(1,sucChance)

        if action in ['search'] and success == 1:
            progress = actor.dex
        else:
            progress = target.dex * -1
            
        
        if zone in [ "tits", "boobs" ] and target.sex == "female":
            actionCost = 15 + diff
            if action in ["search", 'find']: 
                arousal = 2.5
            elif action in ["caress", "kiss"]: 
                arousal = 5
            elif action in ["lick", "grope"]: 
                arousal = 6
            elif action in ["suck", "bite"]:
                arousal = 7
            elif action == "pump" and actor.boobjob: 
                arousal = 10
            elif action == "insert" and actor.sex == "male" and not selfAct:
                actor.boobJob = True
                actor.whoBoobs = target
                target.boobJob = True
                target.whoBoobs = actor
                arousal = 5
        elif zone in [ "lips" ]:
            actionCost = 15 + diff
            if action in ["kiss"]: 
                arousal = 5
            elif action in ["tongue kiss"]:
                arousal = 7
            elif action == "pump" and actor.blow: 
                arousal = 10
            elif action == "insert" and actor.sex == "male" and not selfAct:
                actor.blow = True
                actor.whoBlow = target
                target.blow = True
                target.whoBlow = actor
                arousal = 5
        elif zone in [ "pussy", "vag", "vagina", "penis", "cock", "dick"]:
            actionCost = 15 + diff
            if action in ["kiss", "stroke"]: 
                arousal = 5
            elif action in ['lick', "finger", "bite"]:
                arousal = 7
            elif action in ["pump", 'suck',"agressive stroke"] and actor.inside: 
                arousal = 10
            elif action == "insert" and actor.sex == "male" and not selfAct:
                actor.inside = True
                actor.whoInside = target
                target.inside = True
                target.whoInside = actor
                arousal = 5




        ##### End of Turn Calculations #####
        actor.loseStam(actionCost)                                      # apply stamina cost
        actor.addArousal((arousal * actor.lewdness * actor.dex) / 3)
        if not selfAct:
            target.addArousal((arousal * target.lewdness * actor.dex) / 3)
        target.addHp(progress)
            
    return action in ['search'] and success == 1
