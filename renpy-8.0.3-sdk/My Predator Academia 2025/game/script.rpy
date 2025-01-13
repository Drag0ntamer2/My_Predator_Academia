
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



# Images
image room = "images/base/bedroomday.jpg"



# Image style templates
transform fill_screen:
    xsize config.screen_width
    ysize config.screen_height








# The game starts here.

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene room at fill_screen with dissolve

    menu:
        "start game":
            jump Day1_start
        "test vore minigame":
            jump digestionTesting



    return
