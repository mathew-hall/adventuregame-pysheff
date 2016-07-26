from agps.utils import action_prompt, move, take_words

scene_contents = {}


def pick_up_jellyfish(name, inventory):
    print(str.format(
        "You try to pick up the jellyfish in order to put it in your bag. What a stupid idea, {}!", name))
    print("Ouch, that stings! It hurts so much you drop your bag and all your items fall out.")
    for item, count in list(inventory.items()):
        scene_contents[item] = inventory[item]
        del inventory[item]

    enter(name, inventory)


def enter(name, inventory):
    print("You are on a wide, sandy beach. There's a wobbling jellyfish on the beach.")
    for item, count in scene_contents.items():
        if count > 1:
            print(str.format("There are {} {}s on the beach.", count, item))
        else:
            print(str.format("There is a {} on the sand.", item))
    print()
    while True:
        action = action_prompt(inventory)
        if action[0] in take_words and 'jellyfish' in action:
            pick_up_jellyfish(name, inventory)
        elif action[0] in take_words and 'everything' in action:
            if len(scene_contents) > 0:
                for item, count in list(scene_contents.items()):
                    inventory[item] = count
                    del scene_contents[item]
                    print(str.format("You pick up the {}.", item))
            else:
                print("The sand slips through your fingers.")
        elif action[0] in take_words:
            for item, count in list(scene_contents.items()):
                if item in action:
                    inventory[item] = count
                    del scene_contents[item]
                    print(str.format("You pick up the {}.", item))
        elif action[0] is move:
            return action[1]
        else:
            print("Sorry, I don't understand.")
