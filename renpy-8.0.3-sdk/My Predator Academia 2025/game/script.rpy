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
        health=200,
        stam=150,
        strength=3,
        stomachHealth=0,
        acidStrength=0,
        stomachSize=0,
        size=1,
        acidResistance=2,
        acidFillRate=0,
        dexterity=8,
        constitution=5,
        oxygen=50,
        lewdness=4
    )
    mer = Char(
        name=["Merry Avatar"],
        color="#00ff00",
        health=250,
        stam=120,
        strength=5,
        stomachHealth=250,
        acidStrength=20,
        stomachSize=3,
        size=1,
        acidResistance=3,
        acidFillRate=0.05,
        dexterity=6,
        constitution=7,
        oxygen=50,
        lewdness=6
    )
    fel = Char(
        name=["Felicity Ferocity"],
        color="#99ff99",
        health=300,
        stam=170,
        strength=7,
        stomachHealth=400,
        acidStrength=15,
        stomachSize=3,
        size=0.85,
        acidResistance=1,
        acidFillRate=0.1,
        dexterity=10,
        constitution=12,
        oxygen=50,
        lewdness=1
    )
    ash = Char(
        name=["Ash Grigori"],
        color="#ff0000",
        health=300,
        stam=170,
        strength=7,
        stomachHealth=800,
        acidStrength=30,
        stomachSize=10,
        size=60,
        acidResistance=1,
        acidFillRate=0.5,
        dexterity=1,
        constitution=40,
        oxygen=300,
        lewdness=1
    )
    sof = Char(
        name=["Sofie Moon"],
        color="#9999ff",
        health=100,
        stam=170,
        strength=700,
        stomachHealth=150,
        acidStrength=13,
        stomachSize=3,
        size=1,
        acidResistance=1,
        acidFillRate=0.07,
        dexterity=6,
        constitution=4,
        oxygen=50,
        lewdness=3
    )


default loop = 0
default minigame_active = False
default digestion_active = False
default containment_active = False
default pleasure_active = False
default view = "outer"
default prey = None
default preyName = ""
default pred = None
default predName = ""
default pred_action = "rest"
default prey_action = "rest"

image room = "images/base/bedroomday.jpg"
image stomach = "images/base/stomach.jpg"
image roomButton = "images/tiny/bedroomday.jpg"
image stomachButton = "images/tiny/stomach.jpg"


transform fill_screen:
    xsize config.screen_width
    ysize config.screen_height








# The game starts here.

label start:
    scene room at fill_screen with dissolve
    jump digestionTesting
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #if loop == 0:
        # script for initial loop (before Return By Death has activated for the first time)
    #elif loop == 1:
        # script for the first time Jessie resets his loop
        # may need to vary based on previous ending, revisit when multiple death-points exist
   #else:
        # script for when Jessie

    #menu:
     #   "Sleep In",
     #   "Find Phone & Scroll News",



    return
label digestionTesting:
    "Starting the digestion minigame test."
    "pick your pred"
    menu:
        "Merry Avatar":
            call digestion_start(jes, mer)
        "Felicity Ferocity":
            call digestion_start(jes, fel)
        "Ash Grigori":
            call digestion_start(jes, ash)
        "Sofie Moon":
            call digestion_start(jes, sof)
        "quit":
            return
    jump initializeMinigameStats
label initializeMinigameStats:
    # Reset states for the test
    $ prey.alive = True
    $ prey.inStomach = True
    $ prey.hp = prey.maxHp
    $ prey.stam = prey.maxStam
    $ prey.dis = 0
    $ prey.arousal = 0

    $ pred.shp = pred.maxShp
    $ pred.stam = pred.maxStam
    $ pred.sComp = 0.01
    $ pred.aLev = 0
    $ pred.arousal = 0

    $ round = 1
label digestionRound:


    # Test loop
    while jes.alive and jes.inStomach:
        "Round [round]:"
        $ round += 1
        # Prey action selection
        "Choose Jessie's action:"
        menu:
            "Light struggle":
                call prey_vore_action("light struggle")
            "Moderate struggle":
                call prey_vore_action("moderate struggle")
            "Aggressive struggle" if prey.arousal < 35:
                call prey_vore_action("aggressive struggle")
            "Rest":
                call prey_vore_action("rest")
            "Massage":
                call prey_vore_action("massage")
            "quit":
                return
        jump predActionSelect

label predActionSelect:
    if not jes.inStomach:
        "Jessie has escaped!"
        jump digestionTesting
    $ predAct = renpy.random.randint(1,5)
    $ predAct = 4
    if predAct == 1:
        call pred_vore_action("squeeze")
    elif predAct == 2:
        if pred.arousal < 35:
            call pred_vore_action("crush")
        else:
            call pred_vore_action("squeeze")
    elif predAct == 3:
        call pred_vore_action("massage")
    elif predAct == 4:
        call pred_vore_action("rest")
    elif predAct == 5:
        call pred_vore_action("shake")


    # Check for end conditions
    if not jes.alive:
        "Jessie has been digested!"
        jump digestionTesting

    # Increment round counter and loop
    jump digestionRound

