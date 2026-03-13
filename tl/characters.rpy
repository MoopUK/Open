# Script for any characters

#-----------------------------------------------------
################# Character List ####################
#-----------------------------------------------------

# Player / You
define you = Character("Player", color="#cf3476") # dark peach name tag

define silence = Character("Silence", color="#77878f") # slate grey name tag
#-----------------------------------------------------
################# Character Images ####################

#((NOT HAVING CHARACTER SPRITES DUE TO TIME CONSTRAINTS
# BUT IT WOULD HAVE LOOKED LIKE BELOW FOR NAMING CONVENTIONS))
# Instructions and tips on how to include sprites for people seeing this...

# Just have a characters folder in your game folder and add sprites there, then name them
# the same as below (eg: 'playern.png' with a neutral faced player character) to add them in game

# EG for in script.rpy to have a character on screne you just put:
# show playern
# And that'll show your player neutral face in middle, to add direction
# show player n at right
# show player n at left
# etc... for putting them to specific sides of the screen or with both next to each other
# you can have two people at once, like below:

# scene BackgroundImage
# show playerOne sad at right
# show playerTwo happy at left
# (Background image in background, Player One (sad face) at right of screen, Two (happy face) at left, and so on.

# sorry for ramble lol

################# Character Images ####################

# General expressions for characters:
# - neutral face
# - sad/crying
# - happy
# - angry
# - confused
# - embarrassed/shy

#------------------------------------------------------

# player (Player)
image player n:
    "playern"
    zoom 0.5 # zoom to resize image to correct proportions if it is
             # wrongly sized to game resolution or for resizing for
             # dramatic effect lol
image player sad:
    "playersad"
    zoom 0.5
image player happy:
    "playerhappy"
    zoom 0.5
image player angry:
    "playerangry"
    zoom 0.5
image player confused:
    "playerconfused"
    zoom 0.5
image player shy:
    "playershy"
    zoom 0.5
