"""(0, 2)"""

from agps.utils import action_prompt, move, take_words

GOLD = 'pile of gold coins'

scene_contents= {
    'tiger': 1,
    GOLD: 1,
    'golden key': 0,
}

def take_tiger(inventory):
    if scene_contents['tiger'] > 0:
        scene_contents['tiger'] -= 1
        inventory['tiger'] += 1
        print("Reaching up, you pick up the tiger.")
    else:
        print("There is no tiger here.")

def take_gold(inventory):
    if scene_contents[GOLD] > 0:
        scene_contents[GOLD] -= 1
        inventory[GOLD] += 1
        print("Reaching down, you pick up the gold.")
    else:
        print("There is no gold here.")

def stock_scene(inventory):
    if 'key' not in inventory and GOLD in inventory and 'tiger' in inventory:
        print("OOooooo.. something happened in your bag!")
        inventory[GOLD] -= 1
        inventory['golden key'] += 1

def enter(name, inventory):
    stock_scene(inventory)
    print("You come across a cottage with two doors. One door is (b)lue and the other (r)ed.")
    print("You might want to choose a door? Or perhaps both? Do you feel lucky?")
    print()
    while True:
        action = action_prompt(inventory)
        if action[0] is move:
            return action[1]
        if action[0] in ('b', 'blue', 'r', 'red'):
            if action[0] in ('red', 'r'):
                if scene_contents['tiger']:
                    print("Aaarrgh, it's a tiger!")
                    print("Do you want to (r)un from, (f)ight or (b)efriend the tiger?")

                    answer = []
                    while not answer:
                        answer = input('> ').lower().split()
                        if 'r' in answer or 'run' in answer:
                            print("You are running in a random direction")
                            return 'w'
               
                        elif 'f' in answer or 'fight' in answer:
                            print("Ouch! The tiger nearly ate you so you run away screaming!")
                            return 'w'
               
                        elif 'b' in answer or 'befriend' in answer:
                            print("You sing the Tiger Befriending Song you learnt as a child. "
                                  "The tiger is enraptured. It agrees to join you on your quest.")
                            take_tiger(inventory)
                        else:
                            answer = []
                else:
                    print("What are you doing back here?")
               
               
            if action[0] in ('blue', 'b'):
               deal_with_gold(inventory)
        else:
            print("Sorry, I don't understand.")

def deal_with_gold(inventory):
    if not scene_contents[GOLD]:
        print("What are you doing back here?")
        return
        
    print("Wow! It's a pile of gold coins!")
    
    while True:
        action = action_prompt(inventory)
        if (action[0] in take_words) and ('gold' in action):
            take_gold(inventory)
            return
        else:
            print("Sorry, I don't understand.")
