import random
import time




#all the lists and class necessary to run the game follow
#list to contain all the transition texts
trans1 = ["That was harrowing. You take a moment to regain your composure. Behind you stretches only darkness, with no way back. You can hear the dragging of the creature's feet, and it's closer than you'd like. ",
"You take a moment to catch your breath. From behind you, you can hear muffled sounds. You are still being followed! A long corridor stretches before you, with a solitary exit at the end. You must keep moving. ",
"When will this nightmare end? What did you do to get here? Was it because you nicked Tommy Hardman's lollipop in Year 3 and blamed Sally Jones? No time for ruminations, you can feel the monster drawing ever closer. You are in a narrow passage, and you run towards the exit ahead", 
"Yet another passage materialises before you. You're getting tired. You run on, with both fear and frustration growing.",
]

#creating a list with all the different room descriptions
rooms = ["You enter a large room, sparsely lit by spluttering torches. There's a mosaic on the wall. A person is fleeing an indistinct horror, all the more disturbing for its vagueness. There are only three ways out of the room: ", 
"Ahead, you make out an ornate iron door. It resists your attempts to open it. You take a few steps back, and then rush forward to barge the door. The door swings open, protesting hinges squealing. Three options are before you: ", 
"You enter what looks like a stone room with lit with braziers. Before you can survey the chamber, the door slams shut behind you. A blood-curdling roar breaks the ominous silence. The door behind you shakes, pounded on by the creature. Suddenly the room bursts to life as the braziers come to life, with a giant one in the centre of the room. There are only three ways out.", 
"You feel the walls either side of you give way into open space. The earthy smell and the damp warmth of the chamber are noticeable. Unable to see far in the gloom, you pause to listen. Nothing, but your own ragged breathing. Upon closer inspection, another three choices present themselves."
]


#creating a class to contain all the phobias and their values. Manifestations contained in a list
class Phobia:
    def __init__(self, name, manifestation1, manifestation2, manifestation3, manifestation4, vision, fatality, nonthreatening, art):
        self.name = name
        #create a list to contain all the manifestations attributes, so we can pick from them at random
        self.manifestations = [manifestation1, manifestation2, manifestation3, manifestation4]
        self.vision = vision
        self.fatality = fatality
        self.nonthreatening = nonthreatening
        self.art = art



    #function to print out clean text
    def __repr__(self):
        return self.name



    #declaring items for the class Phobia and populating the attributes
claustrophobia = Phobia("Claustrophobia",
"A coffin lies in the middle of the room. Your curiosity outweighs your fear, and you slowly approach the coffin. You remove the lid, to find the coffin empty. Is it meant for you? There is a rumbling above you, and dirt begins to pour from the ceiling. You must either jump in, or dash for one of the other exits, quickly!",
"A small hole in the floor provides hope of escape. You realise that you need to hunch your shoulders to fit in, and it seems to get narrower yet. You may be able to squeeze yourself through, but with little hope of return. Do you proceed?",
"You try the door leading away from the creature, but it’s locked. To your right is a small alcove with an iron key lying at the end. Reaching your hand inside this passage, you feel the strangest sensation, as if your muscles are trapped beneath your skin. You begin to panic. Do you push through?",
"You enter through the small door, hoping to find an easy way out. It slams shut behind you, and you hear the rusty squeal of old cogs beginning to turn nearby. With a rumble, all four walls start to inexorably move in towards you. An open passageway at the end of the chamber is slowly closing. Will you sprint towards the passageway, and hope you don't get crushed?",
"You focus on the vision covering the exit: It's you, trapped in a corridor. The roof behind you collapses. Your only hope of escape lies in front of you, a small hole bored into the rock. You enter the hole, and it slowly closes around you, burying you alive. You can feel the earth around you even as you're watching the vision unfold. Is this the best exit?",
"You cannot move, and breathing is becoming more difficult. You realise that there will be no escape, this will be your tomb. As you start to lose consciousness, you hear a childlike giggling close by…",
"a tiny box", 
"""
_________________________
|\ _____________________ /|
| |_____________________| |
|/_______________________\|
/=========================\'
===========================
|  ~~       _|_        ~~ |
|            |            |
|_________________________|
"""
)
spiders = Phobia("spiders",
"This exit leads to a dimly-lit room. You step forward, only to be covered in a giant web. You flail frantically as you plunge forward through more webbing. The silent room erupts in malignant chittering, and something large lands on your back. Will you face the beast or run to another exit?",
"You inspect the small opening to a cavern. Something warns you to look up. Just above you is a writhing mass. Under the opalescent light, it morphs into several distinct shapes. Giant red reflective eyes study you. The nearest furry leg is inches away from your head, and your path is blocked by gigantic webs. Use the torch or run? ",
"This exit is a stone arch. Stepping inside, you see there is an occupant standing between you and escape. Shelob's bigger cousin is hungrily watching you. Will you run between its legs and hope for the best?",
"A small cavern offers a way out. You linger at the entrance. Between you and the exit lie hundreds of large spider eggs. You brush lightly against one, waking its occupant. As the spider starts to twitch, the eggs around it also start to pulsate. Will you hurry as quickly (and as quietly) to the other side as possible?",
"You see a vision of yourself before you, in a tight box. There is but one hole, on top. Through it crawls a stream of tarantulas. Your new friends are making themselves at home in your hair, pockets and clothes. Even though it's a vision, you can feel them crawling everywhere. Will you pick this route?",
"You are in a well, filling with spiders. Small, big, venomous, gigantic. There's no way out, just you and your eight-legged friends. Your own personalised hell. ",
"a giant, fluffy spider",
    """
░░░░░░░░░░░║
░░▄█▀▄░░░░░║░░░░░░▄▀▄▄
░░░░░░▀▄░░░║░░░░▄▀
░▄▄▄░░░░█▄▄▄▄▄▄█░░░░▄▄▄
▀░░░▀█░█▀░░▐▌░░▀█░█▀░░░▀
░░░░░░██░░▀▐▌▀░░██
░▄█▀▀▀████████████▀▀▀█
█░░░░░░██████████░░░░░▀▄
█▄░░░█▀░░▀▀▀▀▀▀░░▀█░░░▄█
░▀█░░░█░░░░░░░░░░█░░░█▀

"""
)

fire = Phobia("fire",
"You approach this unassuming door. As you reach for the handle, you are buffeted back by flames erupting around the door. The heat is intense, and you’re finding it impossible to breathe. You realise with horror that the flames are slowly creeping towards you. WIll you attempt to cross them?",
"The wooden door grabs your eye. You grasp the bronze knob, but you recoil immediately. It's hot, and a rush of flames almost envelops you. You can just about make a path through the passage. Will you make your way through?",
"What fresh hell is this? The passage is coated in blue flames. You reach out and touch a wall, and draw it back quickly. The pain was excruciating, but there is no sign of damage. You can cross, but you'll feel like you're being burnt alive. Will you do it?",
"You examine this exit keenly, because it seems safe. The sudden, overwhelming stench of petrol causes you to gag. A small flame appears on the roof of the chamber, and then more still. The flames start to fall, a rain of fire through which you must pass. Will you brave the passage?",
"This vision is of a person, engulfed by flames on a stake. You look closer, that person is you. You think you can feel the flames already.  Will you pick this exit?",
"You are submerged in a pit of flames. They burn you to the core, yet they do not kill you. You scream, but nobody hears you. You are condemned to an eternity of hellfire ",
"a flame, followed by a puff of smoke",
"""
@@@@@@@@@@@@@@@@@@@(@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@((((@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@((@(@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@&&((((((@@@@@@@@@@@@@@@@
@@@@@@@@@@@(@((((%(#(((@@@@@@@@@@@@@@@
@@@@@@@@@@@@(&((%%%%%#(#@@@@@@@@@@@@@@
@@@@@@@@@@@@###%%%%%%###@@@@@@@@@@@@@@
@@@@@@@@@@@@#%#%%%@%@%@#@#@@@@@@@@@@@@
@@@@@@@@@####&%&%&&&&&%&###@@@@@@@@@@@
@@@@@@@@@@###&&&&&&&&&&&&##@@@@@@@@@@@
@@@@@@@@@@&%&&&&&&&&&&&&&%@@@@@@@@@@@@
@@@@@@@@@@@@%&&&&&&&&&&&&%@@@@@@@@@@@@
@@@@@@@@@@@@@@%&&&&&&&&%@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
""") 


blood = Phobia("blood",
"You examine this antechamber. You notice a sharp metallic tang in the air. You realise that the wall closest to you seems to be moving. You reach out and touch the wall. Your hand is coated in gore. Looking down, you find a slowly rising crimson tide, pulsing to the beat of a monstrous heart. Is this the best exit to take?",
"Before you lies a table. On it, a golden chalice contains a steaming liquid. The implication is clear, you must drink it. You notice that the chalice is still being filled from above. Above you, a bucket of blood is dripping into the cup. Will you pick it up and drink? ",
"This exit opens out to a cavern. There's a small lake before you. You're clearly meant to swim across, but this is no water as the fluid is viscous and red. Will you swim through the blood?",
"This door has writing etched on it: 'Offer what's most precious and you shall receive passage'. In front of the door there's a simple bronze receptacle and a silver knife, laid on top. You pick the knife up considering the blood sacrifice. Will you do it?",
"You see yourself, surrounded by needles in a sarcophagus. Each time you move one of them stabs you, drawing blood. Is this the best exit?",
"You are alone, immobilised by an overwhelming force. A sharp pain causes you to look at your finger. A tiny drop of blood is emerging. Another on your arm, and then your leg. Tiny rivulets of blood. This is death by a thousand paper cuts.",
"a vial of blood",
"""

    @
    @(@
    @((((@
    @((@(@
   @&&((((((@
  @@#%#%%%@%@%@
  @###&%&&&&##@
  @###&&&&&&##@
  @&%&&&&&&&%@
   @%&&&&&%@
     @&&@

"""
)

dark = Phobia("dark", 
"This exit is an entrance to a cave. The closer you get, the darker it becomes. The inky blackness is unrelenting and no light seems to penetrate it. Will you face the dark? ", 
"In the middle of the room stands a well. Upon closer inspection, you see there are steps descending downwards, but no light touches them. This way, you will be at the mercy of whatever lurks in the darkness. Can you brave it? ", 
"Before you stands a swirling black column. You move to go around it, but it moves forward at speed and envelopes you. Drained of positive emotions, you feel as if there is no point in going on. Focus what little willpower you have left and push through?", 
"The passage is exactly your height, and strangely shaped like you. You can only pass through with your arms to your side, blocking out the light. The dark is tangible, like a void. Will you brave the darkness, or pick another?",
"The sense of malice and foreboding here is almost overwhelming. The torch sputters and dies as the darkness consumes it. You can see nothing, and sound is curiously muted. Feel your way through?",
"You have been stumbling around in the darkness for almost a week. The whispering voices refuse to leave you. Without foor and water, you are close to collapse. You realise that you can go no further, and slump to your knees in defeat.",
"endless, unforgiving darkness",
"""
   ,,;;;;;,,
 ,;;:::::::;;,
,;;::' , ':::;,
;;::  /(   ::;;
;;:: |  \  ::;;
';;::.\c/.::;;'
 ';:::'-,:::;'
   '';| |;''
      '-,
      | |
      '-,
      | |
      '-,
      | |
      '-,
      | |
     /`"`\'
  .-'.  _.'-.
 `._  `    _.'
    `"---"`
"""
)

heights = Phobia("heights",
"Before you lies a pit, so deep there is no sign of the bottom. You can see an open door on the other side of the pit. Between you and salvation are several small platforms, balanced precariously on crumbling pillars. Should you attempt to cross?",
"The ground gives way beneath your feet, and you find yourself staring into an abyss. You can just about make out a narrow string of stone, uniting your bank with the other side of the darkness. You will be balancing over unknown depths, at the mercy of gravity. Will you overcome the vertigo and push on?",
"This passage opens into an abyss. As you eyes get used to the crepuscular light, you notice you're standing on a narrow parapet, extending left and right. And though there's no way across the void, you can edge along, back-on-wall, to the welcoming light of another doorway, to your right. Will you walk across this hair's breadth or choose another way out?",
"This door opens into a parapet. There's no bridge, nor crossing. The only way is down. Will you overcome the vertigo and jump?",
"You turn your eyes to this vision -- so simple, yet so terrifying. It's a hole into the abyss. In the distance you can make out a dot, and hear a small voice. That voice is yours. Will you pick darkness?",
"The floor that you are standing on begins to crumble. You jump, but there is nowhere safe to land. As you fall, you twist in the air just in time to glimpse the rusted iron spikes pertruding from the floor below.",
"a nauseating view from above",
"""
    ^^      ..                                       ..
            []                                       []
          .:[]:_          ^^                       ,:[]:.
        .: :[]: :-.                             ,-: :[]: :.
      .: : :[]: : :`._                       ,.': : :[]: : :.
    .: : : :[]: : : : :-._               _,-: : : : :[]: : : :.
_..: : : : :[]: : : : : : :-._________.-: : : : : : :[]: : : : :-._
_:_:_:_:_:_:[]:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:[]:_:_:_:_:_:_
!!!!!!!!!!!![]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!![]!!!!!!!!!!!!!
^^^^^^^^^^^^[]^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^[]^^^^^^^^^^^^^
            []                                       []
            []                                       []
            []                                       []
 ~~^-~^_~^~/  \~^-~^~_~^-~_^~-^~_^~~-^~_~^~-~_~-^~_^/  \~^-~_~^-~~-
~ _~~- ~^-^~-^~~- ^~_^-^~~_ -~^_ -~_-~~^- _~~_~-^_ ~^-^~~-_^-~ ~^
   ~ ^- _~~_-  ~~ _ ~  ^~  - ~~^ _ -  ^~-  ~ _  ~~^  - ~_   - ~^_~
     ~-  ^_  ~^ -  ^~ _ - ~^~ _   _~^~-  _ ~~^ - _ ~ - _ ~~^ -
        ~^ -_ ~^^ -_ ~ _ - _ ~^~-  _~ -_   ~- _ ~^ _ -  ~ ^-
            ~^~ - _ ^ - ~~~ _ - _ ~-^ ~ __- ~_ - ~  ~^_-
                ~ ~- ^~ -  ~^ -  ~ ^~ - ~~  ^~ - ~
"""
)

#populating a list with all the items from the class Phobia
phobias_l = [claustrophobia, spiders,fire, blood, dark, heights]
def makeacopiedlist():
#function ot create a fresh list populated by phobia attributes. Necessary for replaying the game
    global phobias_list
    phobias_list = phobias_l.copy()
    return phobias_list



def printcorridor():
    #a function to print name and initial art
    print("""\n
     ▄███████▄    ▄█    █▄     ▄██████▄  ▀█████████▄   ▄██████▄     ▄████████ 
    ███    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███ 
    ███    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    █▀  
    ███    ███  ▄███▄▄▄▄███▄▄ ███    ███  ▄███▄▄▄██▀  ███    ███   ███        
  ▀█████████▀  ▀▀███▀▀▀▀███▀  ███    ███ ▀▀███▀▀▀██▄  ███    ███ ▀███████████ 
    ███          ███    ███   ███    ███   ███    ██▄ ███    ███          ███ 
    ███          ███    ███   ███    ███   ███    ███ ███    ███    ▄█    ███ 
    ▄████▀        ███    █▀     ▀██████▀  ▄█████████▀   ▀██████▀   ▄████████▀  
                                                                                
                                                                                """)
                                                                        
    time.sleep(1)


    print("""
    \n\n
    _    __      __       _     _        ___                               ___             _         _   _          
   /_\   \ \    / /__ _ _| |__ (_)_ _   | _ \_ _ ___  __ _ _ _ ___ ______ | _ \_ _ ___  __| |_  _ __| |_(_)___ _ _  
  / _ \   \ \/\/ / _ \ '_| / / | | ' \  |  _/ '_/ _ \/ _` | '_/ -_|_-<_-< |  _/ '_/ _ \/ _` | || / _|  _| / _ \ ' \ 
 /_/ \_\   \_/\_/\___/_| |_\_\ |_|_||_| |_| |_| \___/\__, |_| \___/__/__/ |_| |_| \___/\__,_|\_,_\__|\__|_\___/_||_|
                                                     |___/                                                          """)
    time.sleep(1)
    print("""
    \n\n
    88888888888888888888888888888888888888888888888888888888888888888888888
    88.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..88
    88   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  88
    88      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  88
    88..__  |     |`-!._ | `.| |_______________||."'|  _!.;'   |     _|..88
    88   |``"..__ |    |`";.| i|_|MMMMMMMMMMM|_|'| _!-|   |   _|..-|'    88
    88   |      |``--..|_ | `;!|l|MMoMMMMoMMM|1|.'j   |_..!-'|     |     88
    88   |      |    |   |`-,!_|_|MMMMP'YMMMM|_||.!-;'  |    |     |     88
    88___|______|____!.,.!,.!,!|d|MMMo * loMM|p|,!,.!.,.!..__|_____|_____88
    88      |     |    |  |  | |_|MMMMb,dMMMM|_|| |   |   |    |      |  88
    88      |     |    |..!-;'i|r|MPYMoMMMMoM|r| |`-..|   |    |      |  88
    88      |    _!.-j'  | _!,"|_|M<>MMMMoMMM|_||!._|  `i-!.._ |      |  88
    88     _!.-'|    | _."|  !;|1|MbdMMoMMMMM|l|`.| `-._|    |``-.._  |  88
    88..-i'     |  _.''|  !-| !|_|MMMoMMMMoMM|_|.|`-. | ``._ |     |``"..88
    88   |      |.|    |.|  !| |u|MoMMMMoMMMM|n||`. |`!   | `".    |     88
    88   |  _.-'  |  .'  |.' |/|_|MMMMoMMMMoM|_|! |`!  `,.|    |-._|     88
    88  _!"'|     !.'|  .'| .'|[@]MMMMMMMMMMM[@] \|  `. | `._  |   `-._  88
    88-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-88
    88      |_.'|   .' | .' |/                   \  \ |  `.  | `._-Lee|  88
    88     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  88
    88  _.'     !'|   .' | /                       \|  `  |  `.    |`.|  88
    88 vanishing point 888888888888888888888888888888888888888888888(FL)888 """)

#function to initiate game
def start_game():
    time.sleep(1)
    global player
    player = input("\n\nTell me traveller, what is your name?: ")
    time.sleep(1)
    starting = input(f"\nWelcome {player}, to a tale of horror and woe. Are you ready to begin? [Y/N]: ").upper()
    time.sleep(1)
    if starting == "Y" or starting == "YES":
        print("\nAh, a brave soul.")
        intro()
    elif starting.upper() == "N" or starting.upper() == "NO":
        print("\nYou have no choice, you must go on.")
        intro()
    else:
        print("\nI'll take that as a yes.")
        time.sleep(1)
        intro()

def intro():
    time.sleep(1)
    print("""\nYou awaken on the dusty floor of a small, dark room. You have no memory of how you came to be here.
    \nYou rise slowly to your feet.
    \nLooking around, you notice that the walls have been roughly hewn out of stone. A torch on the wall is flickering, pulsing a dim light that barely fills the room. At each end of the room lie two open doorways, leading off in what appear to be corridors. You're wondering where each lead, when you hear a faint noise from the doorway behind you.""")
    time.sleep(1)
    intro1 = input("\nDo you investigate the noise? [Y/N]: ")
    time.sleep(1)
    if intro1.upper() == "Y" or intro1.upper() == "YES":
        print("""\nYou peer into the dark. On the walls, spaced every few meters are burning torches. The corridor appears to go on forever. You hear the noise again, a low, unnatural moan that echoes towards you. In the distance, you see a torch disappear, absorbed by something darker than the gloom surrounding it. It moves towards you, a shambling lovecraftian horror. A bloated, writhing mass of shadows with a grinning childlike face. \nInstinctively, you know you must escape from it.\n""")
        torch()
    elif intro1.upper() == "N" or intro1.upper() == "NO":
        print("\nAs you back away from the noise it sounds again, but closer. Unable to stop yourself, you glance back to see a horror shambling towards you. It is hard to see clearly as it appears to absorb the light, but a single look at its childlike face lets you know that to survive, you must escape ")
        torch()
    else:
        print("\nYou dither as the entity draws closer. Peeking through the doorway, you can see its indistinct form more clearly. It's hulking body seems to absorb the light, and its oddly childlike face grins with malice at you. You must make haste!")
        time.sleep(1)
        torch()

#function for interaction with an item
def torch():
    time.sleep(1)
    torch1 = input("\nTake the torch from the wall before you leave? [Y/N]: ")
    time.sleep(1)
    if torch1.upper() == "Y" or torch1.upper() == "YES":
        print("\nYou remove the torch, and make your way down the passage.\n")
    elif torch1.upper() == "N" or torch1.upper == "NO":
        print("\nYou must have fantastic night vision. You make your way down the passage.\n")
    else:
        print("\nTime is short, and the challenges ahead unknown. You take the torch and move on.")
    time.sleep(1)


#function that prints room descriptions (from list), and also randomly picks a phobia item from phobia list, 
# calls up one of its manifesations attributes, associates art wtih it, and kicks item out of phobias list
def question(number):
    time.sleep(1)
    print("\n \n")
    print(rooms[number])
    print("\n")
    print("Press ENTER to continue")
    #creating a random list of phobias from the list phobias_list
    random_sample = random.sample(phobias_list, 3)
    #create a number to print prior to each manifestation, 
    i = 1
    # for each phobia instance from the random sample from the list phobias, we select a random sample from manifestations to print, and also delete it. This for loop will repeat as many times as the length of the sample list (3 or 2 in the final choice)
    for phobia_instance in random_sample:
        #create input to force the text to pause and only resume after ENTER  is pressed
        enterinput = input()
        #pick a random manifestation out of the list manifestations, from the class object corresponding to the phobia and print it
        manifestation = random.choice(phobia_instance.manifestations)
        phobiainstanceart = phobia_instance.art
        #print the previous number, which goes up with each interation
        time.sleep(1)
        print(phobiainstanceart)
        print(f"{i}. {manifestation}")
        time.sleep(1)
        print("\nPress ENTER to continue")
        #instantly remove this manifestation from its list, to avoid reuse
        phobia_instance.manifestations.remove(manifestation) 
        # up the number so it prints 2 and 3 next time
        i += 1
        time.sleep(0.3)
    input()
    #call on function to get integer result, take out 1 to find the phobia's position on the random choice list, and find and kick out of phobias_list
    answer = askforinput3()
    answerindex = int(answer) - 1
    selectedphobia = random_sample[answerindex]
    phobias_list.remove(selectedphobia)

#function to ask for input, accept only answers 1-3 and return equivalent integer, or print error message and loop
def askforinput3():
    while True:
        answer3 = input("\nPlease make a choice, 1-3: ")
        if answer3 == "1":
            return 1
        elif answer3 == "2":
            return 2
        elif answer3 == "3":
            return 3
        else:
            print("This is not a valid choice, try again")


 #function to ask for input, accept only answers 1-2 and return equivalent integer, or print error message and loop (to be used when there are only two phobias left)
def askforinput2():
    while True:
        answer3 = input("\nPlease make a choice, 1-2: ")
        if answer3 == "1":
            return 1
        elif answer3 == "2":
            return 2
        elif answer3 == "3":
            return 3
        else:
            print("This is not a valid choice, try again")
    

def transitions():
    #function to print transition texts out of a list and remove them afterwards
    print("\n")
    time.sleep(1)
    trans_choice = trans1[0]
    print(trans_choice)
    trans1.remove(trans_choice)   
    time.sleep(2) 



def visionquestion():
    #function to present final two choices from phobia list
    time.sleep(1)
    print("\nYou enter the chamber, it's as tall as a cathedral. There's daylight streaming from above, you're obviously near the surface. You steal a glance behind you and there it is. It looks tall and strangely shapeless, and ineffably sad. You're paralysed by fear, but notice that it's pointing. Not at you, but behind you. You turn around to see two visions, covering two exits. Which one will you pick?")
    print("\nPress ENTER to continue")
    #set i = 1, it'll print the value 1-3 before each manifestation
    i = 1
    for phobia_instance in phobias_list:
        enterinput = input()
        vision = (phobia_instance.vision)
        visionart = (phobia_instance.art)
        print(visionart)
        print(f"{i}. {vision}")
        print("\nPress ENTER to continue")
        i += 1        
    time.sleep(1)
    #call to function that will return a valid integer
    vision_choice = askforinput2()
    answerindex = int(vision_choice) - 1
    selectedphobia = phobias_list[answerindex]
    phobias_list.remove(selectedphobia)

def bat():
    #random little function to print a bat!
    time.sleep(1)
    print("\n What's that sound?")
    time.sleep(2)
    print("""
    ─────▄───▄
─▄█▄─█▀█▀█─▄█▄
▀▀████▄█▄████▀▀
─────▀█▀█▀
    
    
    """)
    time.sleep(1)
    print("WHOA. Shoo, flying rat!\n")
    input(f"Do you hate bats, {player}?[Y/N]: ")
    print("Yeah, me too.") 
    time.sleep(1)
    print("Good chat.")
    time.sleep(1)



def finalquestion():
    #function to offer a final binary question. Picks the remaining two phobias from list. If user picks face, it'll give a happy ending using the nonthretening property from Phobia class. If RUNm, it'll 
    time.sleep(1)
    while True:
        final_answer = input("\nWill you turn and run, or face the monster? F for FACE, R for RUN  ").upper()
        if final_answer == "RUN" or final_answer == "R":
            print(phobias_list[0].art)
            print(f"You feel its hand on your shoulder. From up close, it looks like a small child, and also your biggest nightmare. Its jaws distend, moving towards your face, it swallows you and {phobias_list[0].fatality} According to our very accurate personality test, your biggest fear was {phobias_list[0].name}, and now you must live with it. Such is the irony of life and death, {player}.")
            break
        elif final_answer == "FACE" or final_answer == "F":
            print(phobias_list[0].art)
            print(f"The creature for a minute looks like you biggest fear: {phobias_list[0].nonthreatening}. Then it turns into a small furry kitten. You pick up your purring pal and you leave this accursed place, at peace with your fears.")
            break
        else:
            print("Not a valid choice, try again")
    # final if else choice to start runthrough again or exit.
    time.sleep(1)
    playagain = input("Start again? [Y/N] ").upper()
    if playagain == "Y" or playagain == "YES":
        runthrough()
    elif playagain == "N" or playagain == "NO":
        print("OK, mortal, cheers for playing.")
    else:
        print("You've clearly been affected by the horror within. Don't worry, it's just a game.")

#a function that contains all the functions and runs them through in an appropriate order
def runthrough():
    makeacopiedlist()
    printcorridor()
    start_game()
    question(0)
    transitions()
    question(1)
    transitions()
    question(2)
    transitions()
    question(3)
    bat()
    visionquestion()
    finalquestion()
runthrough()





