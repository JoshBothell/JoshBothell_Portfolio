# Josh Bothell
# CS1400 - Section 02
# September 24, 2020
# A simple menu based program meant to emulate the art-o-mat art project.
# It is essentially an old fashion cigarette vending machine modified to sell art.

import random


def menu(should_print):  # The basic options and input screen, input check happens here.
    if should_print:
        print("s - report the machine status\n"
              "d - drop in a quarter\n"
              "1 - pull the 1st knob\n"
              "2 - pull the 2nd knob\n"
              "3 - pull the 3rd knob\n"
              "4 - pull the 4th knob\n"
              "r - restock the machine\n"
              "q - quit")
    options = ['s', 'd', '1', '2', '3', '4', 'r', 'q', '']
    selection = input().lower()
    if selection not in options:
        print("I do not understand")
        return menu(False)
    else:
        return selection


def init_stock():  # initialize the stock.
    inv_init = []
    for x in range(0, 4):
        inv_init.append(random.randint(2, 10))
    return inv_init


def status(inv, bank, choices, bal):  # prints the current inventory and total bank.
    for i in range(4):
        print("(%s) %s packs of %s" % (i+1, inv[i], choices[i]))
    print("There is $" + str(bank) + " in the machine bank")
    print("Your current balance is $%s" % bal)


def drop_quarter(bal):  # adds a quarter to the balance, and makes the noise.
    print("*clink*")
    bal += 0.25
    return bal


def pull_knob(knob, inv, bal, bank, choices):  # checks that the balance is high enough and the item is in stock
    if bal >= 0.75:  # it will perform the correct action based on the values.
        if inv[knob] > 0:  # if they have enough money and it is in stock, it will dispense.
            print("A pack of", choices[knob], "slides into view.")
            bal -= 0.75
            bank += 0.75
            inv[knob] -= 1
        else:  # if they have enough money but the item is out of stock, it takes the money, but dispenses nothing.
            print("You hear mechanical clanking, but no boxes appear.")
            bal -= 0.75
            bank += 0.75
    else:  # if you do not have enough money, nothing happens.
        print("(nothing happens)")
    return inv, bal, bank


def restock(inv_local):  # The inventory will be managed with the list 'stocked'.
    # a random value int from 1 - 7 will be added to the current value of each option.
    # the 'machine' has a max of 10 however, and will cap at that point.
    print("A grouchy-looking attendant shows up, opens the back, fiddles around a bit, closes it, and leaves.")
    for i in range(0, 4):
        inv_local[i] += random.randint(4, 7)
        if inv_local[i] > 10:
            inv_local[i] = 10
    return inv_local


def main():
    bank = float(random.randint(5, 15)) + (0.25 * random.randrange(4))  # initializes a random bank.
    choices = [  # initializes the current 4 options.
        "Whittington B&W photos",
        "Escher woodcuts",
        "da Vinci sketches",
        "Pollock drop cloth clippings"
    ]
    inv = init_stock()  # uses init_stock to initialize the inventory.
    bal = 0.0  # starts the user balance off at zero.
    should_print = True
    while True:  # checks the user input and calls the respective function.
        response = menu(should_print)
        should_print = False
        if response == 's':
            status(inv, bank, choices, bal)
        elif response == 'd':
            bal = drop_quarter(bal)
        elif response in ['1', '2', '3', '4']:
            knob = int(response) - 1
            inv, bal, bank = pull_knob(knob, inv, bal, bank, choices)
        elif response == 'r':
            inv = restock(inv)
        elif response == '':
            should_print = True
        else:
            break


main()
