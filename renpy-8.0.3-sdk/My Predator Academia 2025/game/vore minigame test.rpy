label digestionTesting:
    $ round = 1
    $ stomachPartners = [jes]
    $ mealSize = jes.size
    "Starting the digestion minigame test."
    "pick your pred"
    menu:
        "Sofie Moon":
            $ pred = sof
            $ pred.reset()
            call stomachPartnerSelect
            call digestion_start(_return, sof)
        "Leah Anagro":
            $ pred = lea
            $ pred.reset()
            call stomachPartnerSelect
            call digestion_start(_return, lea)
        "Lilly Oak":
            $ pred = lil
            $ pred.reset()
            call stomachPartnerSelect
            call digestion_start(_return, lil)
        "Yuliana Gomez":
            $ pred = yul
            $ pred.reset()
            call stomachPartnerSelect
            call digestion_start(_return, yul)
        "quit":
            return
    jump digestionRound

label stomachPartnerSelect:
    "Chose stomach partners"
    menu:
        "Lilly Oak" if (pred != lil) and not lil in stomachPartners and pred.sSize >= mealSize + lil.size:
            $ stomachPartners.append(lil)
            $ mealSize += lil.size
            $ lil.reset()
            jump stomachPartnerSelect
        "Sofie Moon" if (pred != sof) and not sof in stomachPartners and pred.sSize >= mealSize + sof.size:
            $ stomachPartners.append(sof)
            $ mealSize += sof.size
            $ sof.reset()
            jump stomachPartnerSelect
        "Leah Anagro" if (pred != lea) and not lea in stomachPartners and pred.sSize >= mealSize + lea.size:
            $ mealSize += lea.size
            $ lea.reset()
            $ stomachPartners.append(lea)
            jump stomachPartnerSelect
        "Yuliana Gomez" if (pred != yul) and not yul in stomachPartners and pred.sSize >= mealSize + yul.size:
            $ mealSize += yul.size
            $ yul.reset()
            $ stomachPartners.append(yul)
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
                    call prey_vore_action(prey, "light struggle")
                    return
                "Moderate":
                    call prey_vore_action(prey, "moderate struggle")
                    return
                "Aggressive":
                    call prey_vore_action(prey, "aggressive struggle")
                    return
        "Rest":
            call prey_vore_action(prey, "rest")
            return
        "Massage":
            call prey_vore_action(prey, "massage")
            return
        "Brace":
            call prey_vore_action(prey, "brace")
            return
        "Pleasure Self":
            call prey_vore_action(prey, "Pleasure Self")
            return
        "Pleasure Pred":
            call prey_vore_action(prey, "Try to pleasure pred")
            return
        "Interact With Stomach Partner" if len(preyList) > 1:
            menu:
                "Pleasure [preyList[0].name]" if not prey == preyList[0]:
                    call prey_vore_action(prey, "Pleasure Fellow Prey", preyList[0])
                    return
                "Pleasure [preyList[1].name]" if not prey == preyList[1]:
                    call prey_vore_action(prey, "Pleasure Fellow Prey", preyList[1])
                    return
                "Pleasure [preyList[2].name]" if (len(preyList) >= 3) and not (prey == preyList[2]):
                    call prey_vore_action(prey, "Pleasure Fellow Prey", preyList[2])
                    return
                "Pleasure [preyList[3].name]" if (len(preyList) >= 4) and not (prey == preyList[3]):
                    call prey_vore_action(prey, "Pleasure Fellow Prey", preyList[3])
                    return
label predActionSelect:
    #$ predAct = renpy.random.randint(1,5)
    #$ predAct = 5
    #if predAct == 1:
    #    call pred_vore_action("squeeze", "digest")
    #elif predAct == 2:
    #    if pred.arousal < 35:
    #        call pred_vore_action("crush", "digest")
    #    else:
    #        call pred_vore_action("squeeze", "digest")
    #elif predAct == 3:
    #    call pred_vore_action("massage", "digest")
    #elif predAct == 4:
    #    call pred_vore_action("rest", "digest")
    #elif predAct == 5:
    #    call pred_vore_action("shake", "digest")

    call pred_vore_action(pred.chooseAction(), "digest")

    # Check for end conditions
    if len(preyList) == 0:
        "Game Over"
        jump digestionTesting

    # Increment round counter and loop
    jump digestionRound

