# Game Title: Open
# New house, middle of nowhere, deathly silent, are the doors open?
# Psychological horror? Character "Silence" never saying anything and being
# an ominous background noise. Player waits for Silence as if it'll actually
# say something... And it might?

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene opening
    show player n

    # These display lines of dialogue.

    you "So... I'm finally here"
    "(You get out of the taxi and pull your bag out of the back)"
    "(An old house is before you, in the middle of nowhere, surrounded by a forest.)"
    "(A present... of sorts?...)"
    "(An inheritance from a very distant family member you never even met...)"
    "(You hear the taxi drive away back down the gravel road)"
    you "I should go inside before it gets too dark"

    # try front door
        # locked, check phone?
        # Thought the lawyers would be here... key is in back garden under a rock

# Door is locked, key is in the back garden under a rock, in an envelope, hidden by the lawyers
# who informed you of your new home
# QUESTION:
    "What do you do?"
    menu:
        "Try the front door":
            scene door
            silence "..."
            "(It's not open)"
#            play sound "audio/locked.mp3"
            "(You remember the lawyer saying something about a 'hide-a-key' somewhere...)"
            menu:
                "Go around to the back garden?":
                    jump backGarden

        "Go around to the back garden":
            jump backGarden


label backGarden:
    "(You go around the side of the house and open the gate)"
    # play sound "audio/gate.mp3"
    scene back
    "(The back garden is overgrown, dry, and cluttered)"
    "(You see a stone that looks a little uncanny next to the back door)"
    "(The lawyer mentioned something about a 'hide-a-key')"
    jump pickUpRock

label pickUpRock:
    "(It feels lighter than a rock and has a latch under it)"
    "(You open the latch)"
    # play sound "audio/keyJingle.mp3"
    "(A key drops out)"
    silence "..."
    you "Hello?"
    "(It feels more silent than before...)"
    "(You look around, seeing nothing, but noticing it is getting darker by the second)"
    you "I guess I should try the door?"
    # play sound "audio/keyLock.mp3"
    "(The lock clicks)"
    you "Ok..."
    "(You open the door with a tug and push it open)"
    "(A smell permiates the air as the seal on the door is broken and the inside air rushes out)"
    silence "..."
    you "...?"
    "(It's the kitchen)"
    jump kitchen

label kitchen:
    scene kitchen
    "(It's small, cramped, and cluttered with old plates, cups, and cutlery)"
    you "I guess nobody was left to clear this?"
    "What do you do?"
    menu:
        "Look around more":
            "(There's two ovens, a hob, a long counter top, a sink, and a door)"
        "Move some of the dishes to the sink":
            you "I should probably try to clean some of these if I'm going to live here..."
            silence "..."
            "(You place some of the dishes into the sink and try the tap)"
            "(It runs dark for a few seconds before spluttering to life with fresh, albeit freezing cold water)"
            "((rinse, scrub, rinse))"
            "(You washed some dishes)"

    "What do you do next?"
    menu:
        "Go to the door":
            "(You try to open the door and realise it's locked)"
            silence "..."
            you "Who locks their inside doors? We're in the middle of nowhere it's not like someone would be robbing the place"
            jump hallwayDoor

        "Make yourself a cup of tea":
            "(You rinse and fill the kettle up)"
            "(Pulling some teabags out of your bag, you place it into a rinsed cup)"
            silence "..."
            "(Pressing the button on the kettle you realise the power isn't on in the kitchen, maybe there's a fuse box somewhere?)"
            "(You decide to try the door near the hallway and realise it's locked)"
            you "Who locks their inside doors? We're in the middle of nowhere it's not like someone would be robbing the place"
            jump hallwayDoor

label hallwayDoor:
    scene hallwayDoor
    "(You look around the kitchen for a key or a hint of how to open the door in the hallway)"
    "(Noticing a key inside of a puzzle box, you take a good look at the puzzle)"
    jump puzzleBox

label puzzleBox:
    scene puzzleBox
    "what do you do?"
    menu:

        "Turn the middle piece":
            #play sound "audio/no.mp3"
            "(Nothing happens)"
            silence "..."
            jump puzzleBox

        "Turn the left piece":
            #play sound "audio/yes.mp3"
            "(It clicks)"
            silence "..."
            "(The key drops out)"
            "(You open the hallway door and step inside)"
            "(Again, a smell permiates the air as the seal on the door is broken and the inside air rushes out)"
            "(Before you is a hallway with an old carpet runner slung to the side)"
            jump hallway

        "Turn the right piece":
            #play sound "audio/no.mp3"
            "(Nothing happens.)"
            silence "..."
            jump puzzleBox

label hallway:
    "(The stairs to your right, and two separated rooms to your left)"

    "What do you do?"
    menu:
        "Go up the stairs":
            "(There's a weirdly shaped staircase with a 180 degree turn halfway up)"
            "(You're half expecting a locked door stopping you from going all the way up the stairs)"
            "(To your relief, there is none)"
            jump upstairsHallway

        "Go into Room 1":
            "(You walk to the first room and push on the door)"
            "(You let out a sigh)"
            you "Of course it is..."
            "(There's a keypad on the door handle with a note)"
            "(Never Eat Shredded Wheat)"
            you "What the?"
            silence "..."
            jump room1Lock

        "Go to Room 2":
            "(You walk to the second room and push on the door)"
            "(You let out a sigh)"
            you "Of course it is..."
            jump room2Lock

label upstairsHallway:
    "(There's four doors at the top of the stairs, one to the north, one east, one around the corner to the south, and one to the west)"
    "What do you do?"
    menu:
        "North":
            "(It's locked)"
            "(But there's a number on the door handle)"
            "(1)"
            jump upstairsHallway

        "East":
            "(It's locked)"
            "(But there's a number on the door handle)"
            "(3)"
            jump upstairsHallway

        "South":
            "(It's locked)"
            "(But there's a number on the door handle)"
            "(6)"
            jump upstairsHallway

        "West":
            "(It's locked)"
            "(But there's a number on the door handle)"
            "(2)"
            jump upstairsHallway

        "Go back down the stairs":
            jump hallway

label room1Lock: #1362
        you "Never Eat Shredded Wheat huh?"
        "What do you do?"
        menu:
            "Come back later":
                jump upstairsHallway
            "1":
                "(It clicks once)"
                jump room1Lock2
            "2":
                "(Nothing happens.)"
                jump room1Lock
            "3":
                "(Nothing happens.)"
                jump room1Lock
            "4":
                "(Nothing happens.)"
                jump room1Lock
            "5":
                "(Nothing happens.)"
                jump room1Lock
            "6":
                "(Nothing happens.)"
                jump room1Lock

label room1Lock2: #1362
        "What do you do?"
        menu:
            "Come back later":
                jump upstairsHallway
            "1":
                "(The lock resets)"
                jump room1Lock
            "2":
                "(The lock resets)"
                jump room1Lock
            "3":
                "(It clicks a second time)"
                jump room1Lock3
            "4":
                "(The lock resets)"
                jump room1Lock
            "5":
                "(The lock resets)"
                jump room1Lock
            "6":
                "(The lock resets)"
                jump room1Lock


label room1Lock3: #1362
        "What do you do?"
        menu:
            "Come back later":
                jump upstairsHallway
            "1":
                "(The lock resets)"
                jump room1Lock
            "2":
                "(The lock resets)"
                jump room1Lock
            "3":
                "(The lock resets)"
                jump room1Lock
            "4":
                "(The lock resets)"
                jump room1Lock
            "5":
                "(The lock resets)"
                jump room1Lock
            "6":
                "(It clicks a third time)"
                jump room1Lock4

label room1Lock4: #1362
        "What do you do?"
        menu:
            "Come back later":
                jump upstairsHallway
            "1":
                "(The lock resets)"
                jump room1Lock
            "2":
                "(The lock clicks open)"
                jump room1Open
            "3":
                "(The lock resets)"
                jump room1Lock
            "4":
                "(The lock resets)"
                jump room1Lock
            "5":
                "(The lock resets)"
                jump room1Lock
            "6":
                "(The lock resets)"
                jump room1Lock


label room1Open:
    "(The door opens)"
    "(A different smell permiates the air this time as the seal on the door
    is broken and the inside air rushes out)"
    silence "..."
    "(It takes a moment for your eyes to adjust, but you notice a beam of moonlight coming through a
    curtain on the other side)"

    "What do you do?"
    menu:
        "Open the curtains":
            "(You carefully walk through the boxes aand clutter to get to the curtains)"
            "(Opening the curtains, moonlight floods into the room)"
            scene openCurtainLivingRoom
            "(Revealing it's a living room, although the dust pile up implies nothing has been living here
            for quite some time)"

        "Try the lights":
            "(There's no power)"
            you "There has to be a fusebox somewhere..."
            silence "..."
            you "... hello?"
            "(The silence feels weighted, as you feel like someone is with you)"
            "(but there's no reason for why anyone else would be here)"
            "(It's probably just your imagination...)"
            "(To ease your mind you pull open the curtains to let some light inside)"
            scene openCurtainLivingRoom

    "(There's a lot of boxes, stuffed with the memories of that late family member you never met)"
    "(The walls are near barren, except for an oddly shaped ornament, illuminated by the light from the moon)"

    "What do you do?"
    menu:
        "Check the ornament on the wall":
            "(Keysssss)"

        "Look through the boxes":
            "(Toysssss)"




label room2Lock:
    "(There's a padlock on the door)"


    # This ends the game.

    return
