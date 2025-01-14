
#### variables ###########################################################

default loop = 0

# Vore Minigame
default minigame_active = False
default view = "outer"
default preyList = []
default pred = None
default predName = ""
default pred_action = "rest"
default prey_action = "rest"
default maxComp = 50





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








# The game starts here.

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene room at fill_screen with dissolve
    show sofie smile at left
    sof "testing"
    show jessie smile at right
    jes "testing"


    menu:
        "start game":
            jump Day1_start
        "test vore minigame":
            jump digestionTesting



    return
