
#### variables ###########################################################

default loop = 0


# Vore Minigame
default vore_active = False
default view = "outer"
default preyList = []
default pred = None
default predName = ""
default pred_action = "rest"
default prey_action = "rest"
default maxComp = 50
default predBars = [True, True, True, True, True]
default preyBars = [True, True, True, True]

# Sex Minigame
default sexParticipants = []
default player = Jes  # some sex scenes may be controling a different character
default sexPhase = "foreplay"
default sex_active = False
default sexBars = [True, True, False, True]

# Scene Specific Vars
# Day 1: 
# Jessie & Merry booby time in the morning
default Times_Played_With_Boobs = 0
default Jessie_Has_His_Wallet = False

# Image style templates
transform fill_screen:
    xsize config.screen_width
    ysize config.screen_height
transform center:
    xpos 0.5
    ypos 0.0
transform left:
    xpos 0.0
    ypos 0.0
transform right:
    xpos 0.75
    ypos 0.0
transform centerZoom5:
    xpos 0.5
    ypos 0.0
    zoom 5








# The game starts here.

label start:
    jump Day1_start
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    # show sofie smile at left
    # sof "testing"
    show jessie smile at right
    jes "testing"


    menu:
        "start game":
            jump Day1_start
        "test vore vore":
            jump digestionTesting



    return
