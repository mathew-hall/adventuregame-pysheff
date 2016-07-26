"""(1, -1)"""
from agps.utils import action_prompt, move, take_words, give_words, use_words, fight_words, talk_words
import time

positive_words = {'yes', 'yeah', 'sure', 'ok', 'si'}

def enter(name, inventory):
    print("You cut through the dense forest and find yourself in the House of Commons.")
    print("The great hall is empty except for an eldery man (\033[1;41mjeremy\033[0m) dressed like a geography teacher.")
    print("He is reading through reams of printed emails.")
    print()
    while True:
        action = action_prompt(inventory)
        if action[0] is move:
            if action[1][0] == 'e':
                print("There are Tories to the East, you don't want to go there.")
            else:
                return action[1]
        if action[0] in fight_words and 'jester' in action:
            print("But Jingle is our friend!")
        if action[0] in fight_words and 'jeremy' in action:
            print("You don't want to hurt jeremy, he says he has thousands of friends... Unfortunately none here in the Commons.")
        if action[0] in talk_words and 'jeremy' in action:
            talk_to_jeremy()
        if action[0] in talk_words and 'kid' in action:
            print("\"Sorry mate, I don't have any golden keys, only pokemon.\"")
            print("\"Try going West!\"")

def talk_to_jeremy():
    print("I seem to have lost my friends, can you help me with my work?")
    while True:
        response = input('> ').lower().split()
        print(response)
        if response[0] in positive_words:
            print("\"I have a question here for the Prime Minister from Maureen in Basingstoke.\"")
            print("\"Maureen says 'given the current economic climate should...'\"")
            time.sleep(6)
            print("...")
            print("You begin to feel sleepy")
            time.sleep(2)
            print("...")
            time.sleep(2)
            print("...")
            time.sleep(2)
            print("He's still talking...")
            time.sleep(2)
            print("...")
            time.sleep(2)
            print("...")
            time.sleep(4)
            print("A teenager wonders in playing Pokemon Go")
            time.sleep(2)
            print("...")
            print("Jeremy attempts to recruit him to the shadow cabinet")
            print("...")
            time.sleep(2)
            print("...")
            time.sleep(2)
            print("The kid is not interested")
            return
        else:
            print("Oh please help! They've all gone and left me!")
