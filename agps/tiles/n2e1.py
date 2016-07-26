from agps.utils import action_prompt

def enter(name, inventory):
    print("You see a castle over the horizon to the North!")
    print()
    return action_prompt(inventory)[1]
