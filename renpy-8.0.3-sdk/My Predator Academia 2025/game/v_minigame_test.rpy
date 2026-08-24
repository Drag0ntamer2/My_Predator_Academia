label digestionTesting:
    $ round = 1
    $ stomachPartners = [Yul]
    $ mealSize = Yul.size
    "Starting the digestion minigame test."
    "pick your pred"
    menu:
        "Sofie Moon":
            $ pred = Sof
            $ pred.reset()
            call stomachPartnerSelect
            call digestion_start(_return, Sof)
        "Leah Anagro":
            $ pred = Lea
            $ pred.reset()
            call stomachPartnerSelect
            call digestion_start(_return, Lea)
        "Lilly Oak":
            $ pred = Lil
            $ pred.reset()
            call stomachPartnerSelect
            call digestion_start(_return, Lil)
        "Yuliana Gomez (broken?)":
            $ pred = Yul
            $ pred.reset()
            call stomachPartnerSelect
            call digestion_start(_return, Yul)
        "quit":
            return
    jump digestionRound

label stomachPartnerSelect:
    "Chose stomach partners"
    menu:
        "Lilly Oak" if (pred != Lil) and not Lil in stomachPartners and pred.sSize >= mealSize + Lil.size:
            $ stomachPartners.append(Lil)
            $ mealSize += Lil.size
            $ Lil.reset()
            jump stomachPartnerSelect
        "Sofie Moon" if (pred != Sof) and not Sof in stomachPartners and pred.sSize >= mealSize + Sof.size:
            $ stomachPartners.append(Sof)
            $ mealSize += Sof.size
            $ Sof.reset()
            jump stomachPartnerSelect
        "Leah Anagro" if (pred != Lea) and not Lea in stomachPartners and pred.sSize >= mealSize + Lea.size:
            $ mealSize += Lea.size
            $ Lea.reset()
            $ stomachPartners.append(Lea)
            jump stomachPartnerSelect
        "Yuliana Gomez" if (pred != Yul) and not Yul in stomachPartners and pred.sSize >= mealSize + Yul.size:
            $ mealSize += Yul.size
            $ Yul.reset()
            $ stomachPartners.append(Yul)
            jump stomachPartnerSelect
        "That's all":
            return stomachPartners


label digestionRound:
    # Test loop
    while GameCheck():
        "Round [round]:"
        $ round += 1
        # Prey action selection
        #for prey in preyList:
        $ preyNum = 0
        while preyNum < len(preyList):
            $ prey = preyList[preyNum]
            $ preyName = prey.name
            call preyMoveSelection(prey, preyName)
            $ preyNum += 1
        jump predActionSelect

label preyMoveSelection(prey, preyName):
    "Choose [preyName]'s action:"
    menu:
        "Struggle":
            menu:
                "Light":
                    call prey_v_action(prey, "light struggle")
                    return
                "Moderate":
                    call prey_v_action(prey, "moderate struggle")
                    return
                "Aggressive":
                    call prey_v_action(prey, "aggressive struggle")
                    return
        "Rest":
            call prey_v_action(prey, "rest")
            return
        "Massage":
            call prey_v_action(prey, "massage")
            return
        "Brace":
            call prey_v_action(prey, "brace")
            return
        "Pleasure Self":
            call prey_v_action(prey, "Pleasure Self")
            return
        "Pleasure Pred":
            call prey_v_action(prey, "Try to pleasure pred")
            return
        "Interact With Stomach Partner" if len(preyList) > 1:
            menu:
                "Pleasure [preyList[0].name]" if not prey == preyList[0]:
                    call prey_v_action(prey, "Pleasure Fellow Prey", preyList[0])
                    return
                "Pleasure [preyList[1].name]" if not prey == preyList[1]:
                    call prey_v_action(prey, "Pleasure Fellow Prey", preyList[1])
                    return
                "Pleasure [preyList[2].name]" if (len(preyList) >= 3) and not (prey == preyList[2]):
                    call prey_v_action(prey, "Pleasure Fellow Prey", preyList[2])
                    return
                "Pleasure [preyList[3].name]" if (len(preyList) >= 4) and not (prey == preyList[3]):
                    call prey_v_action(prey, "Pleasure Fellow Prey", preyList[3])
                    return
label predActionSelect:
    #$ predAct = renpy.random.randint(1,5)
    #$ predAct = 5
    #if predAct == 1:
    #    call pred_v_action("squeeze", "digest")
    #elif predAct == 2:
    #    if pred.arousal < 35:
    #        call pred_v_action("crush", "digest")
    #    else:
    #        call pred_v_action("squeeze", "digest")
    #elif predAct == 3:
    #    call pred_v_action("massage", "digest")
    #elif predAct == 4:
    #    call pred_v_action("rest", "digest")
    #elif predAct == 5:
    #    call pred_v_action("shake", "digest")

    $ predAction = renpy.random.choice(["squeeze", "crush", "massage", "rest", "shake"])
    call pred_v_action(predAction, "digest")
    # call pred_v_action(pred.chooseAction(), "digest")
    
    # Check for end conditions
    if len(preyList) == 0:
        "Game Over"
        jump digestionTesting

    # Increment round counter and loop
    jump digestionRound

