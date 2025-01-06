# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define sof = Character("Sofie")
define jes = Char("Jessie")
define mer = Character("Merry")
define yul = Character("yuli")
define ash = Character("Ash")
define fel = Character("Felicity")

init python:
    # Define Jessie and Merry using the Char class
    jes = Char(
        name=["Jessie Avatar"],
        color="#ff0000",
        health=20,
        stam=15,
        strength=3,
        stomachHealth=0,
        acidStrength=0,
        stomachSize=0,
        size=1,
        acidResistance=2,
        acidFillRate=0,
        dexterity=8,
        constitution=5
    )

    mer = Char(
        name=["Merry Avatar"],
        color="#00ff00",
        health=25,
        stam=12,
        strength=5,
        stomachHealth=15,
        acidStrength=2,
        stomachSize=3,
        size=1,
        acidResistance=3,
        acidFillRate=0.3,
        dexterity=6,
        constitution=7
    )


default loop = 0


# The game starts here.

label start:
    jump digestionTesting
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    if loop == 0:
        # script for initial loop (before Return By Death has activated for the first time)
    elif loop == 1:
        # script for the first time Jessie resets his loop
        # may need to vary based on previous ending, revisit when multiple death-points exist
    else:
        # script for when Jessie

    menu:
        "Sleep In",
        "Find Phone & Scroll News",



    return
label digestionTesting:
    "Starting the digestion minigame test."

    $ round = 1
    # Reset states for the test
    $ jes.alive = True
    $ jes.inStomach = True
    $ jes.hp = jes.maxHp
    $ jes.stam = jes.maxStam
    $ jes.dis = 0

    $ mer.hp = mer.maxHp
    $ mer.stam = mer.maxStam
    $ mer.sComp = 0
    $ mer.aLev = 0

    # Test loop
    while jes.alive and jes.inStomach:
        "Round [round]:"
        # Display statuses
        "Jessie's HP: [jes.hp], Stamina: [jes.stam], Disorientation: [jes.dis]"
        "Merry's HP: [mer.hp], Stamina: [mer.stam], Stomach Compression: [mer.sComp], Acid Level: [mer.aLev]"

        # Prey action selection
        $ prey_action = renpy.input("Choose Jessie’s action (light, moderate, aggressive, rest, massage):", allow="light moderate aggressive rest massage").strip()
        if prey_action not in ["light", "moderate", "aggressive", "rest", "massage"]:
            $ prey_action = "rest"  # Default to rest if invalid input

        # Predator action selection
        $ pred_action = renpy.input("Choose Merry’s action (squeeze, crush, massage, rest, shake):", allow="squeeze crush massage rest shake").strip()
        if pred_action not in ["squeeze", "crush", "massage", "rest", "shake"]:
            $ pred_action = "rest"  # Default to rest if invalid input

        # Call digestion_round
        $ jes, mer = digestion_round(jes, mer, preyAction=prey_action, predAction=pred_action)

        # Check if Jessie has escaped or been digested
        if not jes.alive:
            "Jessie has been digested!"
        elif not jes.inStomach:
            "Jessie has escaped!"

        # Increment round counter
        $ round += 1

    return
