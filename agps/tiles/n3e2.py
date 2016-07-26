from agps.utils import action_prompt, take_words, move
import time

def wait_for_move(inventory):
    while True:
        action = action_prompt(inventory)
        if action[0] is move:
            return action[1]

def enter(name, inventory):
    if inventory['§1234']:
        print("Bandits are running away from you with a golden key in their grasp.")
        time.sleep(1)
        print("They drop the key in panic. Lucky huh. It falls into the swamp and starts sinking. Grab it quick!")
        print()

        start = time.time()
        while True:
            action = action_prompt(inventory)
            if action[0] in take_words:
                if time.time() < start +15:
                    inventory['golden key'] +=1
                    print("You have the key! It's dirty... but it's yours!")
                    inventory['§1234'] = 0
                else:
                    print("It's sunk. It's too deep to pull out... maybe you find a stick")
                return wait_for_move(inventory)
            else:
                print("But it's a key. It may be dirty, but still TAKE it! Cmon!")
                print("It's been sinking for", time.time() - start)

    else:
        print("You are in a swamp. You look down and see foot print that mean absolutely nothing to you.")
        print("So you continue walking...")
        return wait_for_move(inventory)
