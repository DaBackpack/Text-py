label dungeon1: 
    $expected = ["look", "think", "east", "north", "south", "west", "use", "help", "items", "take"]
    $pickup = ["key"]
    $room = "Dungeon: My Cell"
    $desc = "I awake to find myself in a barren dungeon cell. I'm probably underground, but I don't remember how I got here. Below me is a bed of dirt, surrounded by walls of solid steel. Since the area is completely sealed, my only lighting is from a mounted torch.\nThis isn't any place I recognize. Is there even a place like this IN Los Angeles?\n\n((Enter the 'help' command to find out all legal actions.))"
    $say()
    while True:
        e "> [inputv] [argument]{nw}"
        if inputv not in expected:
            call wait from _call_wait
        
        elif inputv == "west" or inputv == "north" or inputv == "south":
            $flush_input()
            call deadend from _call_deadend
        
        elif inputv == "east":
            $flush_input()
            $desc = "The door is sealed. I need to open it before I can leave."
            $say()
        elif inputv == "think":
            $think()
            $desc = "[think_message]"
            $say()
        elif inputv == "help":
            call help from _call_help
        elif inputv == "look":
            $flush_input()
            $desc = "I'm in a... brown?... dungeon cell. The room's only door, on the east wall, is locked shut, but there's a key on the floor. Why is it here? Do they want me to escape or something?"
            $say()
        elif inputv == "items":
            call inventory from _call_inventory
        elif inputv == "use":
            if argument == "leaflet":
                call leaflet_desc from _call_leaflet_desc
            elif argument == "key" and "key" in items:
                $flush_input()
                jump dungeon1_2
                
            else:
                call use_failed from _call_use_failed
        elif inputv == "take":
            call take from _call_take
            
    return
    
label dungeon1_2:
    $pickup = []
    $room = "Dungeon: My Cell"
    $desc =  "By sticking my key into the keyhole, the door opens."
    $say()
    while True:
        e "> [inputv] [argument]{nw}"
        if inputv not in expected:
            call wait from _call_wait_1
            
        elif inputv == "north" or inputv == "south" or inputv == "west":
            $flush_input()
            call deadend from _call_deadend_1
        elif inputv == "east":
            $flush_input()
            jump dungeon2
            
            
        elif inputv == "think":
            $think()
            $desc = "[think_message]"
            $say()
        elif inputv == "help":
            call help from _call_help_1
        elif inputv == "look":
            $desc = "The door to the cell is open. I can leave the cell by going east."
            $say()
        elif inputv == "items":
            call inventory from _call_inventory_1
        elif inputv == "use":
            if argument == "leaflet":
                call leaflet_desc from _call_leaflet_desc_1
            elif argument == "key" and "key" in items:
                $flush_input()
                $desc = "I just used the key. I don't need it anymore."
                $say()
            else:
                call use_failed from _call_use_failed_1
        elif inputv == "take":
            call take from _call_take_1
            
        elif inputv == "echo":
            $flush_input()
            $echo_smalltalk()
            
    return
    
label dungeon2:
    
    $small_fantasy_loss()
    $room = "Dungeon: Hallway (West End)"
    
    $desc = "There are other cells lining the parallel walls in this straight hallway.\nI have the feeling that I should leave this dungeon and reach the outside."
    $say()
    while True:
        e "> [inputv] [argument]{nw}"
        if inputv not in expected:
            call wait from _call_wait_2
            
            
        elif inputv == "east":
            $flush_input()
            jump dungeon3
        elif inputv == "west":
            $flush_input()
            jump dungeon1_2
        elif inputv == "north":
            $flush_input()
            jump cell2_north
        elif inputv == "south":
            $flush_input()
            jump cell2_south
            
        elif inputv == "think":
            $think()
            $desc = "[think_message]"
            $say()
        elif inputv == "help":
            call help from _call_help_2
        elif inputv == "look":
            $desc = "The hallway extends indefinitely to the east. Luckily there are mounted torches, aiding my vision. To the north and south of me are prison cells. It kinda stinks in here."
            $say()
        elif inputv == "items":
            call inventory from _call_inventory_2
        elif inputv == "use":
            if argument == "leaflet":
                call leaflet_desc from _call_leaflet_desc_2
            elif argument == "key" and "key" in items:
                $flush_input()
                $desc = "I just used the key. I don't need it anymore."
                $say()
            else:
                call use_failed from _call_use_failed_2
        elif inputv == "take":
            call take from _call_take_2
        
        elif inputv == "echo":
            $flush_input()
            $echo_smalltalk()
            
    return
    
label cell2_north:
    
    $room = "Dungeon: Empty Cell"
    
    $small_fantasy_loss()
    $desc = "I open the unlocked door to the northern cell. It's totally empty. It's like my cell, except without a cool person inside."
    $say()
    while True:
        e "> [inputv] [argument]{nw}"
        if inputv not in expected:
            call wait from _call_wait_3
            
            
        elif inputv == "east":
            $flush_input()
            call deadend from _call_deadend_2
        elif inputv == "west":
            $flush_input()
            call deadend from _call_deadend_3
        elif inputv == "north":
            $flush_input()
            call deadend from _call_deadend_4
        elif inputv == "south":
            $flush_input()
            jump dungeon2
            
        elif inputv == "think":
            $think()
            $desc = "[think_message]"
            $say()
        elif inputv == "help":
            call help from _call_help_3
        elif inputv == "look":
            $flush_input()
            $desc = "There's nothing really here. Actually, it would look kinda cool if you stuck a IBM PC setup here. Big brother and I could play without mom or dad bothering us."
            $say()
        elif inputv == "items":
            call inventory from _call_inventory_3
        elif inputv == "use":
            if argument == "leaflet":
                call leaflet_desc from _call_leaflet_desc_3
            elif argument == "key" and "key" in items:
                $flush_input()
                $desc = "I just used the key. I don't need it anymore."
                $say()
                
            else:
                call use_failed from _call_use_failed_3
        elif inputv == "take":
            call take from _call_take_3
            
        elif inputv == "echo":
            $flush_input()
            $echo_smalltalk()
            
    return
    
label cell2_south:
    $small_fantasy_loss()
    $room = "Dungeon: Barren Cell"
    $desc = "I open the unlocked door to the southern cell. There's nobody here. That includes imaginary people, too. Not that I still have any imaginary friends!!"
    $say()
    while True:
        e "> [inputv] [argument]{nw}"
        if inputv not in expected:
            call wait from _call_wait_4
            
            
        elif inputv == "east":
            $flush_input()
            call deadend from _call_deadend_5
        elif inputv == "west":
            $flush_input()
            call deadend from _call_deadend_6
        elif inputv == "north":
            $flush_input()
            jump dungeon2
        elif inputv == "south":
            $flush_input()
            call deadend from _call_deadend_7
            
        elif inputv == "think":
            $think()
            $desc = "[think_message]"
            $say()
        elif inputv == "help":
            call help from _call_help_4
        elif inputv == "look":
            $flush_input()
            $desc = "This room is the same as the one I woke up in. I should look elsewhere for more clues."
            $say()
        elif inputv == "items":
            call inventory from _call_inventory_4
        elif inputv == "use":
            if argument == "leaflet":
                call leaflet_desc from _call_leaflet_desc_4
            elif argument == "key" and "key" in items:
                $flush_input()
                $desc = "I just used the key. I don't need it anymore."
                $say()
                
            else:
                call use_failed from _call_use_failed_4
        elif inputv == "take":
            call take from _call_take_4
            
        elif inputv == "echo":
            $flush_input()
            $echo_smalltalk()
            
    return
label dungeon3:
    
    $room = "Dungeon: Hallway"
    $small_fantasy_loss()
    $desc = "I continue down the empty hallway. Again, there are two cells to my north and south."
    $say()
    while True:
        e "> [inputv] [argument]{nw}"
        if inputv not in expected:
            call wait from _call_wait_5
            
            
        elif inputv == "east":
            $flush_input()
            jump dungeon4
        elif inputv == "west":
            $flush_input()
            call dungeon2 from _call_dungeon2
        elif inputv == "north":
            $flush_input()
            jump cell3_north
        elif inputv == "south":
            $flush_input()
            if "echo" in items:
                jump cell3_south_last
            else:
                jump cell3_south_1
            
        elif inputv == "think":
            $think()
            $desc = "[think_message]"
            $say()
        elif inputv == "help":
            call help from _call_help_5
        elif inputv == "look":
            $flush_input()
            python:
                if "echo" not in expected:
                    desc = "The hallway extends east-to-west, with cells to the north and south.\nI hear a muffled sound from the near distance."
                    say()
                else:
                    desc = "The hallway extends east-to-west, with cells to the north and south."
                    say()
        elif inputv == "items":
            call inventory from _call_inventory_5
        elif inputv == "use":
            if argument == "leaflet":
                call leaflet_desc from _call_leaflet_desc_5
            elif argument == "key" and "key" in items:
                $flush_input()
                $desc = "I just used the key. I don't need it anymore."
                $say()
                
            else:
                call use_failed from _call_use_failed_5
        elif inputv == "take":
            call take from _call_take_5
            
        elif inputv == "echo":
            $flush_input()
            $echo_smalltalk()
            
    return    
    
    
label cell3_north:
    $room = "Dungeon: Grimy Room"
    $small_fantasy_loss()
    $desc = "I open the unlocked door to the northern cell. Why are there so many open cells here?"
    $say()
    while True:
        e "> [inputv] [argument]{nw}"
        if inputv not in expected:
            call wait from _call_wait_6
            
            
        elif inputv == "east":
            $flush_input()
            call deadend from _call_deadend_8
        elif inputv == "west":
            $flush_input()
            call deadend from _call_deadend_9
        elif inputv == "north":
            $flush_input()
            call deadend from _call_deadend_10
        elif inputv == "south":
            $flush_input()

            jump dungeon3
            
        elif inputv == "think":
            $think()
            $desc = "[think_message]"
            $say()
        elif inputv == "help":
            call help from _call_help_6
        elif inputv == "look":
            $flush_input()
            $desc = "An empty dungeon cell. This one is grimy for some reason. Going south will take me back to the hallway."
            $say()
        elif inputv == "items":
            call inventory from _call_inventory_6
        elif inputv == "use":
            if argument == "leaflet":
                call leaflet_desc from _call_leaflet_desc_6
            elif argument == "key" and "key" in items:
                $flush_input()
                $desc = "I just used the key. I don't need it anymore."
                $say()
                
            else:
                call use_failed from _call_use_failed_6
        elif inputv == "take":
            call take from _call_take_6
            
        elif inputv == "echo":
            $flush_input()
            $echo_smalltalk()
    return
    
label cell3_south_1:
    $room = "Dungeon: Noisy Room"
    $small_fantasy_loss()
    $desc = "I think there was a noise coming from this room. Slowly, I open the door and enter."
    $say()
    while True:
        e "> [inputv] [argument]{nw}"
        if inputv not in expected:
            call wait from _call_wait_7
            
            
        elif inputv == "east":
            $flush_input()
            call deadend from _call_deadend_11
        elif inputv == "west":
            $flush_input()
            call deadend from _call_deadend_12
        elif inputv == "north":
            $flush_input()
            $desc = "I should check this room out first."
            $say()
        elif inputv == "south":
            $flush_input()
            call deadend from _call_deadend_13
            
        elif inputv == "think":
            $think()
            $desc =  "[think_message]"
            $say()
        elif inputv == "help":
            call help from _call_help_7
        elif inputv == "look":
            $flush_input()
            jump cell3_south_2
        elif inputv == "items":
            call inventory from _call_inventory_7
        elif inputv == "use":
            if argument == "leaflet":
                call leaflet_desc from _call_leaflet_desc_7
            elif argument == "key" and "key" in items:
                $flush_input()
                $desc =  "I just used the key. I don't need it anymore."
                $say()
                
            else:
                call use_failed from _call_use_failed_7
        elif inputv == "take":
            call take from _call_take_7
            
            
    return

label cell3_south_2:
    $expected += ["talk"]
    $desc = "In the middle of the floor, hunched over on the ground, is a tiny winged creature. Is it a fairy or something?\nAs if to answer my question, the creature leaps off the ground and excitedly flies to my eye level. I should try to 'talk' to it."
    $say()
    while True:
        e "> [inputv] [argument]{nw}"
        if inputv not in expected:
            call wait from _call_wait_8
            
            
        elif inputv == "east":
            $flush_input()
            call deadend from _call_deadend_14
        elif inputv == "west":
            $flush_input()
            call deadend from _call_deadend_15
        elif inputv == "north":
            $flush_input()
            $desc = "I shouldn't leave yet."
            $say()
        elif inputv == "south":
            $flush_input()
            call deadend from _call_deadend_16
            
        elif inputv == "think":
            $think()
            $desc = "[think_message]"
            $say()
        elif inputv == "help":
            call help from _call_help_8
        elif inputv == "look":
            $flush_input()
            $desc = "This fairy is staring me right in the face. I should talk to her."
            $say()
        elif inputv == "talk":
            $flush_input()
            jump cell3_south_3
        elif inputv == "items":
            call inventory from _call_inventory_8
        elif inputv == "use":
            if argument == "leaflet":
                call leaflet_desc from _call_leaflet_desc_8
            elif argument == "key" and "key" in items:
                $flush_input()
                $desc = "I just used the key. I don't need it anymore."
                $say()
                
            else:
                call use_failed from _call_use_failed_8
        elif inputv == "take":
            call take from _call_take_8
            
    return
    
label cell3_south_3:
    $desc = "The fairy emotes excitedly. 'I'm so glad you found me! I was worried you would keep going and leave me behind...'\n'Are you a fairy?' I ask her. It looks like I'm actually in a real fantasy world!\n'Yes! My name's Echo,' she answers. What else does she have to say?"
    $say()
    while True:
        e "> [inputv] [argument]{nw}"
        if inputv not in expected:
            call wait from _call_wait_9
            
            
        elif inputv == "east":
            $flush_input()
            call deadend from _call_deadend_17
        elif inputv == "west":
            $flush_input()
            call deadend from _call_deadend_18
        elif inputv == "north":
            $flush_input()
            $desc = "I should keep looking around."
            $say()
        elif inputv == "south":
            $flush_input()
            call deadend from _call_deadend_19
            
        elif inputv == "think":
            $think()
            $desc = "[think_message]"
            $say()
        elif inputv == "help":
            call help from _call_help_9
        elif inputv == "look":
            $flush_input()
            $desc = "Let's keep talking to her."
            $say()
        elif inputv == "talk":
            $flush_input()
            jump cell3_south_4
        elif inputv == "items":
            call inventory from _call_inventory_9
        elif inputv == "use":
            if argument == "leaflet":
                call leaflet_desc from _call_leaflet_desc_9
            elif argument == "key" and "key" in items:
                $flush_input()
                $desc = "I just used the key. I don't need it anymore."
                $say()
                
            else:
                call use_failed from _call_use_failed_9
        elif inputv == "take":
            call take from _call_take_9
            
    return
    
label cell3_south_4:
    #$gain_fantasy(15)
    $room = "Dungeon: Not Noisy Room"
    $items += ["echo"]
    $expected += ["echo"]
    $expected.remove("talk")
    $desc = "'Nice to meet you,' I say. I have a lot of questions for her. 'So, uh, where exactly are we?'\n'We can talk as we go,' Echo says. 'We don't know when bad people will show up. Come on! I know the way out of here.'\n((The 'echo' command has been added! Use it to talk to Echo.))"
    $say()
    while True:
        e "> [inputv] [argument]{nw}"
        if inputv not in expected:
            call wait from _call_wait_10
            
            
        elif inputv == "east":
            $flush_input()
            call deadend from _call_deadend_20
        elif inputv == "west":
            $flush_input()
            call deadend from _call_deadend_21
        elif inputv == "north":
            $flush_input()
            jump dungeon3
        elif inputv == "south":
            $flush_input()
            call deadend from _call_deadend_22
            
        elif inputv == "think":
            $think()
            $desc = "[think_message]"
            $say()
        elif inputv == "help":
            call help from _call_help_10
        elif inputv == "look":
            $flush_input()
            $desc = "This is the room I found Echo in. The door was unlocked, but she probably doesn't have enough strength to open the door by herself. Why wasn't it locked, though? What if she was a strong fairy?"
            $say()
        elif inputv == "items":
            call inventory from _call_inventory_10
        elif inputv == "use":
            if argument == "leaflet":
                call leaflet_desc from _call_leaflet_desc_10
            elif argument == "key" and "key" in items:
                $flush_input()
                $desc = "I just used the key. I don't need it anymore."
                $say()
                
            else:
                call use_failed from _call_use_failed_10
        elif inputv == "take":
            call take from _call_take_10
            
        elif inputv == "echo":
            $flush_input()
            $echo_smalltalk()
            
    return
    
label cell3_south_last:
    $small_fantasy_loss()
    $room = "Dungeon: Not Noisy Room"
    $desc = "This is the room where I found Echo. What am I doing back here?"
    $say()
    while True:
        e "> [inputv] [argument]{nw}"
        if inputv not in expected:
            call wait from _call_wait_11
            
            
        elif inputv == "east":
            $flush_input()
            call deadend from _call_deadend_23
        elif inputv == "west":
            $flush_input()
            call deadend from _call_deadend_24
        elif inputv == "north":
            $flush_input()
            jump dungeon3
        elif inputv == "south":
            $flush_input()
            call deadend from _call_deadend_25
            
        elif inputv == "think":
            $think()
            $desc = "[think_message]"
            $say()
        elif inputv == "help":
            call help from _call_help_11
        elif inputv == "look":
            $flush_input()
            $desc = "I've done everything I need to here. Do I just enjoy wasting time? I need to go north."
            $say()
        elif inputv == "items":
            call inventory from _call_inventory_11
        elif inputv == "use":
            if argument == "leaflet":
                call leaflet_desc from _call_leaflet_desc_11
            elif argument == "key" and "key" in items:
                $flush_input()
                $desc = "I just used the key. I don't need it anymore."
                $say()
                
            else:
                call use_failed from _call_use_failed_11
        elif inputv == "take":
            call take from _call_take_11
            
        elif inputv == "echo":
            $flush_input()
            $echo_smalltalk()
            
    return
    
label dungeon4:
    $room = "Dungeon: Hallway (East End)"
    $small_fantasy_loss()
    $desc = "This is the end of the hallway. On the east wall is a door with a magic circle on it. I probably need magic to get through."
    $say()
    while True:
        e "> [inputv] [argument]{nw}"
        if inputv not in expected:
            call wait from _call_wait_12
            
            
        elif inputv == "east":
            $flush_input()
            $desc = "There's a magic door blocking my path."
            $say()
        elif inputv == "west":
            $flush_input()
            call dungeon3 from _call_dungeon3
        elif inputv == "north":
            $flush_input()
            call deadend from _call_deadend_26
        elif inputv == "south":
            $flush_input()
            call deadend from _call_deadend_27
            
        elif inputv == "think":
            $think()
            $desc = "[think_message]"
            $say()
        elif inputv == "help":
            call help from _call_help_12
        elif inputv == "look":
            $flush_input()
            python:
                if "echo" in items:
                    desc = "I can't get through this magic door by myself. Maybe Echo can help?"
                    say()
                else:
                    desc = "I don't think I can get through here right now. Maybe I need to keep looking around..."
                    say()
        elif inputv == "items":
            call inventory from _call_inventory_12
        elif inputv == "use":
            if argument == "leaflet":
                call leaflet_desc from _call_leaflet_desc_12
            elif argument == "key" and "key" in items:
                $flush_input()
                $desc = "I just used the key. I don't need it anymore."
                $say()
                
            else:
                call use_failed from _call_use_failed_12
        elif inputv == "take":
            call take from _call_take_12
            
        elif inputv == "echo":
            $flush_input()
            jump dungeon4_open
            
    return
    
label dungeon4_open:
    $room = "Dungeon: Hallway (East End)"
    $desc = "'Ah, a magic door!' Echo exclaims. 'Yes, we need to say the magic incantation to pass through! Lucky for you, I happen to know what it is.' Amazing...\n'The magic spell is...! 9913.'\nThat's a boring magic spell...\nWith that spell, the door magically opens in front of our eyes. Let's get out of here!"
    $say()
    while True:
        e "> [inputv] [argument]{nw}"
        if inputv not in expected:
            call wait from _call_wait_13
            
            
        elif inputv == "east":
            $flush_input()
            jump end_of_demo
        elif inputv == "west":
            $flush_input()
            $desc = "I don't want to turn around. The exit is right in front of me. Let's go!"
            $say()
        elif inputv == "north":
            $flush_input()
            call deadend from _call_deadend_28
        elif inputv == "south":
            $flush_input()
            call deadend from _call_deadend_29
            
        elif inputv == "think":
            $think()
            $desc = "[think_message]"
            $say()
        elif inputv == "help":
            call help from _call_help_13
        elif inputv == "look":
            $flush_input()
            $desc = "Echo opened the magic door for me. Let's go east!"
            $say()
        elif inputv == "items":
            call inventory from _call_inventory_13
        elif inputv == "use":
            if argument == "leaflet":
                call leaflet_desc from _call_leaflet_desc_13
            elif argument == "key" and "key" in items:
                $flush_input()
                $desc = "I just used the key. I don't need it anymore."
                $say()
                
            else:
                call use_failed from _call_use_failed_13
        elif inputv == "take":
            call take from _call_take_13
            
        elif inputv == "echo":
            $flush_input()
            $desc = "'We can chitchat later!' Echo exclaims. 'Let's get out of here!'"
            $say()
            
    return

label end_of_demo:
    $global hide_val
    $hide_val = True
    e "Echo and I walk through the open door. In front of us... lies more dungeon.\n'Hey, cheer up!' Echo squeaks. 'I know the way out of here. I think you'll be fine getting out of here!'\nI hope so... but I still want to find my big brother. I can't put my finger on it, but I think he's around here somewhere."
    e "I can't leave here without him."
    e "Absolutely not."
    e "I can't tell Echo, but I have to find him."
    e "He and I will find a way back home together and get to the bottom of this."
    e "<<End of demo! Thanks for playing. If I feel like it, I'll probably add on to this. I have the rest of the story planned out, but coding it is kind of tedious. Oh well, see you later!>>"
    return
    
label deadend:
    $flush_input()
    $desc = "Can't go that way."
    $say()
    return
    
    
label leaflet_desc:
    $flush_input()
    $desc = "I open the leaflet.\n'Welcome to 'Fantasy Adventure'! This is a game made by Chris Purdy for LMC6317. I used 'Colossal Cave Adventure' (by Will Crowther) and 'ZORK' (by Marc Leibling, et. al.) as references, and used royalty-free sound clips from SoundBible.com. I hope you enjoy! I'll probably add on to this later, but this should be a fine demo.'\n\nI haven't seen a more useless leaflet since big brother and I played ZORK together."
    $say()

    return
    
label reality:
    $room = "???"
    $global hide_val
    $hide_val = True
    e "I... I think I know what's going on."
    play sound "sound/slow_beat.wav" loop
    e "I'm not really here."
    e "Yeah." 
    e "None of this is real." 
    e "And if I think back to what led me here, I think I can remember."
    
    stop sound
    play sound "sound/fast_beat.wav" loop
    

    e ""
    e ""
    e "My head hurts but my mind is racing."
    e ""
    e "" 
    e "I need to leave." with flash
    e "I need to find big brother." with flash 
    e "---"
    e "As if by epiphany, memories erupt from the darkest corners of my mind. With them, a bloodcurdling scream from my mouth."
    e "Big brother told me not to scream, never to scream, but I can't listen to him now. I can't even if I wanted to."
    e "Everything here is bad." 
    e "I need to leave but I can't stop screaming."
    
    e ""
    
    stop sound
    play sound "sound/running.wav" loop
    e "---The sound of footsteps."
    e "They're coming. They hear me screaming. But I can't stop."
    e ""
    e "'I need to go.'" with flash
    
    e "That singular message rings in my head like an alarm. This place is bad."
    
    e ""
    e "The footsteps are getting closer."
    e "I'm probably going to die here."
    
    e "Somebody"
    e "          help me" with flash
    e "                  please" with flash
    stop sound
    play sound "sound/gunshot.wav"
    
    window hide 
    scene bg black with fade 
    $ renpy.pause(3.0)
    
    return