from agps.utils import action_prompt, move, fight_words, wait_words

has_castle = True


def enter(name, inventory):
    global has_castle
    if has_castle:
        print("You are on a wide, sandy beach. You see a formidable sand castle towering above you.\n"
              "The precocious child responsible stands on the battlements brandishing a golden key.")
    else:
        print("You are on a wide, sandy beach. It is so peaceful.")
    print()
    while True:
        action = action_prompt(inventory)
        if action[0] in fight_words and 'child' in action and has_castle:
            print("You scramble pathetically at the walls while the child laughs.\n"
                  "Suppose you could wait for the tide to bring the castle down.")
        elif action[0] in wait_words and 'tide' in action and has_castle:
            print("The castle washes away with the tide taking the small child with it.\n"
                  "You see a key on the floor and pick it up.")
            inventory['golden key'] += 1
            has_castle = False
        elif action[0] is move:
            return action[1]
        else:
            print("Sorry, I don't understand.")

