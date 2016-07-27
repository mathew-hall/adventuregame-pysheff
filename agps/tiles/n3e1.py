from agps.utils import action_prompt, move, take_words, give_words
import time

scene_contents = {'compass' :1}

def wait_for_move(inventory):
    while True:
        action = action_prompt(inventory)
        if action[0] is move:
            return action[1]

def enter(name, inventory):
    if not inventory['golden key']:
        print("You see a super boring castle with absolutely nobody waiting or watching... honest. But i'd leave quick.")
        return wait_for_move(inventory)
    if not scene_contents['compass']:
        print("The chest is empty")
        return wait_for_move(inventory)

    print("You enter the castle - the door slams behind. You're trapped! Ooosh.")
    print("There is a glowing chest in front of you. It glows green.")
    print()
    trap(name, inventory)
    return wait_for_move(inventory)

def trap(name, inventory):
    while True:
        action = action_prompt(inventory)
        if action[0] is move:
            print("You're trapped! Tough.")
        if (action[0] in take_words) and ('chest' in action) and scene_contents['compass']:
            scene_contents['compass'] = 0
            inventory['compass'] = 1
            print("There is a glowing green compass inside")
            time.sleep(1)
            print("But, behind you are some bandits demanding your keys!!")
            while True:
                action = action_prompt(inventory)
                if action[0] in give_words:
                    inventory['golden key'] -= 1
                    inventory['§1234'] = 1
                    print("Bandits take the key and flee east as the door opens.")
                    return
