# Josh Bothell
# CS1400 Section 02
# Sept. 22, 2020
# A program built from a flowchart meant to imitate the thought process of a dog.
# uses a top-down -> left-right approach where the topmost questions are not indented.

is_object = input("Is it an object [y/n]?\n")  # top level
if is_object == 'y':
    can_eat = input("Can you eat it [y/n]?\n")  # level 2
    if can_eat == 'y':
        print("Eat it.")
        was_good = input("Was it good [y/n]?\n")  # level 3
        if was_good == 'y':
            print("Wag your tail.\n")
        else:
            print("Puke it out.")
            print("Re-eat it.")
    else:
        is_tennis = input("Is it a tennis ball [y/n]?\n")
        if is_tennis == 'y':
            print("pick it up.")
            print("Return to owner.")
        else:
            print("Bark at it.")
else:
    is_sound = input("Is it a sound [y/n]?\n")
    if is_sound == 'y':
        print("Bark at it.")
    else:
        print("Ignore it.")
print("Done!")
