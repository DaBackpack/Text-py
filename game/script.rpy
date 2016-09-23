style my_text is text:
    size 16
    font "ufonts.com_terminal.ttf"
    color "#00cc00"

# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character(None, kind=nvl, what_style="my_text")

image bg black = "#000000"



# NVL configuration
      
      
init -2 python:
    
    global hide_val
    hide_val = False
    
    global fantasy
    fantasy = 100
    
    global inputv
    inputv = ""
    
    global items
    items = ["leaflet"]
    
    global think_message
    think_message = ""
    
    global pickup
    pickup = [""]
    
    global expected
    expected = []
    
    global argument
    argument = ""
    
    global smalltalkcounter
    smalltalkcounter = 0
    
    global desc
    desc = ""
    
    global append
    append = ""
    
    # An int describing which last fantasy threshold the warning was done at 
    global append_done
    append_done = 0
    
    global room
    room = ""
    
    global smalltalkarray1
    smalltalkarray1 = [
    "'So...' I ask Echo, 'where are we? I'm, uh, new around here.'\n'Why, we're in, uh...' she stutters. 'What was it called again? Oh, right: Ivalice!'\nSounds like a fantasy location, for sure. Wait, isn't that response kind of strange?\n'Well, to be specific, it looks like we're in a dungeon,' she adds.",    
    "'Can you tell me more about yourself?' I ask Echo.\n'I'm a pixie,' she answers. 'A fierce little ball of magical power!'\n Magical power? Was she summoned or something? I really need to learn the rules of this universe.",
    "'Is there anyone else in this dungeon?' I ask Echo. If my big brother is around here, I want to meet up with him as soon as possible.\n'Er, uh, no,' she returns. 'When I came here you were the only one held captive. I overheard the guards talking about it.'\nWell, maybe I should look anyway.",
    "'Why? Were you... looking for anyone?' Echo blushes.\n'Yeah, I had this feeling that my big brother might be around here, but I have no idea. If he's here, I really want to find him.'",
    "'I... don't think that's a good idea,' Echo says, sullenly. 'The guards around here will probably kill you if they find you. Our top priority should be getting out of here alive. We might be able to come back with help after we escape.'",
    "'Can you tell me about your big brother?' Echo asks me.\n'He's the coolest guy in the whole world. He's really smart, and funny, and lets me play video games with him. I love him so much. That's why I want to find him.'\nEcho looks really happy, but also emotional. Are those tears in her eyes?",
    "'We should keep going,' Echo says, wiping her eyes. I agree. As cool as it is to be in a fantasy videogame world, these guards sound really scary...",
    ]
    
    
init 0 python:
    

    config.nvl_list_length = 4

    # Game variables here... maybe find non-persistent way?

    
    
    renpy.image("red1", "#220000")
    renpy.image("red2", "#440000")
    renpy.image("red3", "#660000")
    renpy.image("red4", "#880000")
    renpy.image("red5", "#BB0000")
    renpy.image("red6", "#FF0000")
    
    flash = Fade(.25, 0, .75, color="#fff")
    
    
    
    menu = nvl_menu

    # The color of a menu choice when it isn't hovered.
    style.nvl_menu_choice.idle_color = "#ccccccff"

    # The color of a menu choice when it is hovered.
    style.nvl_menu_choice.hover_color = "#ffffffff"

    # The color of the background of a menu choice, when it isn't
    # hovered.
    style.nvl_menu_choice_button.idle_background = "#00000000"

    # The color of the background of a menu choice, when it is
    # hovered.
    style.nvl_menu_choice_button.hover_background = "#ff000044"

    # How far from the left menu choices should be indented.
    style.nvl_menu_choice_button.left_margin = 20


    #style.nvl_window.background = "nvl_window.png"
    style.nvl_window.xpadding = 55
    style.nvl_window.ypadding = 55

    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve
    
    config.say_attribute_transition = dissolve
    
    config.default_text_cps = 30

    config.window_auto_hide = [ 'scene', 'alma' ]
    
    def update_input(value=""): 
        global argument
        global inputv
        words = str.split(str(value))
        if len(words) == 0 or len(words) == 1:
            inputv = value
        if len(words) >= 2:
            inputv = words[0]
            argument = words[1]
        
        
    def flush_input():
        global inputv
        global argument
        inputv = ""
        argument = ""
        
    def change_background_color(fantasyval):
        global append
        append = fantasy_message()
        if fantasyval < 100 and fantasyval >= 80:
            renpy.scene()
            renpy.show("red1")
        
        if fantasyval < 80 and fantasyval >= 60:
            renpy.scene()
            renpy.show("red2")
            
        if fantasyval < 60 and fantasyval >= 40:
            renpy.scene()
            renpy.show("red3")
            
        if fantasyval < 40 and fantasyval >= 20:
            renpy.scene()
            renpy.show("red4")
        
        if fantasyval < 20 and fantasyval >= 0:
            renpy.scene()
            renpy.show("red5")
        
        if fantasyval < 0:
            renpy.scene()
            renpy.show("red6")
        
    def gain_fantasy(value):
        global fantasy 
        fantasy += value
        if fantasy > 100:
            fantasy = 100
        change_background_color(fantasy)
      
    def fantasy_message():
        global fantasy
        global append_done
        if fantasy <= 20:
            if append_done >= 7:
                return ""
            append_done = 7
            return "[[I can feel the jaws of 'reality' closing around me.]"
        if fantasy <= 40: 
            if append_done >= 5:
                return ""
            append_done = 5
            return "[[A wave of despair suddenly washes over my body as I step forward. Maybe I shouldn't dawdle anymore...]"
            
        if fantasy <= 60:
            if append_done >= 3:
                return ""
            append_done = 3
            return "[[I'm suddenly assaulted by a vision of another world.]"
        if fantasy < 80:
            if append_done >= 2:
                return ""
            append_done = 2
            return "[[Something bad might happen if I let the fantasy 'deteriorate', whatever that means. I shouldn't waste my time.]"
        if fantasy < 100:
            if append_done >= 1:
                return ""
            append_done = 1
            return "[[As I move, an ominous voice resounds in my mind: 'the fantasy is deteriorating.']"
        if fantasy == 100:
            append_done = 0
            return ""
        
        
    def small_fantasy_loss():
        global fantasy
        
        fantasy -=2
        
        
        change_background_color(fantasy)
        if fantasy <=0:
            renpy.jump("reality")
        return
        
    def say():
        global desc
        global append
        
        e(desc + "\n" + append)
        desc = ""
        append = ""
        
    
    def echo_smalltalk():
        flush_input()
        global smalltalkcounter
        if smalltalkcounter >= len(smalltalkarray1):
            e("We should keep going. I can talk to Echo later.")
            return
        e(smalltalkarray1[smalltalkcounter])
        smalltalkcounter += 1
        return
        
    def think():
        global fantasy
        global think_message 
        
        fantasy -= 15
        flush_input()
        # Game ends...
        
        change_background_color(fantasy)
        
        if fantasy < 100 and fantasy >= 80:
            think_message = "How exactly did I get here? I can't remember what led me to this world."
        if fantasy < 80 and fantasy >= 60:
            think_message = "Something about this isn't quite right...\n"
        if fantasy < 60 and fantasy >= 40:
            think_message = "Am I in another world, or am I just dreaming?\n"
        if fantasy < 40 and fantasy >= 20:
            think_message = "I'm not dreaming, but reality doesn't have magic and flying sprites...\n"
        if fantasy < 20 and fantasy > 0:    
            think_message = "This isn't real. That's because...\n"
        if fantasy <= 0:
            renpy.jump("reality")
    
# The game starts here.
label start:
    python:
        global fantasy
        fantasy = 100
        
        global inputv
        inputv = ""
        
        global items
        items = ["leaflet"]
        
        global think_message
        think_message = ""
        
        global pickup
        pickup = [""]
        
        global expected
        expected = []
        
        global argument
        argument = ""
        
        
    scene bg black
    jump dungeon1
    
    
label wait:
    if inputv == "":
        $flush_input()
        e "Please give a command."
        
    else:    
        $s = inputv
        $flush_input()
        e "You said '[s]'. Please supply a valid command. Enter 'help' for more information."
    return
    
    
label help:
    
    
    python:
        string = "Right now, I can do one of these: [expected]."
        flush_input()
        e(string)
    return
    
label inventory:
    $s = items
    $flush_input()
    e "I have [s] in my inventory right now."
    
    return 
    
label take:
    python:
        global items
        global pickup
        
        arg = argument
        flush_input()
        if arg == "":
            e("What am I taking?")
        elif arg not in pickup:
            e("There isn't a '[arg]' here.")
        elif arg in pickup:
            items += [arg]
            pickup.remove(arg)
            e("Added '[arg]' to inventory.")
            
        
    return
    
    
label use_failed:
    python:
        global argument
        global items
        
        if argument == "":
            flush_input()
            e("What am I using?")
        elif argument not in items:
            flush_input()
            e("I don't have that in my inventory. Are you thinking of another game?")
        elif argument in items:
            if argument == "echo":
                flush_input()
                e("A shrill voice from my side: 'Who are you callin' an item? You can't use me!'\nMaybe I should try 'echo'...")
            else:
                flush_input()
                e("I can't use that item right now.")

    return