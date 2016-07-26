"""(0, 3)"""

from agps.utils import action_prompt, move, take_words

def enter(name, inventory):
	print("You begin to slide down a hidden scree slope.")
	print("It begins to get darker")
	print()
	while True:
		_ = action_prompt(inventory)
		print("You are dead.")