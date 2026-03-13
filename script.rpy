# Game Title: Open
# New house, middle of nowhere, deathly silent, are the doors open?
# Psychological horror? Character "Silence" never saying anything and being
# an ominous background noise. Player waits for Silence as if it'll actually
# say something... And it might?
# RE2 Police Station type puzzles for no reason, just like in RE2 lol

#############################
# Play through order
#############################
# Backdoor key
# Kitchen door
# Living room door
# Upstairs West door
# Upstairs South door
# Upstairs East door
# Upstairs North door
# Fusebox found and flipped
# Front door key found

# fusebox so lights on in game after flipped

###########################
# The game starts here.
###########################
label start:
    # The upstair doors
    default northkey = 0
    default eastkey = 0
    default southkey = 0
    default westKey = 0
    # Living room door
    default livingRoomOpen = 0
    # Front door
    default frontDoorKey = 0
    # fuse box
    default fusebox = 0
    # Cup of tea - Did you make a cup of tea before going to bed?
    default tea = 0
    # stairs - Have you been up the stairs once already? If so, don't play the same dialogue again
    default stairs = 0

# Front Door
    scene opening
    you "So... I'm finally here"
    "(You get out of the taxi and pull your bag out of the back)"
    "(An old house is before you, in the middle of nowhere, surrounded by a forest.)"
    "(A present... of sorts?...)"
    "(An inheritance from a very distant family member you never even met...)"
    "(You hear the taxi drive away back down the gravel road)"
    you "I should go inside before it gets too dark"

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
                "Check your phone":
                    "(The lawyer had text about a hide-a-key in the back garden by the back door)"
                    you "Guess I should try the back garden"
                    jump backGarden

        "Go around to the back garden":
            jump backGarden

# Back door unlock
label backGarden:
    "(You go around the side of the house and open the gate)"
    # play sound "audio/gate.mp3"
    scene backgarden
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

# Kitchen unlock
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
        "Go to the interior door":
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

label kitchen2:
    scene kitchen
    "(It's small, cramped, and cluttered with old plates, cups, and cutlery)"
    "What do you do?"
    menu:
        "Look around":
            "(There's two ovens, a hob, a long counter top, a sink, and a door)"
            jump kitchen2
        "Move some of the dishes to the sink":
            you "I should probably try to clean some of these if I'm going to live here..."
            silence "..."
            "(You place some of the dishes into the sink and try the tap)"
            "(It runs dark for a few seconds before spluttering to life with fresh, albeit freezing cold water)"
            "((rinse, scrub, rinse))"
            "(You washed some dishes)"
            jump kitchen2
        "Make yourself a cup of tea":
            "(You rinse and fill the kettle up)"
            "(Pulling some teabags out of your bag, you place it into a rinsed cup)"
            silence "..."
            if fusebox <= 0:
                "(Pressing the button on the kettle you realise the power isn't on in the kitchen, maybe there's a fuse box somewhere?)"
                "(You leave the kitchen again to search for a fusebox)"
                jump hallway
            elif fusebox >= 1:
                "(Pressing the button on the kettle causes a small hiss to start as the water boils)"
                you "Finally! I really needed a cup of tea right now"
                "(After half a minute it clicks, and the hot water is ready)"
                "(You make yourself a cup of tea, it looks delicious.)"
                you "I should find somewhere to relax and drink this"
                $ tea = tea +1
                jump hallway
        "Go back to the hallway":
            jump hallway

label hallwayDoor:
    scene kitchen
    "(You look around the kitchen for a key or a hint of how to open the door in the hallway)"
    scene keybox
    "(Noticing a key inside of a puzzle box, you take a good look at the puzzle)"
    jump puzzleBox

label puzzleBox:
    "what do you do?"
    menu:
        "Turn the right piece":
            #play sound "audio/no.mp3"
            "(Nothing happens.)"
            silence "..."
            jump puzzleBox

        "Turn the middle piece":
            #play sound "audio/yes.mp3"
            scene solvedbox
            "(It clicks)"
            silence "..."
            "(The key drops out)"
            scene emptybox
            "(You open the hallway door and step inside)"
            scene hallway
            "(Again, a smell permiates the air as the seal on the door is broken and the inside air rushes out)"
            "(Before you is a hallway, painted in blood-like reds and browns)"
            jump hallway

        "Turn the left piece":
            #play sound "audio/no.mp3"
            "(Nothing happens)"
            silence "..."
            jump puzzleBox


# Hallway open
label hallway:
    scene hallway
    "(The stairs are to your right, the kitchen is behind you, the front door and a living rooms are to your left)"

    "What do you do?"
    menu:
        "Go up the stairs":
            if stairs <= 0:
                "(There's a weirdly shaped staircase with a 180 degree turn at the start)"
                "(You're half expecting a locked door stopping you from going all the way up the stairs)"
                "(To your relief, there is none)"
                $ stairs = stairs +1
                jump upstairshallway
            elif stairs >= 1:
                jump upstairshallway

        "Go into the room":
            scene neswdoor
            if livingRoomOpen >= 1:
                jump livingroomopen
            elif livingRoomOpen <= 0:
                "(You walk to the door and push on it)"
                "(You let out a sigh)"
                you "Of course it is..."
                "(There's a keypad on the door handle with a note)"
                "(Never Eat Shredded Wheat)"
                you "What the?"
                silence "..."
                jump livingroomLock

        "Go to the front door":
            if frontDoorKey <= 0:
                scene frontdoor
                "(It's locked)"
                "(There's no sign of a key being anywhere near the key hooks by the door)"
                you "I wonder where the key is?"
                jump hallway
            elif frontDoorKey >= 1:
                scene frontdooropening
                "(The front door opens)"
                "(A cool air flows in, freshening up the damp, old smell that permiates the home)"
                you "Well at least I can use my own front door now..."
                "(You lock it back up and return to the hallway)"
                jump hallway

        "Go into the kitchen again":
            jump kitchen2

# North, East, South, West doors unlock
label upstairshallway:
    scene upstairshallway
    "(There's four doors at the top of the stairs, one to the north, one east, one around the corner to the south, and one to the west)"
    "What do you do?"
    menu:
        "North":
            if northkey >= 1:
                jump northOpen
            elif northkey <= 0:
                "(It's locked)"
                "(But there's a number on the door handle)"
                "(1)"
                jump upstairshallway

        "East":
            if eastkey >= 1:
                jump eastOpen
            elif eastkey <= 0:
                "(It's locked)"
                "(But there's a number on the door handle)"
                "(3)"
                jump upstairshallway

        "South":
            if southkey >= 1:
                jump southOpen
            elif southkey <= 0:
                "(It's locked)"
                "(But there's a number on the door handle)"
                "(6)"
                jump upstairshallway

        "West":
            if westKey >= 1:
                jump westOpen
            elif westKey <= 0:
                "(It's locked)"
                "(But there's a number on the door handle)"
                "(2)"
                jump upstairshallway

        "Go back down the stairs":
            jump hallway

# Living room door keypad lock
label livingroomLock: #1362
        you "Never Eat Shredded Wheat huh?"
        "What do you do?"
        menu:
            "Come back later":
                jump hallway
            "1":
                "(It clicks once)"
                jump livingroomLock2
            "2":
                "(Nothing happens.)"
                jump livingroomLock
            "3":
                "(Nothing happens.)"
                jump livingroomLock
            "4":
                "(Nothing happens.)"
                jump livingroomLock
            "5":
                "(Nothing happens.)"
                jump livingroomLock
            "6":
                "(Nothing happens.)"
                jump livingroomLock

label livingroomLock2: #1362
        "What do you do?"
        menu:
            "Come back later":
                jump hallway
            "1":
                "(The lock resets)"
                jump livingroomLock
            "2":
                "(The lock resets)"
                jump livingroomLock
            "3":
                "(It clicks a second time)"
                jump livingroomLock3
            "4":
                "(The lock resets)"
                jump livingroomLock
            "5":
                "(The lock resets)"
                jump livingroomLock
            "6":
                "(The lock resets)"
                jump livingroomLock


label livingroomLock3: #1362
        "What do you do?"
        menu:
            "Come back later":
                jump hallway
            "1":
                "(The lock resets)"
                jump livingroomLock
            "2":
                "(The lock resets)"
                jump livingroomLock
            "3":
                "(The lock resets)"
                jump livingroomLock
            "4":
                "(The lock resets)"
                jump livingroomLock
            "5":
                "(The lock resets)"
                jump livingroomLock
            "6":
                "(It clicks a third time)"
                jump livingroomLock4

label livingroomLock4: #1362
        "What do you do?"
        menu:
            "Come back later":
                jump hallway
            "1":
                "(The lock resets)"
                jump livingroomLock
            "2":
                "(The lock clicks open)"
                $ livingRoomOpen = livingRoomOpen +1
                jump livingroomopen
            "3":
                "(The lock resets)"
                jump livingroomLock
            "4":
                "(The lock resets)"
                jump livingroomLock
            "5":
                "(The lock resets)"
                jump livingroomLock
            "6":
                "(The lock resets)"
                jump livingroomLock

# Living room unlocked
label livingroomopen:
    scene livingroom
    if westKey <= 0:
        "(The living room door opens)"
        "(A different smell permiates the air this time as the seal on the door
        is broken and the inside air rushes out)"
        silence "..."
        "(It takes a moment for your eyes to adjust, but you notice a beam of moonlight coming through a
        curtain on the other side)"

        "What do you do?"
        menu:
            "Open the curtains":
                "(You carefully walk through the boxes and clutter to get to the curtains)"
                "(Opening the curtains, moonlight floods into the room)"
                scene opencurtainlivingroom
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
                    scene opencurtainlivingroom

        "(There's a lot of boxes, stuffed with the memories of that late family member you never met)"
        "(The walls are near barren, except for an oddly shaped ornament, illuminated by the light from the moon)"

        "What do you do?"
        menu:
            "Check the ornament on the wall":
                scene livingroomkey
                "(There's a weird contraption with a single key dangling from it)"
                "(There's a cowboy hat on a keyring and a label on the key saying 'The Wild ----')"
                "(the last word had been scratched off)"
                you "Is this a really simple *riddle* of sorts to open one of the doors upstairs
                or am I under thinking this?"
                $ westKey = westKey +1
                "(You pick up the key and decide to go back into the hallway)"
                jump hallway

            "Look through the boxes":
                "(There's a lot of cooking books, knitting patterns, bits of clutter, and some baby toys in the boxes)"
                silence "..."
                you "I heard they were alone when they died, I don't think they were married either..."
                you "Kind of why I got the house in the first place, there was no will and I'm the last person left in our bloodline"
                "(You close the boxes back up)"
                menu:
                    "Check the ornament on the wall":
                        scene livingroomkey
                        "(There's a weird contraption with a single key dangling from it)"
                        "(There's a cowboy hat on a keyring and a label on the key saying 'The Wild ----')"
                        "(the last word had been scratched off)"
                        you "Is this a really simple *riddle* of sorts to open one of the doors upstairs
                        or am I overthinking this?"
                        $ westKey = westKey +1
                        "(You pick up the key and decide to go back into the hallway)"
                        jump hallway

# If got west key but not north key game still going
    elif westKey >= 1:
        if northkey <= 0:
            "(There's a lot of boxes, stuffed with the memories of that late family member you never met)"
            "(The walls are near barren, except for an oddly shaped ornament, illuminated by the light from the moon)"
            "(You go back into the hallway)"
            jump hallway
        elif northkey >= 1:
            if fusebox >= 1:
                jump ending2
            elif fusebox <= 0:
                jump ending1

# North room - office/storage - Final upstair key received
label northOpen:
    scene northroom
    if fusebox <= 0:
        "(The inside air pours out as the seal on the door is broken)"
        you "An office room... or storage?"
        "(The room is filled with boxes, papers, exercise equiptment, a table, and a chair)"
        you "There's a fuse box...?"
        "(There's also what seems to be a fuse box on the wall)"

        "What do you do?"
        menu:
            "Flip the fuses":
                scene fusebox
                "(There's a key wedged into the fusebox)"
                menu:
                    "Remove the key":
                        scene fuseboxkeygone
                        "(The key pulls out with little force)"
                        you "Is this the front door key?"
                        $ frontDoorKey = frontDoorKey +1
                        you "At this point I'm not even going to ask..."
            "Go back to the hallway":
                you "I don't trust myself with fuse boxes"
                jump ending1
        menu:
            "Flip the fuses":
                scene fuseboxon
                "(You flip the switches and hear a hum of electricity.)"
                $ fusebox = fusebox +1
                "(A few old lamps and lights seem to turn on in the house)"
                "(With the electricity on you feel like getting ready for some sleep)"
                you "Hmm, I'm unsure if I want a cup of tea before bed or not..."
                "(You leave the north room and go back down stairs)"
        jump hallway
    elif fusebox >= 1:
        scene northroom
        "(The room is filled with boxes, papers, exercise equiptment, a table, and a chair)"
        "(There's nothing else in here, you return to the hallway)"
        jump hallway

# East room - bathroom - Third upstair key recieved
label eastOpen:
    if northkey <= 0:
        scene eastroom
        "(The inside air pours out as the seal on the door is broken)"
        "(An oddly laid out bathroom)"
        you "Wow, these fixtures will need redoing..."
        "What do you do?"
        menu:
            "Check the medicine cabinet":
                you "Another key?"
                "(A key with the North Star on it's keyring)"
                you "How'd you ever leave your house with the keys all locked in different rooms?"
                silence "..."
                you "...?"
                silence "..."
                "(You feel uneasy)"
                you "I was just talking out loud! Out loud to noone in particular!"
                you "Please don't let something answer me in the dark, I'm creeped out enough in here as it is"
                silence "..."
                "(You head back into the hallway)"
                $ northkey = northkey +1
                jump upstairshallway

            "Flush the toilet":
                "(The toilet flushes with a sputter, barely making a mark on the limescale that coats the inside of the bowl)"
                you "Gross..."
                you "Note to self to buy some toilet cleaner... and a brush..."
                "(You look at the toilet roll holder)"
                you "And toilet roll... I hope I don't need the toilet tonight"
                menu:
                    "Check the medicine cabinet":
                        you "Another key?"
                        "(A key with the North Star on it's keyring)"
                        you "How'd you ever leave your house with the keys all locked in different rooms?"
                        silence "..."
                        you "...?"
                        silence "..."
                        "(You feel uneasy)"
                        you "I was just talking out loud! Out loud to noone in particular!"
                        you "Please don't let something answer me in the dark, I'm creeped out enough in here as it is"
                        silence "..."
                        "(You head back into the hallway)"
                        $ northkey = northkey +1
                        jump upstairshallway
            "Go back to the hallway":
                jump upstairshallway

    elif northkey >= 1:
        scene eastroom
        "(An oddly laid out bathroom)"
        "(You thankfully do not need the toilet yet and there's nothing else in the bathroom that you need)"
        "(You decide to go back into the hallway)"
        jump upstairshallway

# South room - child's bedroom - Second upstair key recieved
label southOpen:
    if eastkey <= 0:
        "(The inside air does nothing as the seal on the door is broken)"
        "(It is deathly silent and it feels like there's no atmosphere at all)"
        silence "..."
        scene southroom
        you "It's a children's bedroom?"
        "(There's a room with a pristine cot, and toys arranged across a shelf)"
        "(A teddy bear with a key in it's ribbon sits on a rocking chair)"
        "(Although the chair looks to be usable and functioning, it doesn't budge, even with the movement from
        the floor boards as you walk through the room)"
        you "Abandoned child rooms are always creepy..."
        "(You untie the ribbon on the bear and pick up the key. The keyring has a rising sun on it.)"
        silence "..."
        "(You feel the hairs on the back of your neck raise)"
        you "Must be the win... well, must be the lack of wind... yeah..."
        "(You make your way back into the upstairs hallway)"
        $ eastkey = eastkey +1
        jump upstairshallway
    elif eastkey >= 1:
        scene southroom
        "(There's a room with a pristine cot, and toys arranged across a shelf)"
        "(There doesn't seem to be anything else to do in this room)"
        "(So you decide to go back into the hallway)"
        jump upstairshallway

# West room - master bedroom - First upstair key received
label westOpen:
    if southkey <=0:
        scene westroom
        "(Once again the inside air rushes out into the hallway as the seal on the door is broken open)"
        you "Huh... a bedroom?"
        "(The room is eluminated by the lack of curtains on the window, letting the moonlight pour inside)"
        "(Several wardrobes, some draws, and a single bed are all that reside here)"

        "What do you do?"
        menu:
            "Check the draws":
                "(They're suspiciously empty)"
                "(Clean too, not one bit of dust is inside of the draws)"
                you "Nope! Not today! Not going to try to think about why this is the
                only clean part of the entire house!"
                "(You close the draws and look around)"

                menu:
                    "Check the wardrobes?":
                        "(A coat hanger with a key hangs inside, it has a keyring from the South Pole on it)"
                        you "cute"
                        "(The rest of the wardrobes contents are filled with moth eaten clothing dating
                        back to the 50's and 60's)"
                        "(You sigh)"
                        you "These aren't my style but damn they would have been worth so much money
                        if they were intact"
                        "(You move the clothing aside and take off the key)"
                        $ southkey = southkey +1
                        jump upstairshallway

            "Check the wardrobes":
                "(A coat hanger with a key hangs inside it has a keyring from the South Pole on it)"
                you "cute"
                "(The rest of the wardrobes contents are filled with moth eaten clothing dating
                back to the 50's and 60's)"
                "(You sigh)"
                you "These aren't my style but damn they would have been worth so much money
                if they were intact"
                "(You move the clothing aside and take off the key)"
                $ southkey = southkey +1
                jump upstairshallway

            "Go back into the hallway":
                jump upstairshallway

    elif southkey >= 1:
        scene westroom
        "(The room is eluminated by the lack of curtains on the window, letting the moonlight pour inside)"
        "(Several wardrobes, some draws, and a single bed are all that reside here)"
        "(You already found everything you can in this room, so you decide to go back into the hallway)"
        jump upstairshallway

label ending1:
    scene ending1zz
    "(Ending One:)"
    "(You did not find the front door key, or restore the electricity)"
    "(With how dark it is outside, you lock the back door up again and
    pull out a sleeping bag)"
    "(Making a makeshift bed up on the living room floor)"
    silence "..."
    you "... huh?"
    "(You still feel like you're being watched...)"
    "(It's probably just your imagination because it's musty, damp, cold,
    and all of the lights are still off)"
    scene ending1z
    "(It takes some time, but you eventually fall asleep in your new home)"
    silence "..."
    "(Ending 1: Restless night)"

label ending2:
    if tea >= 1:
        scene ending1a
        "(You set up the sleeping bag on the floor of the living room and sip from your tea whiles watching the nature in the back garden)"
        "(Toads, newts, birds, and even a hedgehog can be seen. Living their lives in peace and harmony)"
        you "I think with a little work, I'm going to like it here..."
        "(You doze off peacefully)"
        silence "..."
        scene ending1aa

    elif tea <= 0:
        scene ending1b
        "(You set up the sleeping bag on the floor of the living room and watch the nature in the back garden)"
        "(Toads, newts, birds, and even a hedgehog can be seen. Living their lives in peace and harmony)"
        "(You're a little thirsty, maybe a cup of tea would have been nice?)"
        "(Alas, you're too sleepy to think about that now)"
        you "I think with a little work, I'm going to like it here..."
        "(You doze off peacefully)"
        silence "..."
        scene ending1bb

    "(Ending 2: Restful night)"
    # This ends the game.
    return
