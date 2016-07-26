"""(0, 3)"""

from agps.utils import action_prompt, move, take_words, look_words, use_words, GameLost

import random

scene_contents = {'world domination plans',5}
timer = -1

launch_code = 'piece of paper labelled: 000000'
def take_instruments(inventory):
    
    def instrument_type():
        return random.choice(['new world order plan','compromising photograph of a world leader',launch_code])
    
    if scene_contents['world domination plans'] > 0:
        inventory['world domination plans'] += 1
        scene_contents['world domination plans'] -= 1
        inst_type = instrument_type()
        inventory['inst_type'] = 1
        print("You shuffle through the papers and grab a %s"%inst_type)
    else:
        print("Looks like someone's already cleaned the office out")

def use_code(inventory):
    if inventory[launch_code] > 0:
        timer = 0
        print("You tap the serial numbers into the computer terminal.")
        print("The ground begins to shake. The TV shows an urgent bulletin; 'government resigns en masse'")
        print("In the distance columns of smoke rise from the horizon.")
        print("")
        print("You hear running footsteps and irritated chatter. You back away from the computer.")
        print("Better hide, fast!")
    

def enter(name, inventory):
    print("You can make out a large silhouette through the undergrowth.")
    print("Fighting the brambles you reach a revolving door and head inside.")
    print("You take the elevator and find yourself at the top of a large office block.")
    print("There is a desk in the office.")
    print()
    while True:
        action = action_prompt(inventory)

        if action[0] in look_words and 'desk' in action:
            print("There is a folder on the desk labelled Evil Plans.")
        if action[0] in look_words and 'folder' in action:
            if scene_contents['world domination plans']:
                print("There are some papers in the desk.")
            else:
                print("There is nothing on the desk")
        if action[0] in take_words and 'papers' in action:
            take_instruments(inventory)
        if action[0] in use_words and 'paper' in action:
            use_code(inventory)
        if timer == 10:
            print("The guards are here. They don't seem to be interested in a conversation.")
            raise GameLost("The guards were unsympathetic to your claims of being a stooge")
        if timer >= 0:
            print("The footsteps are getting closer.")
            timer += 1